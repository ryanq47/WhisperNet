#qthread backup
## doc https://12ft.io/proxy?&q=https%3A%2F%2Frealpython.com%2Fpython-pyqt-qthread
## got stuck with singals n passing data to the subclass (scan) - otherwise everything worked well

    ## Class placed here for organization 
        def portscan_qthread(self):
        self.thread = QThread()
        self.worker = MyApp.scan()
        ## Pointing thread at func/class
        self.worker.moveToThread(self.thread)
        ## queing func to be run
        self.thread.started.connect(self.worker.portscan)
    
    
    class scan(QObject):
        #ip = pyqtSignal(int)
        #def __init__(self):
            #print(self.ip)
        
        def portscan(self):
            import portscanner
            
            #print(self.ip)
            
            self.ip = MyApp.portscan_popup.portscan_IP
            print(self.ip)
            min_port = self._portscan_popup.portscan_minport.text()
            max_port = self._portscan_popup.portscan_maxport.text()
            extra_port = self._portscan_popup.portscan_extraport.text()
            
            if self._portscan_popup.portscan_standard_check:
                standard = True
                
            if self._portscan_popup.portscan_stealth_check:
                stealth = True
            
            ## if clicked standard = true
            target_list = [ip, int(min_port), int(max_port), extra_port]
            scantype_list = [standard, stealth]
            
            portscanner.event_loop(target_list, scantype_list)