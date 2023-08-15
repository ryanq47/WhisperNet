
the 'libraries' provided by WhisperNet to interact with when creating plugins. This is my first time creating a 'plugin' style program, I'm trying my best here.


## Client.Comms
#### CommsHandler.py

| Functions         | Desc     | Input | Returns |
|--------------|-----------|-----------|-----------|
| send_msg | Sends a message using the provided socket. Handles the encoding for you. | msg (str), conn (socket) | None |
| receive_msg      | receive a message using the provided socket. Handles the decoding for you.  | conn (socket)| message (str)|
| connect_to_server      | Connects to a server (or any address you feed it) via IPV4. Returns a socket  | server_conn_tuple (tuple) <br> Ex: 127.0.0.1:80 | socket |
| str_encode      | Encodes a string in UTF-8 | input (str) <br> | Byte encoded string |
| str_decode      | Decodes a string from utf-8 to text | input (byte) <br> | String |

## Fill the rest in with ChatGPT