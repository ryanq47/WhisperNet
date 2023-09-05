import requests

with open("C:\\test.exe", 'rb') as fe:
    file = fe.read()

    response = requests.post(
        '{}/files/safe.exe'.format("http://127.0.0.1:5000"), data=file
    )