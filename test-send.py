import socket
import math
import json
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ("127.0.0.1", 6060)

try:
    server.connect(server_addr)
except ConnectionRefusedError:
    print("Connection Refused")
except Exception as e:
    print(f"Unkown Error: {e}")

### NOTES

## creating this test sender to test the initial msg to server


def send_msg_to_friendlyclient(msg:str):
    ## lazy fix to map self.conn to conn
    conn = server


    ## clients need to have a shared known header beforehand. Default is 10
    HEADER_BYTES = 10
    BUFFER = 1024

    ## get the length of the message in bytes
    msg_length = len(msg)

    ## create a header for the message that includes the length of the message
    header = str_encode(str(msg_length).zfill(HEADER_BYTES))#.encode()

    ## send the header followed by the message in chunks
    print(f"[Server (send_msg_to_friendlyclient: )] SENDING HEADER: {header}")
    try:
        conn.send(header)
    except BrokenPipeError as bpe:
        print(f"[Server (send_msg_to_friendlyclient: )] Broken pipe, friendly client most likely disconnected, or crashed, closing thread: {bpe}")
        ## kills thread, need to make a cleaner way to do this
        exit()

    except Exception as e:
        print(f"[Server (send_msg_to_friendlyclient: )] Error when sending message: {e}")

    chunks = math.ceil(msg_length/BUFFER)
    for i in range(0, chunks):
        try:
            ## gets the right spot in the message in a loop
            chunk = msg[i*BUFFER:(i+1)*BUFFER]
            print(f"[Server (send_msg_to_friendlyclient:)] SENDING CHUNK {i+1}/{chunks}")
            conn.send(str_encode(chunk))
        except Exception as e:
            print(f"[Server (send_msg_to_friendlyclient: )] error sending: {e}")


## str -> bytes
def str_encode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> bytes:
    for format in formats:
        try:
            return input.encode(format)
        except UnicodeEncodeError:
            print(f"Could not encode bytes to {format}")
        except Exception as e:
            print(f"ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    for format in formats:
        try:
            return input.decode(format)
            print(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            print(f"ERRMSG: {e}\n")


client_msg_to_be_sent = {
    "Main": {
        "general": {
            "action":"!_clientlogin_!",
            "client_id": "username or client_id",
            "client_type": "friendly or malicious"
        },
        "conn": {
            "client_ip": "127.0.0.1",
            "client_port": 6969
        },
        "msg": {
            "msg_to": "bob",
            "msg_content": "testmsg",
            "msg_length": 1234,
            "msg_hash": "hash of message (later)"
        },
        "stats": {
            "latest_checkin": "time.now",
            "device_hostname": "hostname",
            "device_username": "username"
        },
        "security": {
            "client_hash": "hash of client (later)",
            "server_hash": "hash of server (later)"
        }
    }
}
user_msg_to_be_sent = {
    "Main": {
        "general": {
            "action":"!_userlogin_!",
            "client_id": "TestUsername",
            "client_type": "friendly or malicious",
            "password":"1234"
        },
        "conn": {
            "client_ip": "127.0.0.1",
            "client_port": 6969
        },
        "msg": {
            "msg_to": "bob",
            "msg_content": "testmsg",
            "msg_length": 1234,
            "msg_hash": "hash of message (later)"
        },
        "stats": {
            "latest_checkin": "time.now",
            "device_hostname": "hostname",
            "device_username": "username"
        },
        "security": {
            "client_hash": "hash of client (later)",
            "server_hash": "hash of server (later)"
        }
    }
}
                            ##python dict -> str
#send_msg_to_friendlyclient(json.dumps(client_msg_to_be_sent))
#time.sleep(2)
send_msg_to_friendlyclient(json.dumps(user_msg_to_be_sent))