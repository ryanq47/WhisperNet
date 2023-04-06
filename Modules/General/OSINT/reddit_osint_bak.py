import sqlite3
import os.path
import requests
import datetime

import pyshorteners


####################
## Credentials
####################
'''
## Loading creds on startup, need to pull from DB
load_creds = open("config/credentials.json")

creds = json.load(load_creds)

## Reddit Login Info
SECRET_TOKEN = creds['SECRET_TOKEN']
CLIENT_ID= creds['CLIENT_ID']

REDDIT_USERNAME = creds['REDDIT_USERNAME']
REDDIT_PASSWORD = creds['REDDIT_PASSWORD']'''

USER_AGENT = "Beta Bot 0.1.1"
##############################
class reddit:
    
    def __init__(self):
        self.total_posts = 0
        self.current_post = 0
    
    ## This gets called directly from logec-attack.py
    def main(self, search_list, options_list):
        self.creds_tuple = database_read_creds()
        self.OAuth()
        
        self.search_list = search_list
        self.url_filter()
        
        self.options_list = options_list
        self.search_logic()
        
        

    ####################
    ## Authentication
    ####################

    def OAuth(self):
        print(self.creds_tuple)
        REDDIT_USERNAME = self.creds_tuple[0]
        REDDIT_PASSWORD = self.creds_tuple[1]
        SECRET_TOKEN = self.creds_tuple[2]
        CLIENT_ID = self.creds_tuple[3]

        ##OAuth Login
        # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

        # here we pass our login method (password), username, and password
        data = {'grant_type': 'password',
                'username': REDDIT_USERNAME,
                'password': REDDIT_PASSWORD}

        # setup our header info, which gives reddit a brief description of our app
        headers = {'User-Agent': USER_AGENT}


        # send our request for an OAuth token
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)
        #print Oauth, for debugging
        #print(res.text + "\n")

        TOKEN = res.json()['access_token']

        # add authorization to our headers dictionary
        self.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        #search()


    def url_filter(self):
        ## List order: search_term, subreddit, time, sort, limit, username
        
        self.search_term = self.search_list[0]
        self.subreddit= self.search_list[1]
        #self.user= self.searchlist[5]
        
        filter_time_raw = self.search_list[2]
        try:
            self.filter_time = "&t=" + filter_time_raw.lower()
        except:
            self.filter_time = ""

        filter_sort_raw = self.search_list[3]
        try:
            self.filter_sort= "&sort=" + filter_sort_raw.lower()
        except:
            self.filter_sort=""

        filter_limit_raw = self.search_list[4]
        try:
            self.filter_limit =  "&limit=" + filter_limit_raw
        except:
            self.filter_limit = ""
            

    
    def search_logic(self):
        ## Options list: download_media, only_comments, only_profile, search_subbreddit
        ## 
        
        ## if appened != checked or true or whatever:
        table_wipe()
        
            ## -- ALl of reddit search -- ##
        if self.options_list[2]: ## profile
            print("ONLY COMMENTS")
            #print("DEBUG: args.u")
            res = requests.get("https://oauth.reddit.com/user/" + self.search_term + "/" + self.filter_sort.replace("&","?") + self.filter_time + self.filter_limit,
                headers=self.headers)
            
            print("https://oauth.reddit.com/user/" + self.search_term + "/" + self.filter_sort.replace("&","?") + self.filter_time + self.filter_limit)
            
            #error_handle(res)
            self.search_process(res)

        elif self.options_list[1]: ## comment
            print("DEBUG: args.c")
            res = requests.get("https://oauth.reddit.com/search/?q=" + self.search_term + self.filter_sort + self.filter_time + self.filter_limit + "&type=comment",
                headers=self.headers)
            
            print("https://oauth.reddit.com/search/?q=" + self.search_term + self.filter_sort + self.filter_time + self.filter_limit + "&type=comment")
            #error_handle(res)
            self.search_process(res)

        elif self.options_list[3]:  
            print("SUBRED SEARCH")
            res = requests.get("https://oauth.reddit.com/r/" + self.subreddit + "/search/?q=" + self.search_term + "&restrict_sr=on" + self.filter_sort + self.filter_time + self.filter_limit,
                headers=self.headers)
            
            print("https://oauth.reddit.com/r/" + self.subreddit + "/search/?q=" + self.search_term + "&restrict_sr=on" + self.filter_sort + self.filter_time + self.filter_limit)
            #error_handle(res)
            self.search_process(res)  


        ## -- Subreddit Search -- ##
        else:
            print("ELSE")
            res = requests.get("https://oauth.reddit.com/search/?q=" + self.search_term + self.filter_sort + self.filter_time + self.filter_limit,
                headers=self.headers)
            
            print("https://oauth.reddit.com/search/?q=" + self.search_term + self.filter_sort + self.filter_time + self.filter_limit)
            
            #error_handle(res)
            self.search_process(res)

    def search_process(self, res):

        ####################
        ## Setup stuff
        ####################
        try:
            self.total_posts = len(res.json()['data']['children'])
        except:
            self.total_posts = 0

        ####################
        ## Main Loop
        ####################
        for post in (res.json()['data']['children']):
            #print(len(res.json()['data']['children']))
            #print("+1")


        ################################################################################
        ## These HAVE to go first so the loop grabs the info the first time around
        ## Getting Post URL ##
            try:
                post_url = post['data']['url']
            except:
                post_url = "Problem with getting URL"


        ## Getting Subreddit, removing ' and limiting to 35 characters  ##
            subreddit_transform = post['data']['subreddit']
            subreddit = subreddit_transform.replace("'","")

        ## Getting Title, removing ' and limiting to 35 characters  ##
            try:
                title_tranfsorm = post['data']['title']
                title = title_tranfsorm.replace("'","")
                #format_title = title_tranfsorm.replace("'","")
            except:
                title = "Problem with getting the Title"

        ################################################################################

        ## -- Getting Media URL -- ##
            try:
                video_url_raw = post['data']['secure_media']['reddit_video']['fallback_url']
                #print(video_url_raw)
                #x = pyshorteners.Shortener()
                #video_url= x.tinyurl.short(video_url_raw)
                    #print(video_url_raw)

                    ## deciding whether to download media or not
                '''
                if args.vd:
                    video_download(video_url_raw)'''
            except:
                #print('URL not found')
                video_url_raw = "NO VIDEO IN POST"

        ## --Saving JSON-- ##
            '''           
            if args.json_html:
                #pass
                file_handle_JSON_in_HTML(res)'''

        ## -- Saving Link -- ##   
            '''     
            if args.link:
                #pass
                file_handle_LINK(res)'''
                
        ## -- Comments -- ##
            if self.options_list[1]:
                comment_raw = post['data']['selftext']
                if comment_raw == "":
                    comment = "Keyword found, check post"
                else:
                    comment = comment_raw
            else:
                comment = "N/A"
        ## -- user -- ##
            ## Quick differentiate for who wrote the posts vs comments
            if self.options_list[1]:
                user = post['data']['author']
            else:
                user = post['data']['author']

        ## -- Shortening URLS of the post -- ##
            post_url_raw = post['data']['permalink'] ## This is where the r/LINK data is stored, so I have to add reddit.com/ infront of it
            post_url_permalink = "https://reddit.com" + post_url_raw
            #s = pyshorteners.Shortener()
            #post_url= s.tinyurl.short(post_url_permalink)
            post_url = post_url_permalink 

        ## -- Sorting uPvotes/Downvotes -- ##
            upvote = post['data']['ups']
            downvote = post['data']['downs']

        ## -- getting date -- ##
            #date = datetime.fromtimestamp(post['data']['created_utc'].strftime("%Y-%m-%d"))
            #time = datetime.fromtimestamp(post['data']['created_utc'].strftime("%H:%M:%S"))

        ## Creating list to write to db
            insert_list = [subreddit, title, comment, upvote, downvote, post_url, video_url_raw, "date", "time", user]
            
            database_write_data(insert_list)
            
            self.current_post = self.current_post + 1

        ## -- Error handling incase no subreddit is supplied -- ##




####################
## DB Connect
####################
def database_read_creds():
    try:
        ## Accesing DB in root dir
        
        sqliteConnection = sqlite3.connect(os.path.dirname(__file__) + '/../../../logec_db')

        cursor = sqliteConnection.cursor()
        #print("Successfully Connected to SQLite")
        
        sqlite_get_query = "select * from AppCredentials where App = 'Reddit'"
        get_user = "select User from AppCredentials where App = 'Reddit'"
        get_pass = "select Pass from AppCredentials where App = 'Reddit'"
        get_token = "select Token from AppCredentials where App = 'Reddit'"
        get_id = "select ID from AppCredentials where App = 'Reddit'"


        ## there is probably a faster way to do this
        cursor.execute(get_user)
        user = cursor.fetchone()[0]
        
        cursor.execute(get_pass)
        password = cursor.fetchone()[0]
        
        cursor.execute(get_token)
        token = cursor.fetchone()[0]
        
        cursor.execute(get_id)
        id = cursor.fetchone()[0]
        
        sqliteConnection.commit()
        cursor.close()
        
        creds_tuple = (user,password, token, id)
        #print(creds_tuple)
        return creds_tuple
        
    except sqlite3.Error as error:
        print("Error:", error)
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("The SQLite connection is closed")

def table_wipe():
        sqliteConnection = sqlite3.connect(os.path.dirname(__file__) + '/../../../logec_db')
        cursor = sqliteConnection.cursor()

        sqlite_wipe = "DELETE FROM RedditResults"
        cursor.execute(sqlite_wipe)
        
        sqliteConnection.commit()
        cursor.close()


def database_write_data(insert_list):
    try:
        #print(insert_list)
        ## Accesing DB in root dir
        
        sqliteConnection = sqlite3.connect(os.path.dirname(__file__) + '/../../../logec_db')

        cursor = sqliteConnection.cursor()
        
        ## if append is not true:


        sqlite_insert_query = f"""INSERT INTO RedditResults (Subreddit, Title, Comment, Upvotes, Downvotes, PostUrl, MediaUrl, CreationDate, CreationTime, User) 
        VALUES
        ("{insert_list[0]}", "{insert_list[1]}", "{insert_list[2]}", '{insert_list[3]}', '{insert_list[4]}', '{insert_list[5]}', '{insert_list[6]}', "{insert_list[7]}", "{insert_list[8]}",  "{insert_list[9]}")"""
        
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
        
    except sqlite3.Error as error:
        print("Error:", error)
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("The SQLite connection is closed")