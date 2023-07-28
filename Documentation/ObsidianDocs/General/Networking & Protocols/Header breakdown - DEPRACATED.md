
    This function parses the header, and returns values
    might need to add some bits to the header to make the length longer for large files
	Yes I could do this on a bit level as well, as that's what it's imitating, but this way I can include other characters such as the aplphabet for expanded options. 

    header: 
    XXXXXXXXX

    1XXXXXXXX
    Let the server know what type of data is being sent:
        0: Cleartext
        1: RSA-Encryption (256 maybe)
        2-9: To be figured out later

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