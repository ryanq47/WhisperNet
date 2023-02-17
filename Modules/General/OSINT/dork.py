## Specifically using '' instead of "" for google dorking
## Doc: https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06
from PySide6.QtCore import QRunnable, Qt, QThreadPool, QObject, QThread, Signal


class Dork(QObject):
    finished = Signal()
    #progress = 
    dork_query = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def dork_framework(self, dork_list):
        ## Dork List = ["searchterm", "Keyword","SiteURL","FileType","InTitle"]
        Searchterm = dork_list[0]
        Keyword = dork_list[1]
        SiteUrl = dork_list[2]
        FileType = dork_list[3]

        ## Send off to functions to format based on the list above, have them return the formatted strings
        #( I realize these could all probaly be lamdbas)
        ## Append all to an output and emit back the output


        dork_query = (
            f"{Searchterm} "
            f"{self.keyword(Keyword)}"
            f"{self.siteurl(SiteUrl)}"
            f"{self.filetype(FileType)}"
        )
        
        #print(dork_query)
        self.dork_query.emit(dork_query)
        #self.finished.emit()
    
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
            output = ''

            for i in FileType.split(" "):
                output += f'"{i}" '

            return f'filetype:{output} '

#D = Dork()
#D.dork_framework(["Keyword","","Nothing"])