## Written mostly by chatGPT, had to make a few changes to the datetime items

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta

def ssl_gen(save_file_path = None):
    # do later
    #if not keycheck():
        #print("Keys not regening")
        
        ##not returning anything, just getting out of the script
        #return

    key_file = f"{save_file_path}/server.key"
    crt_file = f"{save_file_path}/server.crt"


    try:
        ## Key check to see if keys exist

        # Generate a private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Serialize the private key to PEM format
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Save the private key to a file (server.key)
        with open(key_file, 'wb') as key_file:
            key_file.write(private_key_pem)

        # Generate a self-signed certificate
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, u'example.com')
        ])

        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.utcnow()
        ).not_valid_after(
            datetime.utcnow() + timedelta(days=365)
        ).sign(private_key, hashes.SHA256(), default_backend())

        # Serialize the self-signed certificate to PEM format
        cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)

        # Save the self-signed certificate to a file (server.crt)
        with open(crt_file, 'wb') as cert_file:
            cert_file.write(cert_pem)

        print("KeyGen.py: SSL Keys generated successfully")

    except Exception as e:
        print(f"CHANGEME KeyGen.py Error: {e}")
'''
def keycheck():
    ## key check logic
    regen_keys = input("Keys already exist, regenerate? (Y/n)")

    if regen_keys == "y":
        return True
    else:
        return False'''

if __name__ == "__main__":
    ssl_gen()