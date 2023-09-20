import requests
import time
import threading
import os
from colorama import init
from termcolor import colored


sys_path = os.path.dirname(os.path.realpath(__file__))


class CodeTest:
    '''
    A unit test/code test app for testing the suite
    '''
    def __init__(self, c_port, c_ip):
        self.c_port = c_port
        self.c_ip = c_ip
        self.authorization_header = None
        self.color = "green"

    def spawn_control_server_thread(self):
        '''
        Spawns server, in a thread in daemon mode
        '''
        print(colored(f"Spawning server thread: {self.c_ip}:{self.c_port}", self.color))

        t = threading.Thread(
            target = self._spawn_control_server,
        )
        t.setDaemon(True)
        t.start()

    def _spawn_control_server(self):
        '''
        Implementation of spawnign the server
        '''
        print(f"Spawning server at: {self.c_ip}:{self.c_port}")
        server_path = os.path.join(sys_path, "../Server/server.py")

        os.system(f"python3 {server_path} --ip {self.c_ip} --port {self.c_port}")

    def control_server_login(self):
        '''
        Logs into the control server. Sets the self.authorization_header
        '''
        print("-> logging into the control server...")
        try:
            endpoint = f"http://{self.c_ip}:{self.c_port}/login"

            data = {
                "username":"admin",
                "password":"1234",
            }

            r = requests.post(
                url = endpoint,
                json = data
            )

            if self.oops_check(request=r):
                print("[*] Server login successful")
                print("Response Len:",  len(r.text))
            else:
                print(f"request failed with status code {r.status_code} \n {r.text}")

        except Exception as e:
            print(f"[!] Error : {e}")

## Server Upcheck
    def control_server_upcheck(self):
        print("-> Checking if the control server is up...")

        try:
            r = requests.get(
                url = f"http://{self.c_ip}:{self.c_port}/"
            )

            if self.oops_check(request=r):
                print("[*] Server is up")
                print("Response Len:", len(r.text))
        except Exception as e:
            print(f"[!] Error : {e}")

    def control_server_spawn_local_listener(self, port_list = []):
        try:
            for i in port_list:
                endpoint = f"http://{self.c_ip}:{self.c_port}/list"

                print(f"-> Attempting to spawn local listener on {i}...")

                ip = "0.0.0.0"
                port = str(i)

                data = {
                    "ip": ip,
                    "port": port
                }

                headers = {
                    "Authorization":self.authorization_header
                }

                r = requests.post(
                    url = endpoint,
                    json = data,
                    headers=headers
                )

                if self.oops_check(request=r):
                    print("[*] Local Listener spawned successfully")
                    #print("Response Len:",  len(r.text))
                    self.local_listener_upcheck(ip = "127.0.0.1", port = port)
                else:
                    print(f"POST request failed with status code {r.status_code}")  
        except Exception as e:
            print(f"[!] Error : {e}")

    def local_listener_upcheck(self, ip = None, port = None):
        '''
        Checks if a local listener is up
        '''
        print(f"[*] Checking if spawned listener is up...")

        ## Gives a second for things to get set up...
        time.sleep(1)

        try:
            r = requests.get(
                url = f"http://{ip}:{port}/stats"
            )

            if self.oops_check(request=r):
                print(f"[*] Listener is up @ {ip}:{port}")
                #print("Response Len:", len(r.text))
        except Exception as e:
            print(f"[!] Error : {e}")


    def oops_check(self, request):
        if "Oops, Something Went Wrong" in request.text:
            return False
        
        else:
            return True


if __name__ == "__main__":
    test = CodeTest(
        c_port = 5000,
        c_ip = "127.0.0.1"
        )
    
    test.spawn_control_server_thread()
    test.control_server_upcheck()
    test.control_server_login()
    test.control_server_spawn_local_listener(port_list=["8080","9090","7070"])