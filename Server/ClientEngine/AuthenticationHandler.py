## Notes, everything in here must be bulletproof. lots of redundancy & try/excepts for that reason
import random
import Utils.UtilsHandler

class Authentication:
    
    ## OLD
    @staticmethod
    def password_eval(password = None, server_password = None) -> bool:
        """
        The password eval function. returns true if successful. Will be encrypted when I get around to that

        password (str): the password given by the client
        """
        try:
            ## decrypt pass
            _password = str(password)
            if _password == None:
                #move to logging eventually
                #logging.debug("[Server (password_eval)] Password with value of 'None' passed to the password eval function")
                print("[Server (password_eval)] Password with value of 'None' passed to the password eval function")
        
            ## the else covers my ass for any potential injection/rifraff with the None parameter
            else:
                if _password == server_password:
                    return True
                else:
                    return False
        except Exception as e:
            print(f"[Server (password_eval)] Error: {e}")
            return False
        
    @staticmethod
    def generate_random_cookie():
        ## temp hardcode
        client_profile = Utils.UtilsHandler.yaml_load(yaml_file=r"C:\Users\Ryan\Documents\GitHub\logec-suite\Server\Config\ClientProfiles\default.yaml")

        char_string = client_profile["Authentication"]["Cookies"]["Characters"]
        min_length  = client_profile["Authentication"]["Cookies"]["MinLength"]
        max_length  = client_profile["Authentication"]["Cookies"]["MaxLength"]

        random_cookie = ''.join(random.SystemRandom().choice(char_string) for _ in range(min_length, max_length))
        return random_cookie
    
    @staticmethod
    def validate_password(password):
        client_profile = Utils.UtilsHandler.yaml_load(yaml_file=r"C:\Users\Ryan\Documents\GitHub\logec-suite\Server\Config\ClientProfiles\default.yaml")
        '''
        Load password from somewhere

        if server_password == password:
            return True

        else:
            return False
        
        
        '''
        server_password = client_profile["Authentication"]["Server"]["Password"]

        ## need validation that the server_passwrod is actually someting

        if server_password == password:
            return True
        else:
            return False



print(Authentication.generate_random_cookie())