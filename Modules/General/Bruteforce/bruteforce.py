## Hi - this code isn't great, but it works and I haven't had the time to rewrite it - sooo yeah

from PySide6.QtCore import QThread, Signal, QObject, Slot, QRunnable, QThreadPool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import time
import random
#import sqlite3
import os
import queue
import numpy as np
import requests
import itertools  

## Connection Libs
from ftplib import FTP

import warnings
with warnings.catch_warnings(): ## tells paramiko to shut up
    warnings.simplefilter("ignore")
    import paramiko




import Modules.General.utility as utility

## printing out a shitload of stuff for some reason
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs/bruteforce.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'
)

# Set the logging level for the requests & urllib library to CRITICAL
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.WARNING)
#if global_debug:
#logging.getLogger().addHandler(logging.StreamHandler())

## Use Yeild for progress updates to the bar


class Bruteforce(QObject):
    module_error = Signal(list)
    finished = Signal()
    progress = Signal(int)
    goodcreds = Signal(list)    
    
    live_attempts = Signal(str) 
    current_batch = Signal(list)
    num_of_batches = Signal(list)
    errlog = Signal(str)
    
    results_list = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.H = utility.Host()
        
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.good_creds = []
        
        self.bruteforce_progress = 0
        self.number = 0
        
        self.log_tag = "[Bruteforce (Credentials)]"
    
    def error(self, Error, Severity, Message):
        logging.debug(f"{self.log_tag} {Error}")
        #print("ERRORRRRRR")
        error_list = [Error, Severity, Message]
        #print(error_list)
        ## Emiting back to main thread
        
        self.module_error.emit(error_list)
        self.finished.emit()
        
    def success(self, username, password, target=None):
        ## Done as a tuple to reduce mem size + so it can be appended
        self.good_creds.append((username, password))
        self.goodcreds.emit(self.good_creds)
        logging.debug(f"{self.log_tag} Successful Credentials: {username}:{password}@{target}")
    
    def db_emit(self):
        """Emits valid credentials back to the main thread to be written to the DB
        """
        good_creds = ""
        for i in self.good_creds:
            good_creds = good_creds + f"{i[0]}:{i[1]}, "
        
        self.results_list.emit([
            self.IP,
            self.port,
            self.protocol,
            good_creds,
            self.Time,
            self.Date
        ])

    def thread_quit(self):
        #print("EXIT")
        self.thread_quit = True
        #self.errlog.emit("Stopping BruteForce")
        logging.debug("{self.log_tag} Stopping Bruteforce")
        #exit()
        
    def fileopen(self, dir):
        """Takes a file, opens it, and determins encoding based on the file. Prevents weird errors with 
        different encoding types

        Args:
            dir (str): The file path

        Returns:
            str: The decoded file. 
        """
        import chardet
        with open(dir,"rb") as file_bytes:
            file_read_bytes = file_bytes.read()
            
            encoding= chardet.detect(file_read_bytes)
            decode_type =  encoding['encoding']
            #print(decode_type)
            
            file = file_read_bytes.decode(decode_type)
            #file = file_raw.decode('utf-8')
            #self.errlog.emit(f"File Encoding: {decode_type}")
            logging.debug(f"{self.log_tag} File Encoding for {dir}: {decode_type}")
            return file
        
    def generate_creds(self, usernames, passwords):
        """A credential generator, takes each username, adds a password, and yeilds that combo

        Args:
            usernames (str): the usernames
            passwords (_type_): the passwords

        Yields:
            _type_: the username/pass combo
        """
        for username in usernames:
            for password in passwords:
                yield (username, password)
             
    def worker(self, creds): ## Not sure what this does
        pass
    
    def bruteforce_framework(self, input_list): ## should probably migrate to a dict instead of a list eventually
        try:
            logging.debug(f"{self.log_tag} Attack Started: {input_list}")
            #self.GUI.ERROR("low", "error","something")
            
            self.Date = utility.Timestamp.UTC_Date()
            self.Time = utility.Timestamp.UTC_Time()
            
            self.errlog.emit("Date:" + str(self.Date))
            self.errlog.emit("Time:" + str(self.Time))
            
            ## Breaking the list up
            self.IP, self.port, self.protocol, user_wordlist_dir, pass_wordlist_dir, self.delay, self.max_threads, self.batchsize = input_list[:8]
            
            user_list = []
            self.pass_list = []
            self.dir_list = []
            
            ## Results list
            self.results_dir_list = []
            
            ## Creating target list - I know I could just use the input_list, however this cuts down on the amount of arguments I need to enter in each method
            #target_list = [ip, port, delay]
            
        except Exception as e:
            #print(e)
            logging.debug(f"{self.log_tag} Error with attack: {e}")
            #self.error(e,"??","??")
            exit()

        ## using the custom file open here for encoding type stuff
        username = self.fileopen(user_wordlist_dir)
        password = self.fileopen(pass_wordlist_dir)
        
        ## some data for stats on how big this is
        user_list_len = username.split()
        pass_list_len = password.split()
        self.total_combos = len(user_list_len) * len(pass_list_len)
            
        userpass_combo = itertools.product(username.split(),password.split())
        
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
                if self.protocol == "SSH":
                    self.ssh_processor(batch)
                if self.protocol == "FTP":
                    self.ftp_processor(batch)
        
        ## Returning Final values to write to DB
        #print("Emmiting final")
        self.db_emit()
                    
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

    def ftp_processor(self, batch):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for i in batch:
                ## Max workers needs fine tunning/an option for how many threads
                ## Generator to help cut down on ram usage
                #print(i)##<< prints each attempt
                ftp_thread = executor.submit(self.ftp, i)

            ftp_thread.result()
            #print("Done")
            self.done = True
            
    def ftp(self, creds):
        username, password = creds
        #sername = creds[0]
        #password = creds[1]
        
        try:
            time.sleep(random.uniform(0,self.delay))
            
            ftp = FTP(self.IP, timeout=.1)
            ftp.login(username, password)
            ftp.close() ## Close is a bit harsher than quit, but quits it asap
            
            self.success(username, password, self.IP)
            
        ## Blind exception becuase this will happen SO often
        except TimeoutError:
            pass
        
        except Exception as e:
            ## closing FTP connection on error
            logging.debug(f"[Bruteforce (Credentials: FTP)] Error: {e}")
            self.errlog.emit(str(e))            
            try:
                ftp.close()
            except Exception as ee:
                logging.debug(f"[Bruteforce (Credentials: FTP)] Error: {ee}")
                #self.errlog.emit("Could Not close FTP session")
            #self.error(e,"low","testerror")
            
        finally:
            try:
                ftp.close()
            except Exception as ee:
                logging.debug(f"[Bruteforce (Credentials: FTP)] Error: {ee}")
                #self.errlog.emit("Could Not close FTP session")

            self.bruteforce_progress = self.bruteforce_progress + 1
            self.progress.emit(int(self.bruteforce_progress / self.total_combos * 100))  
        
            ## Live update in GUI, if num is 0 it was unsuccessful
        self.number = self.number + 1
        if self.number == 1:
            self.live_attempts.emit(username + ":" + password)
            self.number = 0

    def ssh(self, creds):
        _username, _password = creds
        #_username = creds[0] # _ for namespace reasons
        #_password = creds[1]
        
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
            logging.debug(f"[Bruteforce (Credentials: SSH)] Error: {e}")
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


class Fuzzer(QObject):
    
    module_error = Signal(list)
    finished = Signal()
    progress = Signal(int)
    gooddir = Signal(list)    
    
    live_attempts = Signal(str) 
    current_batch = Signal(list)
    num_of_batches = Signal(list)
    errlog = Signal(str)

    results_list = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.good_dir_list = []
        
        self.bruteforce_progress = 0
        self.number = 0
        
        self.log_tag = "[Bruteforce (WebDir Fuzzer)]"
        
    def fileopen(self, dir):
        """Takes a file, opens it, and determins encoding based on the file. Prevents weird errors with 
        different encoding types

        Args:
            dir (str): The file path

        Returns:
            str: The decoded file. 
        """
        import chardet
        with open(dir,"rb") as file_bytes:
            file_read_bytes = file_bytes.read()
            
            encoding= chardet.detect(file_read_bytes)
            decode_type =  encoding['encoding']
            #print(decode_type)
            
            file = file_read_bytes.decode(decode_type)
            #file = file_raw.decode('utf-8')
            #self.errlog.emit(f"File Encoding: {decode_type}")
            logging.debug(f"{self.log_tag} File Encoding for {dir}: {decode_type}")
            return file
        
    def success(self, dir):
        ## Done as a tuple to reduce mem size + so it can be appended
        self.good_dir_list.append(dir)
        self.gooddir.emit(self.good_dir_list)
        
        
    def db_emit(self, emit_list):
        
        logging.debug(f"{self.log_tag} Emiting to DB: {emit_list}")
        self.results_list.emit([
            emit_list[0],
            emit_list[1],
            emit_list[2],
            emit_list[3],
            emit_list[4],
            emit_list[5],
            emit_list[6]
        ])


    def thread_quit(self):
        logging.debug(f"{self.log_tag} Attempting to stop the current attack")
        self.thread_quit = True
        logging.debug(f"{self.log_tag} Stopping Fuzzer")
        #self.errlog.emit("Stopping Fuzzer")
        #exit()
    
    def fuzzer_framework(self, input_list):
        try:
            logging.debug(f"{self.log_tag} Starting attack: {input_list}")            
            #self.GUI.ERROR("low", "error","something")
            
            self.Date = utility.Timestamp.UTC_Date()
            self.Time = utility.Timestamp.UTC_Time()
            
            self.errlog.emit("Date:" + str(self.Date))
            self.errlog.emit("Time:" + str(self.Time))
            
            ## Breaking the list up
            
            self.URL = input_list[0]
            self.port = input_list[1]
            wordlist = input_list[2]
            self.delay = input_list[3]
            self.max_threads = input_list[4]
            self.batchsize = input_list[5]
            ## Takes gui input, gets rid of spaces, and splits on each comma
            self.validresponsec0de = list((input_list[6].replace(" ","")).split(","))
            self.show_full_url = input_list[7]   

            self.dir_list = []
            
            ## Results list
            self.results_dir_list = []
            
            ## Creating target list - I know I could just use the input_list, however this cuts down on the amount of arguments I need to enter in each method
            #target_list = [ip, port, delay]
            
        except Exception as e:
            logging.debug(f"{input_list} Error: {e}")
            #self.error(e,"??","??")
            exit()

### NOT LOOPING TO NEXT BATCH FOR SOME REASON;

        wordlistdir = self.fileopen(wordlist)
        #password = self.fileopen(pass_wordlist_dir)
        batch_iter = iter(wordlistdir.split()) 
        #user_list_len = username.split()
        #pass_list_len = password.split()
        
        ## Leaving like this for future expandability
        
        batch_iteration = 0
        total_batches = round(len(wordlistdir.split())/self.batchsize)
        
        for i in range(0,total_batches):
            batch_iteration = batch_iteration + 1
            
            batch = list(itertools.islice(batch_iter, self.batchsize))
            #logging.debug(f"{self.log_tag} Dev: Starting ThreadPoolExecutor")
            self.fuzzer_processor(batch)

            self.current_batch.emit(batch)
            self.num_of_batches.emit([batch_iteration, total_batches])
            
    def fuzzer_processor(self, batch):
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            #fuzzer_thread = None
            #print(batch)
            for i in batch:
                ## Max workers needs fine tunning/an option for how many threads
                ## Generator to help cut down on ram usage
                #print(i)##<< prints each attempt
                fuzzer_thread = executor.submit(self.fuzzer_request, i)
                    
            #print("BatchDone")
            fuzzer_thread.result()
            self.done = True
            #logging.debug(f"{self.log_tag} TPE Done")

    def fuzzer_request(self, fuzzvalue):
        """Makes the request to the targeted server.

        Args:
            fuzzvalue (str): the value that willbe placed where "FUZZ" is
        """
        #ip = self.URL ## Currently unusued
        port = self.port
        #fuzzvalue = request_list[2]
        raw_url = self.URL

        ## Rate limiter so you don't get kicked out, make the max value editable in GUI
        time.sleep(np.random.uniform(.001,.01)) 
        
        #base_url = request_list[0]
        
        # backup Port Handler
        if port == None:
            port = 80
        
        ## Replacing "FUZZ" with whatever fuzzvalue is passed in
        target_url = raw_url.replace("FUZZ",fuzzvalue)
        
        try:
            r = requests.get(target_url)
            #print(r.status_code)
            ## Nested if, I know, I'm sorry
            #print(self.validresponsec0de)
            for i in self.validresponsec0de:
                #print(i)
                if i in str(r.status_code):
                    
                    ## Writing success to db
                    self.db_emit([
                        raw_url,
                        port,
                        str(r.status_code),
                        fuzzvalue,
                        target_url,
                        self.Time,
                        self.Date
                    ])
                    
                    if self.show_full_url == True:
                        self.success(target_url)
                    else:
                        self.success(fuzzvalue)
                else:
                    pass
                    #print("FAUL")
            #print("ITERATION")
            
        except Exception as e:
            logging.debug(f"{self.log_tag} Error: {e}")
            self.errlog.emit(str(e))
        
        #print(target_url)
        
        #if r.status_code == 200:
