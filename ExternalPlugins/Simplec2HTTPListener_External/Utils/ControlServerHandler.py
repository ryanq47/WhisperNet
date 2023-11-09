import requests
import json
import os
from Utils.LoggingBaseClass import BaseLogging
import hashlib

class ControlServerHandlerFileSync(BaseLogging):

    def __init__(self, jwt, server_url, server_port):
        BaseLogging.__init__(self)

        self.jwt        = jwt
        self.server_url = server_url
        self.server_port= server_port


    def sync_files(self):
        '''
        Sync's files with the control server. 
        

        Messy ATM
        '''
        self.logger.info(f"{self.logging_info_symbol} Starting Sync....")

        #self.logger.debug(f"Filename; {filename}")

        ## Request files from server
        ## save to Files/

        ## Send msg back to control server on success/fail

        ## Where to store files locally
        # Send an HTTP GET request to the base URL

        ## substitue for now
        base_url = "http://127.0.0.1:5000/"
        ## A list of all files, locked behind API auth
        api_file_url = "http://127.0.0.1:5000/api/filehost/files"

        headers = {
            "Authorization": f"Bearer {self.jwt}"
        }

        try:

            response = requests.get(
                url = api_file_url,
                headers = headers
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the response content as HTML or any other format if needed
                # For example, if the server returns an HTML page with links to files, you can use a library like BeautifulSoup to parse it.
                # Then, extract the file URLs and iterate through them to download the files.
                self.sync_files_action(response, headers)
            else:
                self.logger.warning(f"Failed to retrieve files from {base_url}, code: {response.status_code}")
                #print(response.text)


        except Exception as e:
            self.logger.warning(f"{self.logging_warning_symbol} Unable to connect to Control Server: {e}")


    def sync_files_action(self, response, headers):
        ''' Ex Json data
            {
                "myfile00.txt": {
                    "filedir": "/filehost/myfile00.txt",
                    "filename": "myfile00.txt",
                    "filesize": 28
                },
        '''
        local_directory = "Files/"

        file_urls_dict = json.loads(response.text)
            # Create the local directory if it doesn't exist
        os.makedirs(local_directory, exist_ok=True)

            # Download each file
        for file_url in file_urls_dict:
            chunk_size          = 1024
            filesize            = file_urls_dict[file_url]["filesize"]
            filename            = file_urls_dict[file_url]["filename"]
            filepath_on_server  = file_urls_dict[file_url]["filedir"]
            filehash            = file_urls_dict[file_url]["filehash"]
            #filehash = ""

            self.logger.info(f"{self.logging_info_symbol} Downloading {filename} from {file_url} to {filepath_on_server}")

                #filename = os.path.basename(file_url)
            local_file_path = os.path.join(local_directory, filename)


            ## Need to check if file EXISTS here first... can't compare a file that doesnt exist lol
            if os.path.exists(local_file_path):

                ## Need to do hash checking. IF hashes are the same, DO NOT
                ## redownload. Saves on processing & Network bandwidth
                if self.file_compare(local_file = local_file_path, remote_file_hash = filehash, remote_file_name=filepath_on_server):
                    self.logger.info(f"{self.logging_info_symbol} Exact copy of {filename} already exists. Skipping download.")
                    continue

            else:
                # Send an HTTP GET request to the file URL and save the content to a local file
                with open(local_file_path, 'wb') as local_file:
                    server_response = requests.get(
                        url=f"http://127.0.0.1:5000/filehost/{filename}",
                        headers=headers,                        
                        stream=True  # Set stream=True to enable streaming the content
                    )

                    if server_response.status_code == 200:
                        for chunk in server_response.iter_content(chunk_size=chunk_size):
                            if chunk:
                                local_file.write(chunk)

                        ## Additional file checks, hash checking for file integrity?
                    else:
                        self.logger.warning(f"{self.logging_warning_symbol} Failed to download {file_url}: {server_response.status_code}")

    def file_compare(self, local_file, remote_file_hash, remote_file_name) -> bool:
        ''' 
        Compares files from local, to what is on the server. Won't redownload if they are the same.

        if they are the same, returns true, else returns false.
        
        '''
        md5_hash = hashlib.md5()

        self.logger.debug(f"{self.logging_debug_symbol} Comparing local file: {local_file} and remote file: {remote_file_name}")
        # Open the file in binary mode and read it in chunks
        with open(local_file, 'rb') as file:
            while chunk := file.read(8192):
                md5_hash.update(chunk)

        # Get the MD5 hash in hexadecimal format
        remote_md5_hex = md5_hash.hexdigest()

        #print("MD5 Hash:", remote_md5_hex)
        self.logger.debug(f"{self.logging_debug_symbol} Hash of {local_file}:{remote_md5_hex}\nHash of {remote_file_name}:{remote_file_hash}")


        if remote_md5_hex == remote_file_hash:
            return True

        ## Files not the same
        else:
            self.logger.info(f"{self.logging_info_symbol} {local_file} and {remote_file_name} are not the same. Proceeding to redownload")
            return False
