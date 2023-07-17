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

        //Definitions here for decoding N stuff based on header values
        //ex:

        //Header Values, see docs, or bottom of this CS file for more details
        
        //encryption
        const int AES256 = 1;

        //Request From Server
        const int PUBKEY = 1;

        //ICC (Interclient communication)



        static public void Test()
        {
            Console.WriteLine("\tClient.Comms.NetworkingHandler checking in");
        }
        static public string RecvMessage(Socket conn)
        {
            //takes socket, recieves a message, does actions based on header, returns (decoded/decrypted) msg

            const int HEADER_BYTES  = 10;
            const int BUFFER        = 1024;
            byte[] headerBytes      = new byte[HEADER_BYTES];

            string completeMsg      = "EMPTY";
            int msgBytesReceivedSoFar = 0;

            //if the try does fail, these exist as defaults

            string headerMsgLength  = "00000001"; //really low default
            string ENCRYPTION       = "0"; //default no encryption
            string SERVREQ          = "0"; //requesting nothing from server
            string ICC              = "0"; //sending nothing to peers/no inter client communication


            // Console.WriteLine("WAITING ON HEADER TO BE SENT:");
            //Getting header
            conn.Receive(headerBytes);

            //header starts as a string so certain values can be pulled from it
            string HEADER = Encoding.UTF8.GetString(headerBytes); //int(bytes_decode(msg)
            //Console.WriteLine("HEADER:" + headerMsgLength);

            //this can easily fail if the header is sent wrong, or something weird tries to talk to the client
            try
            {
                headerMsgLength = HEADER.Substring(2, 9);

            }

            catch {
                Console.WriteLine("Debug: Error at try/except on Client.Comms.NetworkingHandler: RecvMessag ");

            }

            //deciding how many chunks to listen for.
            //UPDATE ME TO THE NEW HEADER BREADKWON STANDARD
            int chunks = (int)Math.Ceiling((double)int.Parse(headerMsgLength) / BUFFER);

            for (int i = 0; i < chunks; i++)
            {
                //Console.WriteLine("RECEIVING CHUNK:");
                byte[] msgBytes = new byte[BUFFER];
                int bytesReceived = conn.Receive(msgBytes);  // << adjustable, how many bytes you want to get per iteration

                // getting the amount of bytes sent so far
                msgBytesReceivedSoFar += bytesReceived;

                //byes to str, may need to adjust for encryption/decryption, as those may take bytes
                string msg = Encoding.UTF8.GetString(msgBytes, 0, bytesReceived);
                completeMsg += msg;

            }

            //header processing.
            /*
            
            ENCRYPTION = HEADER[0] //first byte in header (may be off, just an eample)

            if ENCRYPTION = AES256 {
                str decrypted = Client.Comms.CryptoHandler.Aes256Decrypt(key=whatever);
                return decrypted;
            }

            */

            //Weird spacing, I know. Trying it to see if it's easier to read
            ENCRYPTION      = HEADER.Substring(0);
            SERVREQ         = HEADER.Substring(1);
            ICC             = HEADER.Substring(2);



            return "RecvMsg";

        }

        static public void SendMessage(string msg, Socket conn)
        {
            //takes socket, and a msg, does actions on message based on args, sends a message, returns nothing
            const int HEADER_BYTES  = 10;
            const int BUFFER        = 1024;

            // get the length of the message in bytes
            int msg_length = Encoding.UTF8.GetByteCount(msg);

            //!! Note, will need to rework to add in the encrpytion & other bytes N stuff
            // create a header for the message that includes the length of the message
            string header = msg_length.ToString().PadLeft(HEADER_BYTES, '0');
            byte[] headerBytes = Encoding.UTF8.GetBytes(header);

            // send the header followed by the message in chunks
            Console.WriteLine($"SENDING HEADER: {header}");
            conn.Send(headerBytes);

            //send rest of message
            for (int i = 0; i < Math.Ceiling((double)msg_length / BUFFER); i++)
            {
                // gets the right spot in the message in a loop
                int startIdx = i * BUFFER;
                int endIdx = Math.Min(startIdx + BUFFER, msg_length);
                byte[] chunkBytes = Encoding.UTF8.GetBytes(msg.Substring(startIdx, endIdx - startIdx));
                Console.WriteLine($"SENDING CHUNK: {msg.Substring(startIdx, endIdx - startIdx)}");
                conn.Send(chunkBytes);
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