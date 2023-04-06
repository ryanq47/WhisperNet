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
    authenticated = Signal()

    def  __init__(self, credentials_list):
        self.username = credentials_list['username']
        self.password = credentials_list['password']
        self.secret_token = credentials_list['secret_token']
        self.client_id = credentials_list['client_id']
        self.authenticated = False

    def oauth(self):
        """
        This function is used for getting an auth token from the reddit
        API
        """
        logging.debug(f"[Credentials] User: {self.username}, Pass: {self.password}, Token: {self.secret_token}, ID: {self.client_id}")
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
            logging.debug(f"[Reddit-API] {api_response}")
            ## err looks liek:
            ##{"error_description": "Only script apps may use password auth", "error": "unauthorized_client"}
            
            if "error" in api_response:
                logging.debug("Error with authentication: {api_response}")
                self.authenticated = False
                ## self.emit error
        
        ## Need to except connection error  speficially
        except Exception as e:
            logging.debug(f"Error with request to reddit API server: {e}")
            ## self.emit error
        try:
            #print(api_response.text)
            self.token = api_response.json()['access_token']
            print(self.token)
            self.authenticated_header = {**headers, **{'Authorization': f"bearer {self.token}"}}
            self.authenticated = True
            
            ##being funky with a bool error: Error: 'bool' object has no attribute 'emit'
            #self.authenticated.emit()
            
        except Exception as e:
            logging.debug(f"Error: {e}")
            self.authenticated = False


    def osint_reddit_framework(self, search_list, options_list):
        """
        This is the "main" function, with an input from the GUI (searchlist)

        It calls all the neccesary functions for a successful request, and 
        then emits them to the GUI

        search list comprises of: (* is required)
            List order: search_term, subreddit, time, sort, limit, username
        
        Options list comprises of:
            Options list: download_media, only_comments, only_profile, search_subbreddit
        
        Options are either a "True" or a "False"
        ## note change only_ categories to just comments, or profile. Makes it so 
        you can stack different searches on 


        """

        ## mayneed to rethink return vs raise vs self.auth vs emit here
        if not self.authenticated:
            self.oauth()

        ## Parsing list & assinging values to snap together in the URL
        self.url_legos(search_list)
        
        ## url building (returns url)
        url_request_list = self.url_build(options_list)
        
        ## senning request (takes url, returns request results)
        request_output = self.reddit_request(url_request_list)
        ## parsing request (takes request results, returns parsed results)
        print(request_output)
        ## emit results back so they can be written to the DB - 
        ##  May need to think through as the loop is usually a for loop, 
        ## so maybe emit one line, write (or append) said line, and return the next line and 
        ## so on? 

    def url_legos(self, search_list):
        ## List order: search_term, subreddit, time, sort, limit, username

        """
        Takes items from list, sets values for url pieces. Called legos cause it's creating little "lego" pieces 
        to build with
        
        If a value is not found, an warning is emmited, and then the search proceeds without that value included.
        """
        #pass
        self.search_term = search_list[0]
        self.subreddit = search_list[1]
        
        ## Time 
        
        try:
            filter_time_raw = search_list[2]
            self.filter_time = "&t=" + filter_time_raw.lower()
        except:
            self.filter_time = ""
            ## emit err
        
        ## sort    
        try:
            filter_sort_raw = search_list[3]
            self.filter_sort= "&sort=" + filter_sort_raw.lower()
        except:
            self.filter_sort=""
            ## emit err
        
        ## limit
        try:
            filter_limit_raw = search_list[4]
            self.filter_limit =  "&limit=" + filter_limit_raw
        except:
            self.filter_limit = ""
        
        
        logging.debug(f"""
            Search_Term: {self.search_term}, 
            Subreddit: {self.subreddit}, 
            Time {self.filter_time},
            Sort: {self.filter_sort} 
            limit: {self.filter_sort}
            """)
        
    def url_build(self, options_list) -> list:
        """
        Builds the URL with the previously created legos
        
        """
        built_url = []
        download_media, comments, profile, subreddit = options_list
        
        if subreddit:
            built_url.append("https://oauth.reddit.com/search/?q=" + self.search_term + self.filter_sort + self.filter_time + self.filter_limit)
        
        elif profile: ## profile search
            built_url.append("https://oauth.reddit.com/user/" + self.search_term + "/" + self.filter_sort.replace("&","?") + self.filter_time + self.filter_limit)

        else:
            pass
            
    
        return built_url
        #pass
    
    def reddit_request(self, url_request_list):
        ## for i in url's, search, and append to output list
        ## this way you can stack multiple searches
        request_output = []
        
        for url in url_request_list:
            try:
                req = requests.get(url, headers=self.authenticated_header)
                request_output.append(req.text)
            except Exception as e:
                logging.warning(f"Error with request to reddit:\n {e} \n{url}")
        return request_output
            
    
    ############
    #!!!! Upnext, build parser!!!!!!!#
    #########
    
    def reddit_response_parse(self):
        pass
    

    def user_agent_generator(self) -> str:
        ## Some random names, you can customize to whatever you want
        agent = ["RedditBot", "SuperMan", "TMNT", "RareDonkey"]
        version_number = random.randint(1,99)
        
        name = f"{random.choice(agent)} v{version_number}"
        ## Returning name instead of self.name so self.name never is nothing
        return name
        