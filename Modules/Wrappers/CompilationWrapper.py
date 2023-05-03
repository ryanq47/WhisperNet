## A wrapper for GCC, and other compilation things for logec. Each wrapper uses it's own class. Classes are not
## static as you can't thread them with qt then (afaik...)

from PySide6.QtCore import Signal, QObject

## waiting to include QObject, inorder to test these functions standalone
class GccWrapper:
    Error = Signal(str)
    Success = Signal(str)
    def __init__(self):
        pass
        #self.savefile
        #self.name
        #self.flags


    def compile(self):
        pass
        ## subprocess run gcc with options

        """
        if no errors and sanity_check.file_exists?():
            self.Success.emit(f"{fiellocation}, {filename}")
        
        else:
            self.Error.emit("Failed: {error_msg}")
        """