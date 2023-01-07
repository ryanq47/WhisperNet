import base64
# note, all these are run via CMD, so you need to put powershell b4 the command for PS commands to work

class target:
    def hostname():
        cmd = "hostname"
        return cmd
    
    def pub_ip():
        cmd_1 = "powershell $ip = Invoke-RestMethod http://ipinfo.io/json; $ip.ip"
        ## https://www.prajwaldesai.com/get-public-ip-address-using-powershell/
        ## random choose which way to resolve to keep anonymity
        
        # encoding, then formatting and returning b64 encoded command
        return cmd_1
    
    def os():
        cmd = "powershell (Get-WMIObject win32_operatingsystem).name"
        return cmd

        

'''
def encoder(plaintext):
    sample_string = plaintext
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    return base64_string
'''
def b64formatter(encoded):
    cmd = encoded
    return cmd