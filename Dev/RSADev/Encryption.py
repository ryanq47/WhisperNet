################
## Encryption Module
################ 

#https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python


class Encryptor():

    def __init__(self, key_length=2048):
        self.key_length = key_length
        self.public_key = ""
        self.private_key = ""

        ## type checks
        if not type(self.key_length) is int:
            raise Exception(f"Object {object} is not {intended_type}.")

    def generate_keys(self):
        '''
        sets private & public key to this instance
        '''
        key = RSA.generate(self.key_length)
        self.public_key = key.publickey().exportKey('PEM')
        self.private_key = key.export_key('PEM')

    def rsa_encrypt(self, message="", receiver_public_key="") -> bytes:
        """
        message (str OR bytes): The message to encrypt
        receiver_public_key (str): The public key that will be used to encrypt the message

        returns (byte): encrypted text
        """
        ## Byte Check
        if type(message) != bytes:
            print(f"Warning: Messsage recieved by function as {type(message)}. Converting to str, then bytes")
            message = str(message).encode()

        rsa_public_key = RSA.importKey(receiver_public_key)
        rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
        encrypted_text = rsa_public_key.encrypt(message)

        return encrypted_text

    def rsa_decrypt(self, message="") -> str:
        """        
        message (Bytes): The message to decrypt

        returns (str): decrypted text

        """
        if type(message) != bytes:
            print(f"Warning: Messsage recieved by function as {type(message)}. Should be bytes")

        rsa_private_key = RSA.importKey(self.private_key)
        rsa_private_key = PKCS1_OAEP.new(rsa_private_key)

        encrypted_text = message
        decrypted_text = rsa_private_key.decrypt(encrypted_text)

        print(decrypted_text.decode())
        return decrypted_text.decode()

'''
E = Encryptor(key_length=2048)
E.generate_keys()

aaa = E.rsa_encrypt(message="abcd1234", receiver_public_key=E.public_key)

zzz = E.rsa_decrypt(message=aaa)

print(aaa, zzz)'''


