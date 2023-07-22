################
## Encryption Module
################ 

#https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python


## need to replace with the new cryptography module
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding
#from cryptography.hazmat.primitives import serialization #for loading pemfiles
class Encryptor:

    def __init__(self, key_length=2048):
        self.key_length = key_length

        self.private_key_object = None
        self.private_key = ""
        self.public_key = ""

        # type checks
        if not type(self.key_length) is int:
            raise Exception(f"Object {object} is not an int.")

        if key_length <= 512:
            print("Keylength too small, auto-setting to 2048")
            self.key_length = 2048

    def generate_keys(self):
        '''
        sets private & public key to this instance
        '''
        # key =

        # docs for this: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

        # Creating a private key object if needed for other items later.
        self.private_key_object = rsa.generate_private_key(public_exponent=65537, key_size=self.key_length)\

        # mouthful, but there are a lot of good options here.
        self.private_key = self.private_key_object.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),

        )

        # creating the public key here. Not doing a public_key_object at the moment, not needed.
        self.public_key = self.private_key_object.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        #print(self.private_key)
        #print(self.public_key)

    @staticmethod
    def rsa_encrypt(data_to_encrypt="blamk_data", receiver_public_key=None) -> bytes:
        """
        data_to_encrypt (str OR bytes): The message to encrypt, will convert to bytes if passed as a string by accident
        receiver_public_key (str): The public key that will be used to encrypt the message

        returns (byte): encrypted text
        """
        ## Byte Check
        if type(data_to_encrypt) != bytes:
            print(f"Warning: data_to_encrypt recieved by rsa_encrypt as {type(data_to_encrypt)}. " \
            "Don't worry, I got you covered. Converting data_to_encrypt to a str, then encoding to bytes.")
            data_to_encrypt = str(data_to_encrypt).encode()

        if receiver_public_key == None:
            print("receiver_public_key is None, a value was probably not passed to it")
        
        if not type(receiver_public_key) is bytes:
            print("receiver_public_key not in byte form, turning it into bytes")
            receiver_public_key = receiver_public_key.encode()
            #raise Exception(f"Object {object} is not an int.")

        try:

            ## serialize key object from receiver_public_key
            local_pub_key = serialization.load_pem_public_key(
                data=receiver_public_key
            )

            print(local_pub_key)

            '''encrypted_text = local_pub_key.encrypt(
                data_to_encrypt,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )'''
            encrypted_text = local_pub_key.encrypt(
                "data_to_encrypt".encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            ## this error is not from here: ERRMSG: 'bytes' object has no attribute 'encode'
            #print(encrypted_text)
            return encrypted_text

        except Exception as e:
            import sys, os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return "placeholder encryptd msg - if you see this, an error occured"

    @staticmethod
    def rsa_decrypt(encrypted_data: bytes = "", private_key=None) -> str:
        """        
        encrypted_data (Bytes): The message to decrypt

        returns (str): decrypted text

        """
        if type(encrypted_data) != bytes:
            print(f"Warning: Messsage recieved by function as {type(encrypted_data)}. Should be bytes")

        ## serialize key object from receiver_public_key
        local_private_key = serialization.load_pem_private_key(
            private_key,
            password=None
        )

        decrypted_text = local_private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return decrypted_text.decode()

'''
## Jank Unit Test. Should print Private & Public Keys, and the Encrypted & Decrypted messages
E = Encryptor(key_length=512)
E.generate_keys()

aaa = Encryptor.rsa_encrypt(data_to_encrypt="SuperSecretMessage", receiver_public_key=E.public_key)

zzz = Encryptor.rsa_decrypt(encrypted_data=aaa, private_key=E.private_key)


print(f"Encrypted Message: {aaa}\nDecrypted Message: {zzz}")'''


