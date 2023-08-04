using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Client.Comms
{
    internal class MessageHandler
    {
        //NOT USED CURRENTLY
        //Definitions here for decoding N stuff based on header values
        //ex:

        //Header Values, see docs, or bottom of this CS file for more details
        
        //encryption
        //const int AES256 = 1;

        //Request From Server
        //const int PUBKEY = 1;

        //ICC (Interclient communication)
        // END NOT USED CURRENTLY


        static public void Test()
        {
            Console.WriteLine("\tClient.Comms.NetworkingHandler checking in");
        }
        static public string RecvMessage(Socket conn)
        {
            try
            {
                // Receive the 4-byte header containing the message length
                byte[] header = new byte[4];
                conn.Receive(header);

                // Unpack the header to get the message length as an integer
                int msgLength = BitConverter.ToInt32(header, 0);

                // Initialize an empty buffer to store the received message
                byte[] receivedData = new byte[msgLength];

                // Loop until all data is received
                int totalReceived = 0;
                while (totalReceived < msgLength)
                {
                    // Receive the remaining data (adjust buffer size as needed)
                    int bufferLength = Math.Min(msgLength - totalReceived, 4096);
                    int received = conn.Receive(receivedData, totalReceived, bufferLength, SocketFlags.None);

                    if (received == 0)
                    {
                        // Connection closed prematurely, handle error or connection closure here
                        //throw new ConnectionException("Connection closed prematurely");
                        Console.WriteLine("Connection closed prematurely");
                    }

                    totalReceived += received;
                }

                // Convert the received data to a string (assuming UTF-8 encoding)
                string message = Encoding.UTF8.GetString(receivedData);

                Console.WriteLine($"[C2Server] Received message of length: {msgLength}");
                Console.WriteLine($"MSG from receive side {message}");
                return message;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[C2Server] Error receiving message: {ex.Message}");
                // Handle any appropriate error response or connection closure here
                throw;
            }
        }

        static public void SendMessage(string _msg, Socket conn)
        {

            //placeholder:
            //string msg = "{\"general\":{\"action\":\"!_clientlogin_!\",\"client_id\":\"ABC123\",\"client_type\":\"default string\",\"password\":\"default string\"},\"conn\":{\"client_ip\":\"Client IP\",\"client_port\":\"Client Port\"},\"msg\":{\"msg_to\":\"Client IP\",\"msg_content\":\"content\",\"msg_command\":\"content\",\"msg_value\":\"content\",\"msg_length\":\"1234\",\"msg_hash\":\"fakehash\"},\"stats\":{\"latest_checkin\":\"tomorrow\",\"device_hostname\":\"ttest.microsoft.com\",\"device_username\":\"1234\"},\"security\":{\"client_hash\":\"hash\",\"server_hash\":\"hash\"},\"test\":\"Hello World\"}";


            try
            {
                // Ensure the message is encoded as bytes
                byte[] data = Encoding.UTF8.GetBytes(_msg);

                // Get the length of the message in bytes
                int msgLength = data.Length;

                // Create a 4-byte header for the message length
                byte[] header = BitConverter.GetBytes(msgLength);

                // Send the header followed by the message
                conn.Send(header);
                conn.Send(data);

                Console.WriteLine($"[C2Server] Sent message of length: {msgLength}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[C2Server] Error sending message: {ex.Message}");
                // Handle any appropriate error response or connection closure here
                throw;
            }
        }

    }
}


/* For reference, from the docs

header: (10 chars, or 10 ints)
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

*/