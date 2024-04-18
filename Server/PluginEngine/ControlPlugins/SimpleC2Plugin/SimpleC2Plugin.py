from DataEngine.SimpleC2DbHandler import SimpleC2DbHandler

import os

''' Imports
Go ahead and define any other imports you may need here.

'''
import logging
import inspect
from flask import jsonify, send_from_directory, redirect, make_response
#from flask_login import LoginManager, login_required
import requests
import json

## API stuff
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from Utils.ApiHelper import api_response
from werkzeug.exceptions import BadRequest
from DataEngine.Neo4jHandler import Neo4jConnection
from Utils.Logger import LoggingSingleton
from PluginEngine.ControlPlugins.SimpleC2Plugin.Utils.ListenerHandler import HttpListenerHandler
from Utils.DataSingleton import Data
################################################
# Info class
################################################
'''Info class
Fill in your info for the plugin here. This is defined near the top, so it's accessible
by anything that may need it.

'''
class Info:
    name    = "SimpleC2"
    author  = "ryanq47"
    endpoint = "/simplec2"
    classname = "SimpleC2"
    plugin_type = "Builtin"
    #dashboard = True

## RoleCheck Decorator - move to BasePlugin after testing
def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            user_role = current_user.get('role') if current_user else None

            if user_role != required_role:
                return jsonify({"message": "Access denied"}), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator


## Inherets BasePlugin
## Is a class instance, the __init__ is from BasePlugin.
class SimpleC2():
    def __init__(self, app):
        self.logger = LoggingSingleton.get_logger()
        self.data = Data()
        self.app = app
        self.neo4j = None
        self.connect_to_neo4j()
        ## Data Structures
        self.node_checkin_logs = []



################################################
# Main Stuff
################################################

    def main(self):
        '''
        Main function/entry point for the plugin.
        '''
        self.logger.debug(f"{inspect.stack()[0][3]}")
        self.logger.debug(f"Loading {Info.name}")
        self.register_routes()

    ## Put all the routes here.
    def register_routes(self):
        self.logger.debug(f"{inspect.stack()[0][3]}")
        #self.app.route(f'/{Info.endpoint}', methods = ["GET"])(self.simplec2_dashboard)
        #self.app.route(f'/api/{Info.endpoint}/', methods=["GET"])(self.simplec2_api_placeholder)
        #self.app.route(f'/api/{Info.endpoint}/postcommand', methods = ["POST"])(self.simplec2_api_post_client_command)
        #self.app.route(f'/api/{Info.endpoint}/nodecheckin', methods = ["POST"])(self.simplec2_api_node_checkin)
        #self.app.route(f'/api/{Info.endpoint}/nodelogs', methods = ["GET"])(self.simplec2_api_get_checkin_logs)
        #self.app.route(f'/api/{Info.endpoint}/clientdata', methods = ["POST"])(self.simplec2_api_post_client_data)
        #self.app.route(f'/api/{Info.endpoint}/clients', methods = ["GET","POST"])(self.simplec2_api_client)
        #self.app.route(f'/api/{Info.endpoint}/console', methods = ["GET"])(self.simplec2_api_console)
        
        ## Network
        self.app.route(f'/api/{Info.endpoint}/network/add', methods = ["POST"])(self.neo4j_add_network)
        self.app.route(f'/api/{Info.endpoint}/network/remove', methods = ["POST"])(self.neo4j_remove_network)
        self.app.route(f'/api/{Info.endpoint}/network/properties', methods = ["POST"])(self.neo4j_get_network_properties)
        self.app.route(f'/api/{Info.endpoint}/network/addproperties', methods = ["POST"])(self.neo4j_add_network_properties)

        self.app.route(f'/api/{Info.endpoint}/network/clients', methods = ["POST"])(self.neo4j_retrieve_clients_in_network)
        self.app.route(f'/api/{Info.endpoint}/network/networks', methods = ["GET"])(self.neo4j_retrieve_all_networks)
        
        ## General
        self.app.route(f'/api/{Info.endpoint}/general/everything', methods = ["GET"])(self.neo4j_retrieve_everything)

        ## listeners
        self.app.route(f'/api/{Info.endpoint}/listener', methods = ["GET"])(self.listener_list)
        self.app.route(f'/api/{Info.endpoint}/listener/http/spawn', methods = ["POST"])(self.http_listener_spawn)
        self.app.route(f'/api/{Info.endpoint}/listener/http/kill', methods = ["POST"])(self.http_listener_kill)


        ## Client
        self.app.route(f'/api/{Info.endpoint}/client/add', methods = ["POST"])(self.neo4j_add_client)
        self.app.route(f'/api/{Info.endpoint}/client/remove', methods = ["POST"])(self.neo4j_remove_client)
        self.app.route(f'/api/{Info.endpoint}/client/properties', methods = ["POST"])(self.neo4j_get_client_properties)
        self.app.route(f'/api/{Info.endpoint}/client/addproperties', methods = ["POST"])(self.neo4j_add_client_properties)

    def connect_to_neo4j(self):
        '''
        Creates Neo4j connection
        
        '''
        ## Creating ONE connection for performance purposses, otherwise 
        ## it would take 2-3 seconds to create it, query, and return
        ## should stick this in a func to be more resiliant

        try:
            self.neo4j = Neo4jConnection()
        except Exception as e:
            self.logger.critical(f"Could not connect to Neo4j DB!: {e}")

################################################
# HTML Dashboard
################################################

    def simplec2_dashboard(self):
        '''
        Dashaboards. Cool eventually but not now
        
        '''

        return "dashboard"
    
    def simplec2_api_placeholder(self):
        '''
        api
        '''
        return "api"

################################################
# Listener Management- Gonna have to redo these
################################################


## General
    def listener_list(self):
        '''
            Lists all listeners in JSON form

            JSON:

            nickname {
                type: HTTP,
                nickname: nickname
                address: 0.0.0.0 #-> ext addr? - or list of addresses it's running on
                pub_address: pub_ip
                port: 9999
                #strt_time: unix_timestamp #(LATER)

            }


        '''

        try:
            listeners_dict = {}

            #2024-03-29 17:24:19 - [!] SimpleC2.listener_list - 'str' object has no attribute 'get' 
            # something wrong here. not sure what.

            # Get HTTP Listeners, add to dict
            http_listeners = self.data.Listeners.HTTP.get_listeners()

            for nickname in http_listeners:
                # once you have nickanes, get the data for each one
                http_listener = self.data.Listeners.HTTP.get_listener_by_nickname(nickname=nickname)
                # Use .get() for safer access
                info = http_listener.get("info", {})
                
                # Now safely attempt to get the 'nickname', 'bind_address', and 'bind_port' using .get()
                nickname = info.get("nickname")
                bind_address = info.get("bind_address", "Unknown address")  # Provide default value
                bind_port = info.get("bind_port", "Unknown port")  # Provide default value
                listener_type = info.get("type", "Unknown Type")  # Provide default value

                if nickname:  # Ensure nickname exists before adding to the dictionary
                    listeners_dict[nickname] = {
                        "bind_address": bind_address,
                        "bind_port": bind_port,
                        "type":listener_type
                    }

            # Assuming jsonify and api_response are correctly defined elsewhere
            #listeners_json = jsonify(listeners_dict)
            return api_response(status_code=200, data=listeners_dict)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            self.logger.warning(e)
            return api_response(status_code=500)

## HTTP Listener
    def http_listener_spawn(self):
        '''
            Spawn an HTTP listener
        '''

        try:
            listener_port = request.json.get('port')
            listener_address = request.json.get('address')
            listener_nickname = request.json.get('nickname')

            # class call
            HttpListenerHandler.spawn(bind_port = listener_port, bind_address = listener_address, nickname=listener_nickname)

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            self.logger.warning(e)
            return api_response(status_code=500)

    def http_listener_kill(self):
        '''
            Kill an HTTP listener (hard kill). POST request, recieves nickname for listener to kill
        '''

        try:
            nickname = request.json.get('nickname')

            # class call
            HttpListenerHandler.kill(nickname=nickname)

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            self.logger.warning(e)
            return api_response(status_code=500)


################################################
# API - Gonna have to redo these
################################################

    ## Endpoint for CLinet sending command
    ## Post, JSON   
    def simplec2_api_post_client_command(self):
        '''
        Endpoint for Client sending command. Gets magically parsed, and forwarded to the respective listener
        '''
        ...

        ## Parse json.

        ## Get listener.

        ## post to listener.
        return make_response("up", 200)
    
    def simplec2_post_command_to_listener(self, command = None, listener = None, target = None):
        '''
        Forwards the command onto the listener
        

        JSON:

        {
            command: command (powershell whoami)
            target: "target_ip/name of target, etc

        }


        '''

        ## Requests.send to listneer at post addr.
        ## 127.0.0.1:80/postaddr/post_commands

        ## on the listnere side, take post, parse it, queue it

        ...

    def simplec2_api_client(self):
        '''
        for the GUI to GET client data from the server
        
        or POST to the server for queuing commands N stuff

        WIll figure out the intraceuies later
        '''
        if request.method == 'GET':
            client_data = [
                {
                    "client": "WIN-0N3BY",
                    "ip": "192.168.93.214",
                    "port": "8233",
                    "listener": "Listener-HTTP-4",
                    "sleep": "31s",
                    "username": "Admin",
                    "client_type": "C++"
                },
                {
                    "client": "WIN-HFT63",
                    "ip": "192.168.214.109",
                    "port": "8182",
                    "listener": "Listener-HTTP-8",
                    "sleep": "58s",
                    "username": "User",
                    "client_type": "Python"
                },
                {
                    "client": "WIN-GUN75",
                    "ip": "192.168.96.93",
                    "port": "8870",
                    "listener": "Listener-HTTP-9",
                    "sleep": "36s",
                    "username": "Guest",
                    "client_type": "C++"
                },
                {
                    "client": "WIN-V5DYU",
                    "ip": "192.168.250.41",
                    "port": "8982",
                    "listener": "Listener-HTTP-3",
                    "sleep": "56s",
                    "username": "Admin",
                    "client_type": "Python"
                },
                {
                    "client": "WIN-5MXHF",
                    "ip": "192.168.100.114",
                    "port": "8133",
                    "listener": "Listener-HTTP-1",
                    "sleep": "14s",
                    "username": "Admin",
                    "client_type": "Python"
                },
                {
                    "client": "WIN-UV2PK",
                    "ip": "192.168.26.52",
                    "port": "8438",
                    "listener": "Listener-HTTP-5",
                    "sleep": "57s",
                    "username": "Admin",
                    "client_type": "Java"
                }
            ]

            return jsonify(client_data)

        elif request.method == "POST":
            '''
            This is meant to be used for queing command N stuff
            '''
            ## turn into a func eventually

            # Get data from request
            client_id = request.json.get('id')


            if client_id == "server":
                return "simplec2 console API is up"
                #something?
                ...

            else:
                ## Do actions, 

                ## Get Client Object (dunno how, gonna take somethinking)

                ## POST to respective Listnener, Queue command
                    ##/synccommand on listener
                response = self.queue_command_on_listener(
                    listener_url="http://127.0.0.1:5001/synccommand",
                    client_id=client_id
                )
                
                ## Get callbacktime/info from request. 

                ## put injson

                # return json with details for console/gui
                ## Directly returning json from node at the moment. 
                return response

                #return jsonify(fake_data)

################################################
# API - DB stuff
################################################
    def neo4j_add_network(self):
        '''
            Adds a network to the DB

            Request:
                {
                    "cidr":"10.0.0.0/24"
                }
        '''

        try:
            network_cidr = request.json.get('cidr')
            network_nickname = request.json.get('nickname')

            self.neo4j.add_network_node(
                cidr = network_cidr,
                nickname = network_nickname
            )

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    def neo4j_remove_network(self):
        '''
            Adds a network to the DB

            Request:
                {
                    "cidr":"10.0.0.0/24"
                }
        '''

        try:
            network_nickname = request.json.get('nickname')

            self.neo4j.remove_network_node(
                nickname = network_nickname
            )

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    def neo4j_get_network_properties(self):
        '''
            Gets properties of a netowrk Node

            Request:
                {
                    "nickname":"Subnet1"
                }
        '''

        try:
            network_nickname = request.json.get('nickname')

            #neo4j = Neo4jConnection()
            properties = self.neo4j.get_network_node_properties(
                nickname = network_nickname
            )

            print(properties)

            return api_response(
                status_code=200,
                data={}
                )

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)  

    def neo4j_add_network_properties(self):
        '''
        Adds properties to a network. 
        
        Request:
        {
            "nickname":"NetworkNickname3",
            "property":"cidr",
            "value":"10.0.0.0/24"

        }

        '''

        try:
            network_nickname = request.json.get('nickname')
            network_property = request.json.get('property')
            network_property_value = request.json.get('value')

            #neo4j = Neo4jConnection()
            properties = self.neo4j.add_or_update_network_node_property(
                nickname = network_nickname,
                property_name=network_property,
                value = network_property_value
            )

            print(properties)

            ## blank response, properties command failed. Reutrn a 400 bad request
            if properties == []:
                return api_response(status_code=400)
            

            return api_response(
                status_code=200,
                data={}
                )

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500) 

    def neo4j_add_client(self):
        '''
            Adds a client to the DB

            Request:
                {
                    "hostname":"DESKTOP-123ABC2"
                }
        '''

        try:
            #host_hostname = request.json.get('hostname')
            host_nickname = request.json.get('nickname')

            self.neo4j.add_client_node(
                nickname = host_nickname
            )

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    def neo4j_remove_client(self):
        '''
            Removes a client from the DB

            Request:
                {
                    "hostname":"DESKTOP-123ABC2"
                }
        '''

        try:
            host_nickname = request.json.get('nickname')

            self.neo4j.remove_client_node(
                nickname = host_nickname
            )

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    def neo4j_add_client_properties(self):
        '''
        Adds properties to a network. 
        
        Request:
        {
            "nickname":"NetworkNickname3",
            "property":"cidr",
            "value":"10.0.0.0/24"

        }

        '''

        try:
            client_nickname = request.json.get('nickname')
            client_property = request.json.get('property')
            client_property_value = request.json.get('value')

            #neo4j = Neo4jConnection()
            properties = self.neo4j.add_or_update_client_node_property(
                nickname = client_nickname,
                property_name=client_property,
                value = client_property_value
            )

            print(properties)

            ## blank response, properties command failed. Reutrn a 400 bad request
            if properties == []:
                return api_response(status_code=400)
            

            return api_response(
                status_code=200,
                data={}
                )

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500) 

    def neo4j_get_client_properties(self):
        '''
            Gets properties of a client Node

            Request:
                {
                    "nickname":"Dc01-org01"
                }
        '''

        try:
            network_nickname = request.json.get('nickname')

            #neo4j = Neo4jConnection()
            properties = self.neo4j.get_client_node_properties(
                nickname = network_nickname
            )

            print(properties)

            return api_response(
                status_code=200,
                data={}
                )

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500) 

    def neo4j_retrieve_clients_in_network(self):
        '''
        Retrieves clients under a given network 
        '''


        try:
            #host_hostname = request.json.get('cidr')
            network_nickname = request.json.get('nickname')

            self.neo4j.retrieve_clients_in_network(
                nickname = network_nickname
            )

            return api_response(status_code=200)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    def neo4j_retrieve_all_networks(self):
        '''
        Gets all networks in the neo4j db
        '''
        try:
            #host_hostname = request.json.get('cidr')

            all_networks = self.neo4j.get_network_nodes(
                #no args
            )

            return api_response(status_code=200, data=all_networks)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)

    def neo4j_retrieve_everything(self):
        '''
        Gets everything in the Neo4j db. 
        '''
        try:
            #host_hostname = request.json.get('cidr')

            everything = self.neo4j.get_everything()

            return api_response(status_code=200, data=everything)

        except BadRequest:
            return api_response(status_code=400)
        except Exception as e:
            return api_response(status_code=500)
