################
## Communication Handler, this is the most up-to-date version
################ 
try:            
    import logging
    import socket
    import math
    import struct

    #from Modules.DataHandlers.Encryption import Encryptor

except Exception as e:
    print(f"[ServerNetworkCommHandler.py] Import Error: {e}")
    exit()


## setting encryption to false by default
def send_msg(conn=None, msg="") -> None:
    """Sends a message on the socket connection passed to it. 

    Args:
        conn (Socket, required): The connection in which to send the message on. Defaults to None.
        msg (str, optional): The message you want to send. Defaults to "".

    Raises:
        e: _description_
    """
    try:
        msg = str_encode(msg)

        # Get the length of the message in bytes
        msg_length = len(msg)

        ## will be used later
        # Create a 4-byte header for the message length
        # Use 'I' format for unsigned integer (4 bytes)
        header = struct.pack('I', msg_length)

        # Send the header followed by the message
        conn.sendall(header + msg)

        logging.debug(f"[CommsHandler.receive_msg()] Sent message of length: {msg_length}")
    except Exception as e:
        logging.error(f"[Server (CommsHandler.py)] Error sending message: {e}")
        # Handle any appropriate error response or connection closure here
        raise e



def receive_msg(conn=None) -> str:
    """A message handler that recieves messages. It's a wrapper around socket.recv, and allows for easier error handling

    Args:
        conn (Socket, required): The connection in which to recieve the message on. Defaults to None.

    Raises:
        ConnectionError: _description_
        e: _description_

    Returns:
        str: The message that has been recieved
    """
    try:
        # Receive the 4-byte header containing the message length
        header = conn.recv(4)

        # Unpack the header to get the message length as an unsigned integer
        msg_length = struct.unpack('I', header)[0]

        # Initialize an empty buffer to store the received message
        received_data = b''

        # Loop until all data is received
        while len(received_data) < msg_length:
            # Receive the remaining data (adjust buffer size as needed)
            buffer_size = min(msg_length - len(received_data), 4096)
            data = conn.recv(buffer_size)
                
            if not data:
                # Connection closed prematurely, handle error or connection closure here
                raise ConnectionError("Connection closed prematurely")

            received_data += data

        # Convert the received data to a string
        message = bytes_decode(received_data)

        logging.debug(f"[CommsHandler.receive_msg()] Received message of length: {msg_length}")

        #print(f"MSG: ========== \n\n{message}\n\n==========")

        return message

    except Exception as e:
        logging.error(f"[CommsHandler.receive_msg()] Error receiving message: {e}")
            # Handle any appropriate error response or connection closure here
        raise e
    

# Currently not being used
def _header_parse(header) -> dict:
    '''
    This function parses the header, and returns values
    might need to add some bits to the header to make the length longer for large files

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

    XX1XXXXXX
    Interclient communication - reserved for later
        0: do not communicate with other clients
        1: Send to client (next hop kinda, need to figure out how to pass IP, maybe an extra json section)

    XXX0000000
    The rest are for data size (char 3 - 9)
    '''
    #print(header)

    
    encryption          = header[0]
    server_request      = header[1]
    client_passthrough  = header[2]
    data_size           = header[3:9]
    

    results = {
        "encryption":encryption,
        "server_request":server_request,
        "data_size":data_size
    }

    logging.debug(f"Header: {results}")
    return results
    


## str -> bytes
def str_encode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> bytes:
    '''for format in formats:
        try:
            return input.encode(format)
        except UnicodeEncodeError:
            logging.debug(f"Could not encode bytes to {format}")
        except Exception as e:
            logging.warning(f"CommsHandler (str_encode) ERRMSG: {e}\n")'''
    try:
        return input.encode("utf-8")
    except UnicodeEncodeError:
        logging.debug(f"Could not encode bytes to {format}")
    except Exception as e:
        logging.warning(f"CommsHandler (str_encode) ERRMSG: {e}\n")


## bytes -> str
def bytes_decode(input, formats=["utf-8", "iso-8859-1", "windows-1252", "ascii"]) -> str:
    for format in formats:
        try:
            return input.decode(format)
            logging.debug(f"Succesfully decoded bytes to {format}")
        except UnicodeEncodeError:
            logging.debug(f"Could not decode bytes to {format}")
        except Exception as e:
            logging.warning(f"CommsHandler (bytes_decode) ERRMSG: {e}\n")