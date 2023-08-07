## A wrapper for GCC, and other compilation things for logec. Each wrapper uses it's own class. Classes are not
## static as you can't thread them with qt then (afaik...)

##Note: Make the subprocess timeout value a setting.

import os
from PySide6.QtCore import Signal, QObject
import subprocess

import logging
## has to go first
logging.basicConfig(level=logging.DEBUG)
#filename='logs/CompilationWrapper.log',
logging.basicConfig(filename='CompilationWrapper.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s', force=True)
logging.getLogger().addHandler(logging.StreamHandler())

## waiting to include QObject, inorder to test these functions standalone
class GccWrapper: #(QObject):
    Error = Signal(str)
    Success = Signal(dict)
    def __init__(self, codefile=None, savefile=None, savefile_name=None, flags=[""]):
        """
        The init function

        Parameters:
            codefile (str): location of uncompiled code. Ex: /opt/helloworld.c
            savefile (str): directory where compled code will be stored. Ex: /opt/compiled/helloworld
            savefile_name (str): The name of the compiled file. Seperate from savefile on purpose for error checking
            flags (list): some flags to include during compile time (still working out how this will
                utilized, i.e. list vs string & how to parse the flags

        """
        ## location of uncompiled code
        self.codefile = codefile
        ## directory of where the file will be saved
        self.savefile = savefile
        ## name of the file to be saved (seperate on purpose)
        self.savefile_name = savefile_name
        self.flags = flags


    def compile_framework(self):
        """ THis is the method to call to compile said items
        it will do error handling & handle calls to methods needed
        """
        if self.safe_to_compile():
            compilation_dict = self.compile(compile_command=self.format_compile_command())
            # if file exists
            print(compilation_dict)
            #self.Success.emit(compilation_dict)
            logging.debug(f"[CompilationWrapper(GCC: compile_framework)] Successful Compilation: {compilation_dict}")


        else:
            logging.debug(f"[CompilationWrapper(GCC: compile_framework)] safe_to_compile returned false. AKA something is "
                          f"not right")

    def compile(self, compile_command="") -> dict:
        ## subprocess run gcc with options

        try:
            output = subprocess.check_output(
                compile_command, stderr=subprocess.STDOUT, shell=True, timeout=60,
                universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            logging.debug(f"[CompilationWrapper(GCC: compile)] Error when compiling: {exc.returncode, exc.output}")
        except Exception as e:
            logging.debug(f"[CompilationWrapper(GCC: compile)] Unknown Error when compiling: {e}")

        compliation_dict = {
            "CompiledFileLocation": "placeholder",
            "OtherData": "OtherDataPlaceholder"
        }

        return compliation_dict

    def safe_to_compile(self) -> bool:
        """ Runs a series of checks to make sure all inputs are correct, if so, it returns true"""
        logging.debug(f"[CompilationWrapper(GCC: safe_to_compile)] Checking filepath")
        if not self.filecheck(self.codefile):
            return False

        logging.debug(f"[CompilationWrapper(GCC: safe_to_compile)] Checking directory path")
        if not self.pathcheck(self.savefile):
            return False

        ## if all pass, return true
        return True

    def format_compile_command(self) -> str:
        flags = ""
        flags = self.flag_formatter()

        ## Very open to vulns... needs some saftey checks, around flags & cmd injection too
        gcc_command = f"gcc {self.codefile} -o {self.savefile}/{self.savefile_name} {flags}"
        logging.debug(f"[CompilationWrapper(GCC: format_compile_command)] Formatted Command: {gcc_command}")
        return gcc_command

    def flag_formatter(self):
        """A formatter specifically for flags. Note, flags are passed as their own
        string from the calling function, so this will not affect any other part of the command.
        """
        flag_list = ""

        try:
            for flag in self.flags:
                flag_list += f" {flag}"
            logging.debug(f"[CompilationWrapper(GCC: flag_formatter)] Flags successfully extracted & formatted: {flag_list}")
        except Exception as e:
            logging.debug(f"[CompilationWrapper(GCC: flag_formatter)] Error: {e}")

        return flag_list

    def filecheck(self, filepath: str) -> bool:
        if os.path.isfile(filepath):
            logging.debug(f"[CompilationWrapper(GCC: filecheck)] '{filepath}' exists!")
            return True
        else:
            logging.debug(f"[CompilationWrapper(GCC: filecheck)] '{filepath}' does not exist, or is not a file.")
            return False
    def pathcheck(self, filepath: str) -> bool:
        """ For checking if the path of the outputed file exists before outputting it"""
        if os.path.exists(filepath):
            logging.debug(f"[CompilationWrapper(GCC: pathcheck)] '{filepath}' exists!")
            return True
        else:
            logging.debug(f"[CompilationWrapper(GCC: pathcheck)] '{filepath}' does not exist")
            return False

'''
GCC = GccWrapper(codefile="/home/kali/PycharmProjects/logec-suite/agent/c/client_unix.c",
                 savefile="/home/kali/PycharmProjects/logec-suite/agent/c/",
                 savefile_name="test_compile_client",
                 flags=["-Wall", "-Ofast"]
                 )
GCC.compile_framework()'''

class NuitkaWrapper(QObject): #
    Error = Signal(str)
    Success = Signal(dict)
    Update = Signal(str)
    def __init__(self, codefile=None, savefile=None, savefile_name=None, process_timeout=120, flags=[""]):
        super().__init__()
        """
        The init function

        Parameters:
            codefile (str): location of uncompiled code. Ex: /opt/helloworld.c
            savefile (str): directory where compled code will be stored. Ex: /opt/compiled/helloworld
            savefile_name (str): The name of the compiled file. Seperate from savefile on purpose for error checking
            flags (list): some flags to include during compile time (still working out how this will
                utilized, i.e. list vs string & how to parse the flags

        """
        ## location of uncompiled code
        self.codefile = codefile
        ## directory of where the file will be saved
        self.savefile = savefile
        ## name of the file to be saved (seperate on purpose)
        self.savefile_name = savefile_name
        self.process_timeout = process_timeout
        self.flags = flags


    def compile_framework(self):
        """ THis is the method to call to compile said items
        it will do error handling & handle calls to methods needed
        """
        self.Update.emit("[CompilationWrapper(Nuitka)] Started process")
        if self.safe_to_compile():
            compilation_dict = self.compile(compile_command=self.format_compile_command())
            # if file exists
            print(compilation_dict)
            #self.Success.emit(compilation_dict)
            logging.debug(f"[CompilationWrapper(GCC: compile_framework)] Successful Compilation: {compilation_dict}")

        else:
            logging.debug(f"[CompilationWrapper(GCC: compile_framework)] safe_to_compile returned false. AKA something is "
                          f"not right")

    def compile(self, compile_command="") -> dict:
        ## subprocess run gcc with options

        try:
            output = subprocess.check_output(
                compile_command, stderr=subprocess.STDOUT, shell=True, timeout=self.process_timeout,
                universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            logging.debug(f"[CompilationWrapper(GCC: compile)] Error when compiling: {exc.returncode, exc.output}")
        except Exception as e:
            logging.debug(f"[CompilationWrapper(GCC: compile)] Unknown Error when compiling: {e}")


        ## if file exists, do these next few lines, else return error that the compilation failed
        compliation_dict = {
            "CompiledFileLocation": "placeholder",
            "OtherData": "OtherDataPlaceholder"
        }

        return compliation_dict

    def safe_to_compile(self) -> bool:
        """ Runs a series of checks to make sure all inputs are correct, if so, it returns true"""
        logging.debug(f"[CompilationWrapper(GCC: safe_to_compile)] Checking filepath")
        if not self.filecheck(self.codefile):
            return False

        logging.debug(f"[CompilationWrapper(GCC: safe_to_compile)] Checking directory path")
        if not self.pathcheck(self.savefile):
            return False

        ## if all pass, return true
        return True

    def format_compile_command(self) -> str:
        flags = ""
        flags = self.flag_formatter()

        ## Very open to vulns... needs some saftey checks, around flags & cmd injection too
        ## the outputdir arg dumps everything into a directory
        nuitka_command = f"python -m nuitka {self.codefile} -output-dir={self.savefile} " \
                         f"--output-filename={self.savefile_name} --onefile {flags} --remove-output"
        logging.debug(f"[CompilationWrapper(GCC: format_compile_command)] Formatted Command: {nuitka_command}")
        return nuitka_command

    def flag_formatter(self):
        """A formatter specifically for flags. Note, flags are passed as their own
        string from the calling function, so this will not affect any other part of the command.
        """
        flag_list = ""

        try:
            for flag in self.flags:
                flag_list += f" {flag}"
            logging.debug(f"[CompilationWrapper(GCC: flag_formatter)] Flags successfully extracted & formatted: {flag_list}")
        except Exception as e:
            logging.debug(f"[CompilationWrapper(GCC: flag_formatter)] Error: {e}")

        return flag_list

    def filecheck(self, filepath: str) -> bool:
        if os.path.isfile(filepath):
            logging.debug(f"[CompilationWrapper(GCC: filecheck)] '{filepath}' exists!")
            return True
        else:
            logging.debug(f"[CompilationWrapper(GCC: filecheck)] '{filepath}' does not exist, or is not a file.")
            return False
    def pathcheck(self, filepath: str) -> bool:
        """ For checking if the path of the outputed file exists before outputting it"""
        if os.path.exists(filepath):
            logging.debug(f"[CompilationWrapper(GCC: pathcheck)] '{filepath}' exists!")
            return True
        else:
            logging.debug(f"[CompilationWrapper(GCC: pathcheck)] '{filepath}' does not exist")
            return False
'''
NTKA = NuitkaWrapper(codefile="/home/kali/PycharmProjects/logec-suite/agent/python/client.py",
                 savefile="/home/kali/PycharmProjects/logec-suite/agent/compiled/",
                 savefile_name="python_test_compile_client",
                 #flags=["-Wall", "-Ofast"]
                 )
NTKA.compile_framework()'''