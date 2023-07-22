## Notes, everything in here must be bulletproof. lots of redundancy & try/excepts for that reason


class Authentication:
    
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