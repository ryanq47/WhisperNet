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
        self.fail_color = "red"

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
        Implementation of spawning the server
        '''
        print(colored(f"Spawning server at: {self.c_ip}:{self.c_port}", self.color))
        server_path = os.path.join(sys_path, "../Server/server.py")

        try:
            os.system(f"python3 {server_path} --ip {self.c_ip} --port {self.c_port}")
        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

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
                print(colored("[*] Server login successful", self.color))
                print("Response Len:",  len(r.text))
            else:
                print(colored(f"request failed with status code {r.status_code} \n {r.text}", self.fail_color))

        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

    ## Server Upcheck
    def control_server_upcheck(self) -> bool:
        '''
        Checks if server is up. Returns True if up, false if not
        '''
        print("-> Checking if the control server is up...")
        try:
            r = requests.get(
                url = f"http://{self.c_ip}:{self.c_port}/"
            )

            if self.oops_check(request=r):
                print("[*] Server is up")
                print("Response Len:", len(r.text))
                return True

        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))
            return False

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
                    self.local_listener_upcheck(ip = "127.0.0.1", port = port)
                else:
                    print(colored(f"POST request failed with status code {r.status_code}", self.fail_color))
        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

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
                print(colored(f"[*] Listener is up @ {ip}:{port}", self.color))
        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

    def oops_check(self, request):
        '''
        Checks if error message is hit. Returns false if error is hit, true if error is not hit
        '''
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
    time.sleep(2) ## allows server to get a chance to start. very hacky

    while not test.control_server_upcheck():
        print(colored(f"Waiting for server to come online...", 'blue'))

    test.control_server_login()
    test.control_server_spawn_local_listener(port_list=["8080","9090","7070"])
