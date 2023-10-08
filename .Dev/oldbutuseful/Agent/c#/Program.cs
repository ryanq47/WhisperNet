using Client.Comms;
using System.Net.Sockets;
using System.Net;
using System.Reflection;

namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            // Generate relevant data
            Client.PropertyHandler.Properties.GenerateData();
            //^^ Note, have this generare the first time json checkin string

            // Sample IP and port
            string ipString = "127.0.0.1";
            int port = 80;

            // Create IP address
            IPAddress ipAddr = NetOps.CreateIPObject(ipString);

            // Create endpoint - aka where we are connecting to
            IPEndPoint serverEndPoint = NetOps.CreateEndpoint(ipAddr, port);


            // ConnectToServer(serverEndPoint);
            ConnectToServer(serverEndPoint);
        }

        static void ConnectToServer(IPEndPoint serverEndPoint)
        {
            int iterTrack = 0;
            string decisionTreeResults = "";

            while (true)
            {
                try
                {
                    //Create socket - has to be down here
                    Socket clientSocket = NetOps.CreateSocket();

                    //connect to server
                    clientSocket.Connect(serverEndPoint);

                    //Send Heartbeat/Check in/ send previous results & ask for new job
                    //change _msg to msg when implmenting JSON for real
                    if (iterTrack == 0)
                    {
                        // first iteration, send the dedicated checkin json string, or some permutation of it
                        string initJson = Client.Comms.JsonHandler.ToJson(CID: Client.PropertyHandler.Properties.ID);
                        MessageHandler.SendMessage(_msg: initJson, conn: clientSocket);
                    }

                    else
                    {
                        //taking PREVIOUs iterations results (which should be a JSON string), and sending it back
                        Console.WriteLine($"Results from previouys iter: {decisionTreeResults}");
                        MessageHandler.SendMessage(_msg: decisionTreeResults, conn: clientSocket);
                    }


                    // Recieve Job/Message from server
                    string stringRecv = Comms.MessageHandler.RecvMessage(clientSocket);

                    //unpack Job/Message
                    //note, the JsonStruct.MyJsonStruct is just the object that is returned. can access items viea serverMsg.Whatever
                    JsonStruct.MyJsonStruct serverMsg = Client.Comms.JsonHandler.FromJson(stringRecv);

                    //Console.WriteLine($"From Main: {serverMsg.msg.msg_command}");

                    //Process Job/Decision Tree
                    //decision tree returns json string from result of action. This could cause some issues in the future with adding dtaa to the the stirng, but is fine for now
                    decisionTreeResults = Client.Logic.Trees.decisionTree(serverMsg);

                    //client disconnect -  true means the socket can be reused
                    //!! Socket errors here, need to figure this out
                    /*
                     * Close: Rapidly closes socket -  may lose some data
                     * Disconenct: Tries to shutdown safetly.
                     */
                    clientSocket.Close();
                    //(sends results on next checkin)

                    iterTrack++;
                }

                catch (Exception e)
                {
                    Console.WriteLine($"DEBUG: Error (ConnectToServer): {e}");
                }

            //sleep till next check in
            Thread.Sleep(Client.PropertyHandler.Properties.msWait);

            }

        }

    }

    // These are all mission-critical functions. They throw exceptions on errors.
    class NetOps
    {
        public static Socket CreateSocket()
        {
            try
            {
                Socket clientSock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                return clientSock;
            }
            catch (Exception e)
            {
                Console.WriteLine($"[Client.NetOps.CreateSocket] Error: {e}");
                throw; // Rethrow the exception to handle it at a higher level
            }
        }

        public static IPEndPoint CreateEndpoint(IPAddress ipAddr, int port)
        {
            try
            {
                IPEndPoint serverEndPoint = new IPEndPoint(ipAddr, port);
                return serverEndPoint;
            }
            catch (Exception e)
            {
                Console.WriteLine($"[Client.NetOps.CreateEndpoint] Error: {e}");
                throw; // Rethrow the exception to handle it at a higher level
            }
        }

        public static IPAddress CreateIPObject(string ipString)
        {
            try
            {
                var ipAddr = IPAddress.Parse(ipString);
                return ipAddr;
            }
            catch (Exception e)
            {
                Console.WriteLine($"[Client.NetOps.CreateIPObject] Error: {e}");
                throw; // Rethrow the exception to handle it at a higher level
            }
        }
    }
}
