"""
New Reddit Osint

Mapping:

Gui -> RedditOsint Class

## pass creds here
__init__(credentials_list)
    self.creds etc

pass search lsit here
reddit_framework(self, search_list:list)
    Oauth
    Search
    Parse

return results to GUI & writeto DB from there


"""
import requests
import logging
import random
from PySide6.QtCore import QThread, Signal, QObject, Slot

global_debug = True
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='osint_reddit.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', force=True)
#if global_debug:
logging.getLogger().addHandler(logging.StreamHandler())


class OsintReddit:
    #True if authenticated
    authenticated = Signal(bool)

    def  __init__(self, credentials_list):
        self.username, self.password, self.secret_token, self.client_id = credentials_list
        self.authenticated = False

    def oauth(self):
        """
        This function is used for getting an auth token from the reddit
        API
        """
        logging.debug(f"[Credentials] {self.credentials_list}")
        ## Note, add optional set user agent in GUI options. Pass in via a list or something
        self.user_agent = self.user_agent_generator()

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_token)
        data = {'grant_type': 'password',
                'username': self.username,
                'password': self.password}
        headers = {'User-Agent': self.user_agent}

        try:
            api_response = requests.post('https://www.reddit.com/api/v1/access_token',
            auth=auth, data=data, headers=headers)
        
        ## Need to except connection error  speficially
        except Exception as e:
            logging.debug(f"{e}")
        
        try:
            self.token = api_response.json()['access_token']
            self.authenticated_header = {**headers, **{'Authorization': f"bearer {self.token}"}}
            self.authenticated = True
            self.authenticated.emit()
        except Exception as e:
            logging.debug(f"Error with authentication: {e}")
            self.authenticated = False


    def osint_reddit_framework(self, search_list):
        """
        This is the "main" function, with an input from the GUI (searchlist)

        It calls all the neccesary functions for a successful request, and 
        then emits them to the GUI

        search list comprises of: (* is required)
            search term
            subreddit
            popularity
            time
            profile


        """

        ## mayneed to rethink return vs raise vs self.auth vs emit here
        if not self.authenticated:
            self.oauth()

        ## url building (takes search_list, returns url)

        ## senning request (takes url, returns request results)

        ## parsing request (takes request results, returns parsed results)

        ## emit results back so they can be written to the DB - 
        ##  May need to think through as the loop is usually a for loop, 
        ## so maybe emit one line, write (or append) said line, and return the next line and 
        ## so on? 

    def url_legos():
        """
        Takes items from list, sets values for url pieces. Called legos cause it's creating little "lego" pieces 
        to build with
        """
        pass
    
    def url_build():
        """
        Builds the URL with the previously created legos
        """
        pass
    

    def user_agent_generator() -> str:
        ## Some random names, you can customize to whatever you want
        agent = ["RedditBot", "SuperMan", "TMNT", "RareDonkey"]
        version_number = random.randomint(1,99)
        
        name = f"{random.choice(agent)} v{version_number}"
        ## Returning name instead of self.name so self.name never is nothing
        return name
        