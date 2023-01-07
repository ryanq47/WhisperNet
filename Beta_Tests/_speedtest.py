import speedtest  
  
  
st = speedtest.Speedtest()

  
def download():
  
    print((st.download())/1000000)  
  
def upload():
  
    print(st.upload()/1000000)  
  
def ping():
  
    servernames =[]  
  
    st.get_servers(servernames)  
  
    print(st.results.ping)  
  
