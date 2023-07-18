using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Client.Comms
{
    internal class MessageHandler
    {

        //Definitions here for decoding N stuff based on header values
        //ex: AES256 = 1

        static public void Test()
        {
            Console.WriteLine("\tClient.Comms.NetworkingHandler checking in");
        }
        static public string RecvMessage(Socket conn)
        {
            //takes socket, recieves a message, does actions based on header, returns (decoded/decrypted) msg
            return "RecvMsh";

        }

        static public void SendMessage(string msg, Socket conn)
        {
            //takes socket, and a msg, does actions on message based on args, sends a message, returns nothing

        }

    }
}
