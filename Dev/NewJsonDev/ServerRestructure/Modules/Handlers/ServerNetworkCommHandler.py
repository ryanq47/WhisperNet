################
## Communication Handler, this is the most up-to-date version
################ 
try:            
    import logging
    import socket
    import math

    from Modules.DataHandlers.Encryption import Encryptor



except Exception as e:
    print(f"[ServerNetworkCommHandler.py] Import Error: {e}")
    exit()



tpk = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyAg+3HFtUrBD/yzyDvlF
kA4Q1edzEsuYq/Bb7p7O9t6+4v7bk+o9+bo+7d10pmjHralTQNjihsOxdtHI8aXv
a/ePVIZO6Dj1h00006wX0gjXsoZGFQZ81ATsV5IxYXedw2zqF5FqjDyaQJP48TOb
u8MTogkA3w7QNhruxbzViL5YCCJG25aVUMQBtZmW/TpbjpleKIMxGYcXS1J0hqh9
M2k3eOHK75xi1MIJyW35VLqhUPvcI3vCIxLpKnax0b4HM1iJzyErUlf9bEM0Xku9
och4e/tM22zZXNRmmG50/GUcuJrb1GhmDRdVtRN7FDZ2Akyp062RfBK2zqNqB6id
bQIDAQAB
-----END PUBLIC KEY-----"""



def send_msg(conn=None, msg="", public_key=None, encryption=True):
    HEADER_BYTES = 10
    BUFFER = 1024

    # Handling wrong types of MSG

    #Bytes to str
    if type(msg) is bytes:
        msg = bytes_decode(msg)
    
    #anything else to str
    if not type(msg) is str:
        msg = str(msg)

    ## Encryption here
    if not encryption:
        msg = msg
    else:
        #msg = Encryptor.rsa_encrypt(public_key, msg)
        msg = Encryptor.rsa_encrypt(tpk.encode(), msg)
    

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
    #print(len(private_key))
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
    server_public_request = header_dict["server_public_request"]

    ## PubKey Requests,move to function when more options are introduced.
    # Only returns this value, doesn't actually do anything else. Basically just telling the code taht called this that
    # someone requested a pubkey. That code needs to call a send msg back to said caller
    if int(server_public_request) == 1:
        return "PUBKEY_REQUEST"

    
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
        Encryptor.rsa_decrypt(encrypted_data=msg, private_key=private_key)
        return complete_msg
    else:
        return complete_msg
    

    #return complete_msg


def _header_parse(header):
    '''
    This function parses the header, and returns values

    header: 
    XXXXXXXXX

    1XXXXXXXX
    Let the server know what type of data is being sent:
        0: Cleartext
        1: RSA-Encryption

    X1XXXXXXX
    Request public items from the server:
        1: Public Key
        2-9: reserved

    XX0000000
    The rest are for data size (char 2 - 9)
    '''
    print(header)

    encrypted = header[0]
    server_public_request = header[1]
    data_size = header[2:9]

    results = {
        "encrypted":encrypted,
        "server_public_request":server_public_request,
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