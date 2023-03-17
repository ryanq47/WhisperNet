import socket

global_debug = True


class fclient():

    def __init__(self):
        self.encoding = 'utf-8'
        
    
    def connect_to_server(self):
        print('Connecting to server') if global_debug else None
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        self.ip, self.port = "127.0.0.1", 100
        
        self.server_addr = (self.ip, self.port)
        self.server.connect(self.server_addr)
        
        creds = self.credential_gather()
        
        print(f"!_user_!\\|/{creds[0]}\\|/{creds[1]}") if global_debug else None
        
        self.server.send(self.str_encode(f"!_user_!\\|/{creds[0]}//|\\\\{creds[1]}"))
        print("Connected!")
        self.server_interact()
    
    def credential_gather(self) -> list:
        ## HA yes this works! init the list with types!
        creds_list = [str, str]
        
        creds_list[0] = input("Username: ")
        creds_list[1] = input("Password: ")
    
        return creds_list
    
    def server_interact(self):
        while True:
            user_input = input(f"{self.ip}:{self.port}$: ")
            self.server.send(self.str_encode(user_input))
            print(self.str_decode(self.server.recv))

    
    ## Doing dedicated encode/decode casuse syntax is easier & cleaner
    
    ## bytes -> str
    def str_decode(self, input) -> str:
        decoded_result = input.decode()
        return decoded_result

    ## str -> bytes
    def str_encode(self, input) -> bytes:
        encoded_result = input.encode()
        return encoded_result


if __name__ == "__main__":
    fc = fclient()
    
    fc.connect_to_server()