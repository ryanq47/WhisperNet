#Shell
from PySide6.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, Signal
import subprocess


class Shell(QObject):
    sys_out = Signal(str)
    finished = Signal()
    
    def shell_framework(self, input_list):
        ## Getting User Input:
        print("IN FUNC")
        print(input_list[0])
        raw_user_input = input_list[0]
        
        filtered_user_input = self.input_filter(raw_user_input)
        
        try:
            raw_output = subprocess.check_output(filtered_user_input, shell=True, stderr=subprocess.STDOUT)
            output = raw_output.decode("utf-8")
            
        except subprocess.CalledProcessError as error:
            output = error.output.decode("utf-8")
            
        
        self.sys_out.emit(output)
        #self.finished.emit() 
        
    
    def input_filter(self, user_input):
        
        if user_input == "exit":
            pass
            #Exit
            
        else:
            filtered_input = user_input
            return filtered_input
        
        