
try:
    from getpass import getpass

except Exception as e:
    print(f"[client.Utils.CredenialHandler] Import Error: {e}")
    exit()

class Credentials:
    @staticmethod
    def get_password():
        password = getpass("Enter Password: ")
        return password

    @staticmethod
    def get_username():
        '''Doesn't need to exist, but makes the client.py a bit more readable
        '''
        username = input("Enter Username: ")
        return username
    
    @staticmethod
    def authenticate_to_server():
        cookie = None
        user = Credentials.get_username()
        passwd = Credentials.get_password()

        ## send logni request to server...

        ## get cookie... mmmm cookie monster delish
        if not cookie:
            ## NO COOKIE?
            print("Authentication Failed")
            Credentials.authenticate_to_server()

        return cookie

class Server:
    @staticmethod
    def get_server_to_connect_to():
        '''Prompt user for the server IP & Port to connect to. Returns that data as a Tuple
        
        '''
        server = input("Enter Server & port. Ex 127.0.0.1:5000: ")
        try:
            ip = server.split(":")[0]
            port = server.split(":")[1]

            server = [ip, port]
            return server

        except Exception as e:
            print(f"Invalid input: {e}")
            Server.get_server_to_connect_to()