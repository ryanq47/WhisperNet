## Notes, everything in here must be bulletproof. lots of redundancy & try/excepts for that reason. Not trying to be windows lol :)
'''
Handles all security checks

All methods return a true or a false.
    True: A-Ok and action is allowed
    False: No-Go, action not allowed

'''



class ClientSecurityCheck:
    pass

    @staticmethod
    def validate_ip():
        pass
        '''

        ## using YAML settings to bypass sec checks
        if yaml_obj["clientsec"]["Validate_ip"] == False:
            return True
        
        if rqeuester_ip == prior_client_valid_ip:
            return True

        else:
            return False    
        
        '''