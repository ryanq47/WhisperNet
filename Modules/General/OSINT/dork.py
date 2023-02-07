from PyQt5.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, pyqtSignal


class Dork(QObject):
    finished = pyqtSignal()
    #progress = pyqtSignal(int)
    dork_query = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def dork_framework(self, dork_list):
        ## Dork List = ["Keyword","SiteURL","FileType","InTitle"]
        Keyword = dork_list[0]
        SiteUrl = dork_list[1]

        ## Send off to functions to format based on the list above, have them return the formatted strings
        #( I realize these could all probaly be lamdbas)
        ## Append all to an output and emit back the output


        dork_query = (
            f"{self.keyword(Keyword)}"
            f"{self.siteurl(SiteUrl)}"
        )
        
        #print(dork_query)
        self.dork_query.emit(dork_query)
    
    def keyword(self, Keyword):

        output = f'intext:"{Keyword}" '

        return output
    
    def siteurl(self, SiteUrl):
        if SiteUrl == "":
            return ""

        else:
            output = f'site:"{SiteUrl}" '

            return output        
    
    def filetype(self, FileType):
        if FileType == "":
            return ""
        
        else:
            preprocess_list = []

            for i in FileType.strip():
                preprocess_list.append(i)

            output = f'filetype:"{FileType}" '

#D = Dork()
#D.dork_framework(["Keyword","","Nothing"])