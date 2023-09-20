import requests
import time
import threading
import os
from colorama import init
from termcolor import colored
import atexit
import subprocess

sys_path = os.path.dirname(os.path.realpath(__file__))

class CodeTest:
    def __init__(self, c_port, c_ip):
        '''
        Initialize the CodeTest object.

        Args:
            c_port (int): The port for the control server.
            c_ip (str): The IP address for the control server.
        '''
        self.c_port = c_port
        self.c_ip = c_ip
        self.authorization_header = ""
        self.color = "green"
        self.fail_color = "yellow"
        self.arrow_color = "cyan"

    def startup(self):
        '''
        Print startup information.
        '''
        s = f"""
        Color Codes:
        {self.color}\t Successful Steps
        {self.fail_color}\t Failed Steps
        {self.arrow_color}\t Actions being taken

        Note, this script is far from perfect. It's meant to be a quick "what broke" code check.

        Quick Fixes:
            OS Error (process already on port):
                ps -fA | grep python
                sudo kill -9 <PID>
        """
        print(s)

    def spawn_control_server_thread(self):
        '''
        Spawns the control server in a thread with daemon mode.
        '''
        print(colored(f"{self.arrow('Spawning server thread')}: {self.c_ip}:{self.c_port}", self.arrow_color))

        t = threading.Thread(target=self._spawn_control_server)
        t.daemon = True
        t.start()
        atexit.register(self.exit_handler)

    def _spawn_control_server(self):
        '''
        Implementation of spawning the server.
        '''
        print(colored(f"{self.arrow('Spawning server at')}: {self.c_ip}:{self.c_port}", self.arrow_color))
        server_path = os.path.join(sys_path, "../Server/server.py")

        try:
            self.server_process = subprocess.Popen([
                "python3",
                server_path,
                "--ip", self.c_ip,
                "--port", str(self.c_port)
            ])
        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

    def control_server_login(self):
        '''
        Logs into the control server. Sets the self.authorization_header.
        '''
        print(colored(f"{self.arrow('Logging into the control server')}...", self.arrow_color))
        try:
            endpoint = f"http://{self.c_ip}:{self.c_port}/login"

            data = {
                "username": "admin",
                "password": "1234",
            }

            r = requests.post(
                url=endpoint,
                json=data
            )

            if self.oops_check(request=r):
                print(colored("[*] Server login successful", self.color))
                print("Response Len:", len(r.text))
                self.authorization_header = r.json()["access_token"]
            else:
                print(colored(f"Request failed with status code {r.status_code} \n {r.text}", self.fail_color))

        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

    def control_server_upcheck(self) -> bool:
        '''
        Checks if the control server is up. Returns True if up, False if not.
        '''
        print(colored(f"{self.arrow('Checking if the control server is up')}...", self.arrow_color))
        try:
            r = requests.get(
                url=f"http://{self.c_ip}:{self.c_port}/"
            )

            if self.oops_check(request=r):
                print(colored("[*] Server is up", self.color))
                print("Response Len:", len(r.text))
                return True

        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))
            return False

    def control_server_spawn_local_listener(self, port_list=[]):
        '''
        Spawns local listeners on specified ports FROM the control server
        '''
        try:
            for i in port_list:
                endpoint = f"http://{self.c_ip}:{self.c_port}/list"

                print(colored(f"{self.arrow('Attempting to spawn local listener on')} {i}...", self.arrow_color))
                print(colored(f"{self.arrow('Length of header token: ')} {len(self.authorization_header)} ", self.arrow_color))

                ip = "0.0.0.0"
                port = str(i)

                data = {
                    "ip": ip,
                    "port": port
                }

                headers = {
                    "Authorization": f"Bearer {self.authorization_header}"
                }

                r = requests.post(
                    url=endpoint,
                    json=data,
                    headers=headers
                )

                if self.oops_check(request=r):
                    print("[*] Local Listener spawned successfully")
                    self.local_listener_upcheck(ip="127.0.0.1", port=port)
                else:
                    print(colored(f"POST request failed with status code {r.status_code}", self.fail_color))
                    print(colored(f"Error (from err cookie): {r.cookies.get('err')}", self.fail_color))

        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

    def docker_spawn_listener(self):
        '''
            A representation of what an independent listener would look like.

            THis function builds a docker container for the listener, and deploys it
        '''
        try:
            dockerfile_path = os.path.join(sys_path, "../Listeners/FlaskAPI/")

            self.server_process = subprocess.Popen([
                "sudo", "docker", "build", dockerfile_path
            ])
        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))


    def local_listener_upcheck(self, ip=None, port=None):
        '''
        Checks if a local listener is up.
        '''
        print(f"[*] Checking if spawned listener is up...")

        time.sleep(1)  # Gives a second for things to get set up...

        try:
            r = requests.get(
                url=f"http://{ip}:{port}/stats"
            )

            if self.oops_check(request=r):
                print(colored(f"[*] Listener is up @ {ip}:{port}", self.color))
        except Exception as e:
            print(colored(f"[!] Error : {e}", self.fail_color))

    def oops_check(self, request):
        '''
        Checks if the error message is hit. Returns False if error is hit, True if error is not hit.
        '''
        if "Oops, Something Went Wrong" in request.text:
            return False
        else:
            return True

    def arrow(self, text):
        return f"-> {text}"

    def exit_handler(self):
        '''
        Exit handler function to kill the server process, and the subsequent listeners. This prevents the OS error.
        '''
        if hasattr(self, 'server_process') and self.server_process:
            print(colored("Terminating the server process...", self.arrow_color))
            self.server_process.terminate()
            self.server_process.wait()
            print(colored("Server process terminated.", self.arrow_color))

if __name__ == "__main__":
    test = CodeTest(
        c_port=5000,
        c_ip="0.0.0.0"
    )

    test.startup()

    test.spawn_control_server_thread()
    time.sleep(2)  # Allows the server to get a chance to start. Very hacky

    ## incase the server is being super slow, wait until it's up
    while not test.control_server_upcheck():
        print(colored(f"Waiting for server to come online...", 'blue'))

    test.control_server_login()
    test.control_server_spawn_local_listener(port_list=["8080", "9090", "7070"])
    test.docker_spawn_listener()

    input("Hit any key to exit & shutdown the server....")
