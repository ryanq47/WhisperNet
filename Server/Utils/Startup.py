import random


class StartupBanner:
    """
        A class for startup banner items
    """
    @staticmethod
    def startup_banner(ip = None, port = None, version = None):
        #version = "version"
        #ip = "127.0.0.1"
        #port = 5000

        demonsay_list = [
            "~~~shh... blueteam is watching~~~",
            "0x41414141414141414141...",
            "There is no right or wrong, only fun and boring",
            "No place like 127.0.0.1",
            "For legal reasons, this software does not exist"
        ]

        demonsay = random.choice(demonsay_list)

        a = f"""
    __      __.__    .__                             _______          __      _________                                
    /  \    /  \  |__ |__| ____________   ___________ \      \   _____/  |_   /   _____/ ______________  __ ___________ 
    \   \/\/   /  |  \|  |/  ___/\____ \_/ __ \_  __ \/   |   \_/ __ \   __\  \_____  \_/ __ \_  __ \  \/ // __ \_  __ \\
     \        /|   Y  \  |\___ \ |  |_> >  ___/|  | \/    |    \  ___/|  |    /        \  ___/|  | \/\   /\  ___/|  | \/
      \__/\  / |___|  /__/____  >|   __/ \___  >__|  \____|__  /\___  >__|   /_______  /\___  >__|    \_/  \___  >__|   
        \/       \/        \/ |__|        \/              \/     \/               \/     \/                 \/    

    =================================================================================================================
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        V: {version} -- github.com/ryanq47/whispernet
        Author: Ryanq.47                                         |_|      {demonsay}
                                                                ('.') ///   
                                                                <(_)`-/'    
                                                            <-._/J L /  -bf-
        IP: {ip} Port: {port}
        WebInt: http://{ip}:{port}/
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    =================================================================================================================

    """
        
        return a

    @staticmethod
    def successful_startup_banner(ip = None, port = None):
        '''
        Prints if the server successfuly starts. Using global ip & port vars. 
        Yes it's bad. I know
        '''
        banner = f"""
    ===============================================
    Server has successfuly started on: {ip}:{port}
    ===============================================
    """
        print(banner)
