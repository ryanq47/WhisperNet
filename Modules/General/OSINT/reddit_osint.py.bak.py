#Doc: https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c

## ideas: requests counter to see how many in hour (due to reddit APIlimitation)
#pyshorteners: https://pyshorteners.readthedocs.io/en/latest/ <<SUPER AWESOME !! note: osdb + tinyurl do not need API login

#praw : https://praw.readthedocs.io/en/stable/tutorials/comments.html



## README
## Need to get JSON from comment response, and then filter items based on that. I *could* use praw, but thats no fun
## Praw may come in handy for comments that are not top level, it would search the json and fill in the comment feild







##USE TABS
#basic imports
from gettext import install
from turtle import back
import requests
import argparse
import time

#colors
from rich import print
from rich.progress import track
from rich.traceback import install
install()
import random

## error handling cause panda is being picky
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#formatting
import pandas as pd
from datetime import datetime
import pyshorteners

#doing stuff with data
import json
import subprocess as sp
import os
from json2html import *
import re


#making this look somewhwat okay
import pyfiglet


####################
## Credentials
####################

load_creds = open("config/credentials.json")

creds = json.load(load_creds)

## Reddit Login Info
SECRET_TOKEN = creds['SECRET_TOKEN']
CLIENT_ID= creds['CLIENT_ID']

REDDIT_USERNAME = creds['REDDIT_USERNAME']
REDDIT_PASSWORD = creds['REDDIT_PASSWORD']

USER_AGENT = "Beta Bot 0.1.1"
##############################

####################
## Arg Parse
####################

parser = argparse.ArgumentParser(description='Arg Parser')
parser.add_argument('-s',"--search", required=True, help ='Search function, if spaces are in the argument, add "", ex: "Harry Potter", use * for wildcard')
#parser.add_argument('-s', action='store_true', required=False) #Search

#parser.add_argument('-s', action='store_true', required=False) #Search
parser.add_argument('-vd', action='store_true', help="Add this to download all videos associated with a post, saved in /output" ,required=False) #Video Download
parser.add_argument('-jh','--json_html', action='store_true', required=False, help="##Currently Broken ## Export JSON data in HTML format (No CSS data so it is very ugly, but cleaner than raw json)") #store as html
parser.add_argument('-l','--link', action='store_true', required=False, help="##Currently Broken ## Direct Link to Reddit post") #store as html
parser.add_argument('-sbr','--subreddit', required=False, help="Search a subreddit instead of entire reddit") #store as html

## -- Specific type searches -- ##
parser.add_argument('-c', action='store_true', required=False, help="##Currently Broken ## Export JSON data in HTML format (No CSS data so it is very ugly, but cleaner than raw json)") #store as html
parser.add_argument('-u', action='store_true', required=False, help="User Profile Search - note! Cannot search for specific terms within the user's profile (...yet) so put username in -s flag") #store as html

##Filters
parser.add_argument('--sort', required=False, help="Sort by: top, hot, new, controversial, comments" ) #store as html
parser.add_argument('--limit', required=False, help="How many posts to display on screen, max is 100")
parser.add_argument('--time', required=False, help="Time to filter by: all, year, month, day, hour - needs -sort flag to work")

parser.add_argument('--EXAMPLE', required=False, help="python3 main.py  -s ferrari --sort hot -sbr idiotsincars --limit 30 --time all -vd  " ) #store as html



args = vars(parser.parse_args())

search_term = (args["search"])
subreddit= (args["subreddit"])

####################
## Filter logic
####################

filter_time_raw = (args["time"])
try:
    filter_time = "&t=" + filter_time_raw.lower()
except:
    filter_time = ""

filter_sort_raw = (args["sort"])
try:
    filter_sort= "&sort=" + filter_sort_raw.lower()
except:
    filter_sort=""

filter_limit_raw = (args["limit"])
try:
    filter_limit =  "&limit=" + filter_limit_raw
except:
    filter_limit = ""
    #filter_limit="&limit=25" ##<< Sets default to 25
 
####################
## Startup
####################
color_list = "green", "blue", "red", "yellow", "purple"
random_color = random.choice(color_list)

def startup():
    os.system('clear')
    print(''' [''' + random_color + ''']
 /$$$$$$$                  /$$       /$$ /$$   /$$            /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$      
| $$__  $$                | $$      | $$|__/  | $$           /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__/      
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$$ /$$ /$$$$$$        | $$  \ $$| $$  \__/  | $$  | $$$$| $$   | $$         
| $$$$$$$/ /$$__  $$ /$$__  $$ /$$__  $$| $$|_  $$_/        | $$  | $$|  $$$$$$   | $$  | $$ $$ $$   | $$         
| $$__  $$| $$$$$$$$| $$  | $$| $$  | $$| $$  | $$          | $$  | $$ \____  $$  | $$  | $$  $$$$   | $$         
| $$  \ $$| $$_____/| $$  | $$| $$  | $$| $$  | $$ /$$      | $$  | $$ /$$  \ $$  | $$  | $$\  $$$   | $$         
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  |  $$$$/      |  $$$$$$/|  $$$$$$/ /$$$$$$| $$ \  $$   | $$         
|__/  |__/ \_______/ \_______/ \_______/|__/   \___/         \______/  \______/ |______/|__/  \__/   |__/   

                                            [i]www.github.com/ryanq47
    
    ''')

    intro_options()
    print("\n")
    print("[white] Getting Oauth stuff... this may take a minute (reddit servers are potatoes)")

    print("\n")


####################
## Intro Logic
####################
def intro_options():
    args = parser.parse_args()

    if args.json_html:
        print("Getting JSON_HTML: [green] Enabled")
    else:
        print("Getting JSON_HTML: [red] Disabled")
            
    if args.link:
        print("Saving Links: [green] Enabled")
    else:
        print("Saving Links: [red] Disabled")
    if args.vd:
        print("Downloading Media: [green] Enabled")
    else:
        print("Downloading Media: [red] Disabled")
    if args.c:
        print("(BETA) Comment Search : [green] Enabled")
    else:
        print("(BETA) Comment Search: [red] Disabled")
    if args.u:
        print("User Stalking Mode: [green] Enabled")
    else:
        print("User Stalking Mode: [red] Disabled")




####################
## Authentication
####################

def OAuth():
    args = parser.parse_args()
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
    OAuth.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    search()




####################
## Main Search 
####################

def search(): #<< Where all the logic/decisions will go, based on arguments. if this then run that function
    args = parser.parse_args()

    ## -- ALl of reddit search -- ##
    if args.u:
        
        #print("DEBUG: args.u")
        res = requests.get("https://oauth.reddit.com/user/" + search_term + "/" + filter_sort.replace("&","?") + filter_time + filter_limit,
            headers=OAuth.headers)
        error_handle(res)
        user_search_process(res)

    elif args.c:
        print("DEBUG: args.c")
        res = requests.get("https://oauth.reddit.com/search/?q=" + search_term + filter_sort + filter_time + filter_limit + "&type=comment",
            headers=OAuth.headers)
        error_handle(res)
        comment_search_process(res)

    elif args.subreddit == None:     
        res = requests.get("https://oauth.reddit.com/search/?q=" + search_term + filter_sort + filter_time + filter_limit,
            headers=OAuth.headers)
        print("https://oauth.reddit.com/search/?q=" + search_term + filter_sort + filter_time + filter_limit)
        error_handle(res)
        search_process(res)

    ## -- Subreddit Search -- ##
    else:
        res = requests.get("https://oauth.reddit.com/r/" + args.subreddit + "/search/?q=" + search_term + "&restrict_sr=on" + filter_sort + filter_time + filter_limit,
            headers=OAuth.headers)
        print("https://oauth.reddit.com/r/" + args.subreddit + "/search/?q=" + search_term + "&restrict_sr=on" + filter_sort + filter_time + filter_limit)
        error_handle(res)
        search_process(res)    
    
    ## -- Sending through the filter to be displayed properly -- ##

def error_handle(res):
    args = parser.parse_args()

    if 1 == 100:
        pass

    

    ####################
    ## Response Error Handling - must go first in error chain, otherwise you get a key error 
    ####################
    elif '{"kind": "Listing", "data": {"after": null, "dist": 0, "modhash": null, "geo_filter": "", "children": [], "before": null}}' in res.text:
        print(f"""
##--> 'r/{args.subreddit}' most likely does not exist :(
    ##--> Maybe create it?\n""")
        print("##--> " + res.text)
        exit()
    ## Banned Subreddit 
    elif '"reason": "banned"' in res.text:
        print(f"""
##--> '{args.subreddit}' has been banned
    ##--> Nothing you can do about this one \n""")
        print("##--> " + res.text)
        exit()

    ## Not Found error (keep at end so more detailed errors can be had if possible)
    elif '"message": "Not Found"' in res.text:
        print(f"""
##--> '{args.search}' '{args.subreddit}' Not Found
    ##--> Check Username, Subbreddit, etc to ensure it exists\n""")
        print("##--> " + res.text)
        exit()

    ####################
    ## Warning Filtering
    ####################

    if args.time not in [None, "all", "now", "week", "day", "month", "year"]:
        print(f"[yellow]##--> WARNING: '{args.time}' is not a valid time search parameter, results may be unexpected")

    if args.sort not in [None, "all", "new", "top", "rising", "controversial", "hot", "comments"]:
        print(f"[yellow]##--> WARNING: '{args.sort}' is not a valid sorting parameter, results may be unexpected")
    try:
        if int(args.limit) > 1000:
            print(f"[yellow]##--> WARNING: '{args.limit}' is outside of valid limit range (1-1000)")
    except:
        pass
    ####################
    ## Unsupported flag warning? might take some work
    ####################
    
    else:
        pass
    
    print("\n")


    

def comment_search():
    print("comment search here")

    submission = reddit.submission(url="https://www.reddit.com/r/memes/comments/wpwe2u/well_damn/")

    for top_level_comment in submission.comments:
        print(top_level_comment.body)


def search_process(res):
    args = parser.parse_args()

    ####################
    ## Panda Options
    ####################
    #pd docs: pandas.pydata.org/pandas-docs/stable/user_guide/options.html
    df = pd.DataFrame()

    pd.options.display.max_rows = 100
    pd.set_option('display.max_colwidth', 0)

    ####################
    ## Main Loop
    ####################
    for post in track(res.json()['data']['children'], description="Retrieving reddit data..."):

    ################################################################################
    ## These HAVE to go first so the loop grabs the info the first time around
    ## Getting Post URL ##
        search.post_url = post['data']['url']


    ## Getting Subreddit, removing ' and limiting to 35 characters  ##
        subreddit_transform = post['data']['subreddit']
        search.subreddit = subreddit_transform.replace("'","")[:35]

    ## Getting Title, removing ' and limiting to 35 characters  ##

        title_tranfsorm = post['data']['title']
        search.title = title_tranfsorm.replace("'","")[:35]
        search.format_title = title_tranfsorm.replace("'","")[:35]

    ################################################################################

    ## -- Getting Media URL -- ##
        try:
            video_url_raw = post['data']['secure_media']['reddit_video']['fallback_url']
            #print(video_url_raw)
            x = pyshorteners.Shortener()
            video_url= x.tinyurl.short(video_url_raw)
                #print(video_url_raw)

                ## deciding whether to download media or not
            if args.vd:
                video_download(video_url_raw)
        except:
            #print('URL not found')
            video_url = "NO VIDEO IN POST"

    ## --Saving JSON-- ##           
        if args.json_html:
            #pass
            file_handle_JSON_in_HTML(res)

    ## -- Saving Link -- ##        
        if args.link:
            #pass
            file_handle_LINK(res)

    ## -- Shortening URLS -- ##
        post_url_raw = post['data']['permalink'] ## This is where the r/LINK data is stored, so I have to add reddit.com/ infront of it
        post_url_permalink = "https://reddit.com/" + post_url_raw
        s = pyshorteners.Shortener()
        post_url= s.tinyurl.short(post_url_permalink)

    ## -- Sorting uPvotes/Downvotes -- ##
        upvote = post['data']['ups']
        downvote = post['data']['downs']

        upvotes_downvotes = str(upvote) + " | " + str(downvote)

    ################
     ## Final Formmating 
    ################
        df = df.append({
            #'URL': post['data']['secure_media']['reddit_video']['fallback_url'],
            
            'Subreddit  |': post['data']['subreddit'],
            'Up/Down' : upvotes_downvotes,
            'Title |': search.format_title,
            'Post URL |': post_url,
            #'selftext': post['data']['selftext'],
            #'Video_URL |': video_url,
            'Date/Time Created (UTC) |': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d | %H:%M:%S'),
        }, ignore_index=True)


    ## -- Error handling incase no subreddit is supplied -- ##

    if args.subreddit == None:
        subreddit = "r/All, All of reddit"
    else:
        subreddit = "r/" + args.subreddit

    ## -- Banner/Table structure -- ##
    print("==============================================================================================================================================")
    info_banner = ("================ [red]Subreddit: " + subreddit + " | Search Term: " + search_term + "[/red] || [blue] Relevance: " + filter_sort[6:12] +" | Time: " + filter_time[3:12] + " | Number of Results: " + filter_limit[7:18] + "[/blue] ================")
    print(info_banner[:142]) ##limits length to make it look pretty when printing
    print("==============================================================================================================================================\n")


    print(df)
    
def comment_search_process(res):
    args = parser.parse_args()

    ####################
    ## Panda Options
    ####################
    #pd docs: pandas.pydata.org/pandas-docs/stable/user_guide/options.html
    df = pd.DataFrame()

    pd.options.display.max_rows = 100
    pd.set_option('display.max_colwidth', 0)

    ####################
    ## Main Loop
    ####################
    for post in track(res.json()['data']['children'], description="Retrieving reddit data..."):

    ################################################################################
    ## These HAVE to go first so the loop grabs the info the first time around
    ## Getting Post URL ##
        search.post_url = post['data']['url']


    ## Getting Subreddit, removing ' and limiting to 35 characters  ##
        subreddit_transform = post['data']['subreddit']
        search.subreddit = subreddit_transform.replace("'","")[:35]

    ## Getting Title, removing ' and limiting to 35 characters  ##

        title_tranfsorm = post['data']['title']
        search.title = title_tranfsorm.replace("'","")[:35]
        search.format_title = title_tranfsorm.replace("'","")[:35]

    ################################################################################

    ## --Saving JSON-- ##           
        if args.json_html:
            #pass
            file_handle_JSON_in_HTML(res)

    ## -- Saving Link -- ##        
        if args.link:
            #pass
            file_handle_LINK(res)

    ## -- Shortening URLS -- ##
        post_url_raw = post['data']['permalink'] ## This is where the r/LINK data is stored, so I have to add reddit.com/ infront of it
        post_url_permalink = "https://reddit.com/" + post_url_raw
        s = pyshorteners.Shortener()
        post_url= s.tinyurl.short(post_url_permalink)

    ## -- Sorting uPvotes/Downvotes -- ##
        upvote = post['data']['ups']
        downvote = post['data']['downs']

        upvotes_downvotes = str(upvote) + " | " + str(downvote)

    ## -- COmments -- ##
        comment_raw = post['data']['selftext']
        if comment_raw == "":
            comment = "TERM found, check here -->"
        else:
            comment = comment_raw[:25]
    
    ################
     ## Final Formmating 
    ################
        df = df.append({
            #'URL': post['data']['secure_media']['reddit_video']['fallback_url'],
            
            'Subreddit  |': post['data']['subreddit'],
            'User  |': post['data']['author'], ## Link to user account
            'Up/Down' : upvotes_downvotes,
            'Comment |': comment,
            'Comment URL |': post_url,
            'User URL |': "USERURL",
            'Date/Time Created (UTC) |': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d | %H:%M:%S'),
        }, ignore_index=True)

    ## -- Error handling incase no subreddit is supplied -- ##

    if args.subreddit == None:
        subreddit = "r/All, All of reddit"
    else:
        subreddit = "r/" + args.subreddit

    ## -- Banner/Table structure -- ##
    print("==============================================================================================================================================")
    info_banner = ("================ [red]Subreddit: " + subreddit + " | Search Term: " + search_term + "[/red] || [blue] Relevance: " + filter_sort[6:12] +" | Time: " + filter_time[3:12] + " | Number of Results: " + filter_limit[7:18] + "[/blue] ================")
    print(info_banner[:142]) ##limits length to make it look pretty when printing
    print("==============================================================================================================================================\n")
   
    ## -- printing Banner/Table -- ##
    print(df)

def user_search_process(res):
    args = parser.parse_args()

    ####################
    ## Panda Options
    ####################
    #pd docs: pandas.pydata.org/pandas-docs/stable/user_guide/options.html
    df = pd.DataFrame()

    pd.options.display.max_rows = 100
    pd.set_option('display.max_colwidth', 0)
    ####################
    ## Regex
    ####################
    info_grab(res)

    ####################
    ## Main Loop
    ####################

    for post in track(res.json()['data']['children'], description="Retrieving reddit data..."):
    ################################################################################
    ## -->> Error: You probably entered the username wrong - or have an unsupported flag - or the user dosen't exist :) <<--
    ################################################################################

    ## Getting Post URL ##
        try:
            search.post_url = post['data']['url']
        except:
            search.post_url = "URL not found"


    ## Getting Subreddit, removing ' and limiting to 35 characters  ##
        subreddit_transform = post['data']['subreddit']
        search.subreddit = subreddit_transform.replace("'","")[:35]

    ## Getting Title, removing ' and limiting to 35 characters  ##
        try:
            title_tranfsorm = post['data']['title']
            search.title = "Post: " + title_tranfsorm.replace("'","")[:35]
        except:
            search.title = ""
            #search.title = "[Post: ] "
        try:
            comment_tranfsorm = post['data']['body']
            search.comment = "Comment: " + comment_tranfsorm.replace("'","")[:35]
        except:
            #search.comment = "[Comment: ] "
            search.comment = ""

    ## --Saving JSON-- ##           
        if args.json_html:
            file_handle_JSON_in_HTML(res)

    ## -- Saving Link -- ##        
        if args.link:
            file_handle_LINK(res)

    ## -- Shortening URLS -- ##
        post_url_raw = post['data']['permalink'] ## This is where the r/LINK data is stored, so I have to add reddit.com/ infront of it
        post_url_permalink = "https://reddit.com/" + post_url_raw
        s = pyshorteners.Shortener()
        post_url= s.osdb.short(post_url_permalink)

    ## -- Sorting uPvotes/Downvotes -- ##
        upvote = post['data']['ups']
        downvote = post['data']['downs']

        upvotes_downvotes = str(upvote) + " | " + str(downvote)

    ################
     ## DataFrame Formatting
    ################

        df = df.append({
            #'URL': post['data']['secure_media']['reddit_video']['fallback_url'],
            'User  |': post['data']['author'], ## Link to user account
            'Up/Down' : upvotes_downvotes,
            'Post/Comment': search.title + search.comment,
            'Post/Comment URL |': post_url,
            #'User URL |': "USERURL",
            'Date/Time Created (UTC) |': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d | %H:%M:%S'),
        }, ignore_index=True)

    ################
     ## Banner/Table
    ################

    print("==============================================================================================================================================")
    info_banner = ("================ [red] User: " + search_term + "[/red] || [blue] Relevance: " + filter_sort[6:20] +" | Time: " + filter_time[3:12] + " | Results: " + filter_limit[7:50] + "================")
    print(info_banner[:155]) ##limits length to make it look pretty when printing
    print("==============================================================================================================================================")
    user_info_banner = ("================ [yellow]Possible Email: " + str(info_grab.email) + " [/yellow]| [yellow] Phone Number: " + str(info_grab.phone) + "[/yellow] || [blue] Other: " + "other.github.com" + " [/blue] ================")
    print(user_info_banner)  
    print("==============================================================================================================================================")

    ## -- printing dataframe -- ##
    print(df)

###############
## Info Grab Logic
################
def info_grab(res):
    info_grab.email = re.findall('\S+@\S+', res.text)  #https://uibakery.io/regex-library/phone-number-python
    info_grab.phone = re.findall("\d{3}-\d{3}-\d{4}", res.text) #https://www.w3schools.com/python/python_regex.asp


###############
## Video Download Logic
################

def video_download(url):
    ## making Dirs
    try:
        os.makedirs("media/" + search.subreddit, exist_ok=False)
    except:
        pass
    #Doing WGET
    wget = sp.getoutput("wget -cO - " + url + " > media/" + search.subreddit + "/'" + search.title.replace("/","_") + "'")
    #print(wget)
    wget

###############
## JSON download Logic
################

def file_handle_JSON_in_HTML(res):
    fileload = json.loads(res.text)
    json_html = json2html.convert(json = fileload)

    os.makedirs("JSON_in_HTML/", exist_ok=True)
    try:
        f = open("JSON_in_HTML/"+ search.title + ".html", "w")
        f.write(json_html)
        f.close()
    except: 
        pass
###############
## Link Download logic
################
def file_handle_LINK(res):
    try:
        os.makedirs("links/", exist_ok=False)
    except: 
        pass
    try: 
        f=open("links/" + search.title, "x")
        f.write('''
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url=''' + search.post_url + '''" />
            </head>
            <body> </body>
        </html>

        ''')
        f.close()
    except: 
        pass



##########
## Main Run
##########
if __name__ == "__main__":
    startup()
    OAuth()


