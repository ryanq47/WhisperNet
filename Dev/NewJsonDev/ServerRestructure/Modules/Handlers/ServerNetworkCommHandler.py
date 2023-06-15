################
## Communication Handler
################ 
try:            
    import logging
    import socket
    import math

except Exception as e:
    print(f"[ServerNetworkCommHandler.py] Import Error: {e}")
    exit()

def send_msg(conn=None, msg="", public_key=None, encryption=True):
    HEADER_BYTES = 10
    BUFFER = 1024

    ## Encryption here
    '''
    if not encryption
        msg = msg
    
    else:
        msg = encryption(pubkey, msg)
    '''

    msg_length = len(msg)
    header = str_encode(str(msg_length).zfill(HEADER_BYTES))  # .encode()

    logging.debug(f"[ServerNetworkCommHandler (send_msg] SENDING HEADER: {header}")
    ## header is unencrypted. Not sure how to really get around this, but that's okay for now
    conn.send(header)
    chunks = math.ceil(msg_length / BUFFER)

    for i in range(0, chunks):
        try:
            ## gets the right spot in the message in a loop
            chunk = msg[i * BUFFER:(i + 1) * BUFFER]
            logging.debug(f"[ServerNetworkCommHandler (send_msg)] SENDING CHUNK {i + 1}/{chunks}")
            conn.send(str_encode(chunk))
        except Exception as e:
            logging.debug(f"[ServerNetworkCommHandler (send_msg)] error sending: {e}")



def receive_msg(conn=None, private_key="") -> str:
    ## clients need to have a shared known header beforehand. Default is 10
    HEADER_BYTES = 10
    BUFFER = 1024
    msg_bytes_recieved_so_far = 0
    logging.debug(f"[ServerNetworkCommHandler (recieve_msg_global)] WAITING ON HEADER TO BE SENT:")
    
    
    #header_msg_length = conn.recv(HEADER_BYTES).decode()  # int(bytes_decode(msg)
    header = conn.recv(HEADER_BYTES).decode()
    ## getting the amount of chunks/iterations eneded at 1024 bytes a message

    header_dict = _header_parse(header)
    ## temp placeholder. will be returned from _header_parse
    msg_encrypted = header_dict["encrypted"]
    msg_length = header_dict["data_size"]

    ## Need a type check & error handle maybe? could be a ticking time bomb
    chunks = math.ceil(int(msg_length) / BUFFER)
    complete_msg = ""  # bytes_decode(msg)[10:]
    for i in range(0, chunks):
        logging.debug(
            f"[ServerNetworkCommHandler(recieve_msg_global)] WAITING TO RECEIEVE CHUNK {i + 1}/{chunks}:")
        msg = conn.recv(BUFFER)  # << adjustble, how many bytes you want to get per iteration
        ## getting the amount of bytes sent so far
        msg_bytes_recieved_so_far = msg_bytes_recieved_so_far + len(bytes_decode(msg))
        complete_msg += bytes_decode(msg)

        ## if complete_msg is the same length as what the headers says, consider it complete.
        if len(complete_msg) == msg_length:
            logging.debug(f"[ServerNetworkCommHandler (recieve_msg_global)] MSG TRANSFER COMPLETE")

    ## decryption here
    
    if msg_encrypted == 1:
        print("decrypt")
        return complete_msg
    else:
        return complete_msg
    

    #return complete_msg


def _header_parse(header):
    '''
    This function parses the header, and returns values

    header: 
    0000000000
    1st value: (char 0): Encrypted (1) or NotEncrypted(0)
    The rest are for data size (char 1 - 9)
    '''
    print(header)

    encrypted = header[0]
    data_size = header[1:9]

    results = {
        "encrypted":encrypted,
        "data_size":data_size
    }


    logging.debug(f"Header: {results}")
    return results

## str -> bytes
def str_encode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> bytes:
    for format in formats:
        try:
            return input.encode(format)
        except UnicodeEncodeError:
            logging.debug(f"Could not encode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    for format in formats:
        try:
            return input.decode(format)
            logging.debug(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            logging.warning(f"ERRMSG: {e}\n")