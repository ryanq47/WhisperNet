import json
import os

import logging
import inspect

from flask import jsonify, send_from_directory, render_template, flash, redirect
from flask_login import LoginManager, login_required

## API stuff
from functools import wraps
from flask import request, jsonify, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required

from SecurityEngine.AuthenticationHandler import AccessManagement
#@AccessManagement.role_required()

import hashlib
import time
import threading
from Utils.Logger import LoggingSingleton


################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "FileHost"
    author  = "ryanq47"
    endpoint = "/filehost"
    classname = "FileHost"
    plugin_type = "Builtin"


################################################
# Other Stuff
################################################
SUBROUTINE_REFRESH_TIME = 5

class FileHost():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()

        ## Holds a JSON string of currently hosted files
        self.current_hosted_files = None
        ## holds calucalted file access logs         
        self.current_file_access_logs = None
        ## Node checkin logs
        self.node_checkin_logs = []
        ## raw file access logs FROM NODES
        self.node_file_access_logs = []


        subroutine_thread = threading.Thread(
            target=self.filehost_subroutine
        )
        subroutine_thread.daemon = True
        subroutine_thread.start()

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.logger.debug(f"{self.logging_debug_symbol} Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        self.logger.debug(f"{self.function_debug_symbol} {inspect.stack()[0][3]}")
        self.app.route(f'/{Info.endpoint}', methods = ["GET"])(self.filehost_base_directory)
        self.app.route(f'/api/{Info.endpoint}/command', methods=["GET"])(self.command_endpoint)
        self.app.route(f'/{Info.endpoint}/<path:filename>', methods = ["GET"])(self.filehost_download_file)
        self.app.route(f'/{Info.endpoint}/upload', methods = ["POST"])(self.filehost_upload_file)
        self.app.route(f'/api/{Info.endpoint}/files', methods = ["GET"])(self.filehost_api_file_listing)
        self.app.route(f'/api/{Info.endpoint}/checkin', methods = ["POST"])(self.filehost_checkin)
        self.app.route(f'/api/{Info.endpoint}/updatefilelogs', methods = ["POST"])(self.filehost_file_access_logs)
        self.app.route(f'/api/{Info.endpoint}/filelogs', methods = ["GET"])(self.filehost_api_get_file_access_logs)
        self.app.route(f'/api/{Info.endpoint}/nodelogs', methods = ["GET"])(self.filehost_api_get_checkin_logs)
        self.app.route(f'/api/{Info.endpoint}/upload', methods = ["POST"])(self.filehost_api_upload_file)

    ## Something funky happening here, I bet somethings not returning right, and as 
    ## such, erroring out.
    @jwt_required()
    @AccessManagement.role_required('filehost_admin')
    def command_endpoint(self):
        '''
        Iirc endpoint for commands for the node. this whole thing needs a review
        '''
        json = {
            "command": "stuff"
        }

        return "data"#jsonify(json)
    
    ## disabling until I can find a way to do an OR here, web OR api login.
    #@login_required
    def filehost_download_file(self, filename):
        print(f"Filename; {filename}")
        return send_from_directory(
            "PluginEngine/Plugins/FileHostPlugin/Files",
            filename,
            as_attachment=True)

    # these don't need a (). Funky
    #also not exactly the most secure. no validation on upload
    #@login_required
    def filehost_upload_file(self):
        '''
        Endpoint for uploading files to the FileHost plugin. 
        Not Secure yet.
        

        dev: needs a refactor/rething. Maybe throw forms in a stataic class
        '''
        #return "Not Implemented"
        ## Note, CSRF is missing is issue
        try:

            if request.method == 'POST':
                uploaded_file = request.files['file']

                if uploaded_file:
                    # Save the uploaded file to a specific directory
                    uploaded_file.save('PluginEngine/Plugins/FileHostPlugin/Files/' + uploaded_file.filename)

                    #flash("File uploaded successfully")
                    return redirect("/filehost")

            
            #flash("Upload Failed")
            return redirect("/filehost")
        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Error uploading file: {e}")
            #flash("Upload Failed")
            return redirect("/filehost")


    #@login_required
    def filehost_api_upload_file(self):
        '''
        Endpoint for uploading files to the FileHost plugin. 
        Not Secure yet.
        

        dev: needs a refactor/rething. Maybe throw forms in a stataic class
        '''
        print("API uplaod triggered")
        #return "Not Implemented"
        ## Note, CSRF is missing is issue
        try:

            if request.method == 'POST':
                uploaded_file = request.files['file']

                if uploaded_file:
                    # Save the uploaded file to a specific directory
                    uploaded_file.save('PluginEngine/Plugins/FileHostPlugin/Files/' + uploaded_file.filename)

                    #flash("File uploaded successfully")
                    #return redirect("/filehost")
                    print("file worked ===========================")
                    return make_response("", 200)

            return make_response("", 404)
            #flash("Upload Failed")
            #return redirect("/filehost")
        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Error uploading file: {e}")
            #flash("Upload Failed")
            return make_response("", 404)


    @login_required
    def filehost_base_directory(self):
        '''
        Code for the dashboard at /filehost

        eventually.. if not auth then re-auth.

        Also, break these into sub functions
        '''
        servername = "FileHost Plugin"
        list_of_files = []

        ## populate the list of plugins from the database
        for file in os.listdir("PluginEngine/Plugins/FileHostPlugin/Files/"):
            '''
            Data comes back in a tuple:
            [('FlaskAPIListnener', '/flasklistener', 'ryanq.47', 'Builtin', 0), (more data)]
            This makes it slightly less readable for creating the dict below. Also,
            should prolly make a dedicated function for this.
            '''
            try:
                ## chagne to join
                with open(f"PluginEngine/Plugins/FileHostPlugin/Files/{file}", "rb") as f:
                    data = f.read(40)

                dict_ = {
                    'name': file,
                    'contents': data,
                }

            except Exception as e: 
                dict_ = {
                    'name': f"ERROR: {e}",
                    'contents': '',
                }
            finally:
                list_of_files.append(dict_)

        ## populate the checkin messages from the external filehosts  

        ## Do needed transfomrations to data
        self.filehost_data_management()

        return render_template('filehost-dashboard.html', 
                            files=list_of_files,
                            servername = servername,
                            nodedata = self.node_checkin_logs,
                            filelogdata = self.node_file_access_logs)

################################################
# Hosted files
################################################
    #@jwt_required()
    def filehost_api_file_listing(self):
        '''
            Endpoint for listing the files in the FileHost plugin. Purely for API
            access only, and requires a JWT to access.

        '''
        ## Returns json string
        return self.current_hosted_files

    @BasePlugin.optimization_calc_n_cache
    def filehost_calculate_current_hosted_files(self):
        '''
        Calculates/performs needed actions to get the files currently hosted
        by the server. 
        
        '''

        json_file_data = {}
        filenames = os.listdir("PluginEngine/Plugins/FileHostPlugin/Files/")

        for file in filenames:
            try:
                #print(file)
                file_path = f"PluginEngine/Plugins/FileHostPlugin/Files/{file}"
                file_size = os.path.getsize(file_path)

                file_data = {
                    file:{
                            "filename": file,
                            ## Note, this is depednent on what you set the file endpoint to. 
                            "filedir": f"{Info.endpoint}/{file}",
                            "filesize": file_size,
                            "filehash": self.md5_hash_file(file_path),
                        }
                }
                json_file_data.update(file_data)

            except Exception as e:
                self.logger.warning(f"{self.logging_warning_symbol} Error with getting file info: {e}")

        return json_file_data

################################################
# File Access Logs
################################################
    ## GET endpoint
    def filehost_api_get_file_access_logs(self):
        '''
        API endpoint for GETTING 
        
        '''
        #print(self.current_file_access_logs)
        return self.current_file_access_logs

    @BasePlugin.optimization_calc_n_cache
    def filehost_calculate_file_access_logs(self):
        '''
        ## Currently using placeholder data

        Calculates & creates the file access log JSON to serve via the API
        
        '''
        self.filehost_data_management()
        temp_dict = {}
        i = 0



        ## this works a little weird. in order to have mutliple json rows, each "key" needs to 
        ## be diff so i gave each key a number. not ideal but it works
        for data in self.node_file_access_logs:
            print(data)
            file_data = {
                i:{
                    "filename": data['filename'], #"placeholder", #data['filename'],
                    "accessorip": data['file_accessor_ip'],# My dumbass named this weird somewhere.
                    "hostingserver": data['node_name'],##data['hostingserver'],
                    "timestamp": data['timestamp'],#data['timestamp'],
                    "httpstatuscode": data['httpstatuscode']
                }
            }
            temp_dict.update(file_data)
            i = i + 1
        ## rename this
        return temp_dict #jsonify(temp_dict)

        #return self.node_file_access_logs

        #return jsonify(self.node_file_access_logs)

    ## POST endpoint for getting data from nodes
    def filehost_file_access_logs(self):
        '''
        An endpoint to post file access.
        Takes a post request.
        URI: /api/filehost/filelogs
        
        {

            "filename":"notsafefile.exe",
            "accessorip":"y.y.y.y"
            "hostip":"x.x.x.x",
            "hostingserver":"fh01"
            "timestamp":"010101"

        }
        '''
        try:
            file_name = request.json.get('filename')
            file_accessor_ip = request.json.get('accessorip')
            node_ip = request.json.get('hostip')
            node_name = request.json.get('hostingserver')
            file_timestamp = request.json.get('timestamp')
            http_status_code = request.json.get('httpstatuscode')


            log_string = f"{self.logging_info_symbol} File Access: Plugin Name: '{node_name}' " \
            f"Plugin IP: '{node_ip}' " \
            f"filename: '{file_name}' " \
            f"accessor IP: '{file_accessor_ip}' " \
            f"HTTP status code: '{http_status_code}' " \
            f"Timestamp: '{file_timestamp}' "

            self.logger.info(log_string)


            data_dict = {
                "node_name":node_name,
                "file_accessor_ip":file_accessor_ip,
                "filename":file_name,
                "timestamp":file_timestamp,
                "httpstatuscode":http_status_code
            }

            self.node_file_access_logs.append(data_dict)
            #print(self.node_checkin_logs)

            return "success"
        

        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Error with filelogs: {e}")



################################################
# Node Checkin Stuff
################################################

    def filehost_checkin(self):
        '''
        An endpoint to post checkin data.
        Need to decide if I want to make this protected or not. for now its not
        
        {
            "name":"",
            "ip":"",
            "message":"syncing | sync successful | sync failed | error"
            "timestamp":""
        
        }
        '''
        try:
            plugin_instance_name = request.json.get('name')
            plugin_external_ip = request.json.get('ip')
            plugin_message = request.json.get('message')
            plugin_timestamp = request.json.get('timestamp')

            ## Dump data to DB -- for now just doing a non-persistent message setup
            '''
            Needs to:
                if new fh, add row.

                if existing fh, update row with new data. primary key will be name
            
                    or... just log it. no need for persistent DB data for now.
                    The only having to having a DB is for currently connected nodes. 
                    Downsides are complexity
            
            '''

            log_string = f"{self.logging_info_symbol} Checkin: Plugin Name: '{plugin_instance_name}' " \
            f"Plugin IP: '{plugin_external_ip}' " \
            f"Message: '{plugin_message}' " \
            f"Timestamp: '{plugin_timestamp}' "

            self.logger.info(log_string)


            data_dict = {
                "name":plugin_instance_name,
                "ip":plugin_external_ip,
                "message":plugin_message,
                "timestamp":plugin_timestamp,
            }

            self.node_checkin_logs.append(data_dict)
            #print(self.node_checkin_logs)

            return "success"
        

        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Error with checkin: {e}")

    def filehost_api_get_checkin_logs(self):
        '''
        Logs for file checkins displayed to the api
        
        '''
        temp_dict = {}

        ## accidently made it so only one log of each thing shows up here. win win I suppose?

        ## simlar to filehost_api_get_file_access_logs, but limits the keys to the name of the node checking in
        ## This allows for updates of the nodes without duplicat nodes to process
        for data in self.node_checkin_logs:
            file_data = {
                data['name']:{
                    "name": data['name'],
                    ## Note, this is depednent on what you set the file endpoint to. 
                    "ip": data['ip'],
                    "message": data['message'],
                    "timestamp": data['timestamp'],
                }
            }
            temp_dict.update(file_data)
        ## rename this
        return jsonify(temp_dict)

################################################
# Some failsafes
################################################

    def filehost_data_management(self):
        '''
        Does some general actions on data to make sure it's compliant/dosen't run away 
        or get unmanageable. Everything trimmed here has a log fiel for each respective
        event, so this doens't just vanish on exit
        
        '''

        ## Keeps list limited in size.
        self.node_checkin_logs = self.node_checkin_logs[-15:] 
        self.node_file_access_logs = self.node_file_access_logs[-30:]

    def filehost_subroutine(self):
        '''
        Does stuff on time based triggers. 
        '''
        self.logger.info(f"{self.logging_info_symbol} Starting {Info.name} subroutine")
        ## Calc dir data
        # call filehost_api_file_listing
        ## >> rename: filehost_calculate_current_hosted_files

        while True:
            self.logger.debug(f"{self.logging_debug_symbol} Filehost Subroutine(s) triggering...")
            ## Calcing hosted files
            self.current_hosted_files = self.filehost_calculate_current_hosted_files()

            ## calcing file access logs
            self.current_file_access_logs = self.filehost_calculate_file_access_logs()


            ## Finally, end on a data cleanup
            self.filehost_data_management()
            ## Refresh time
            time.sleep(SUBROUTINE_REFRESH_TIME)

    ## doesnt belong here, move to a util class eventually
    def md5_hash_file(self, file_path):
        '''
        Does an md5 on a file and returns the hash.
        
        '''

        try:
            md5_hash = hashlib.md5()
            
            with open(file_path, 'rb') as file:
                while chunk := file.read(8192):
                    md5_hash.update(chunk)

            # Get the MD5 hash in hexadecimal format
            remote_md5_hex = md5_hash.hexdigest()
            return remote_md5_hex
        except Exception as e: 
            self.logger.warning(f"{self.logging_warning_symbol} Error with getting file hash: {e}")


