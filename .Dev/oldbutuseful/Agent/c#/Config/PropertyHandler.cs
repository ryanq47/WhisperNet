
using System.Net;

namespace Client.PropertyHandler
{

    //handles things like createing a client ID & such. Each accessible method should reutrn a value of some sort


    class Properties
    /* The initial properties for the client. Generated once on program start, call via GenerateData method.
     */

    {
        //Variables
        public static string ID = "";
        public static int msWait = 15000;


        public static void GenerateData()
        /* Calls all the functions, and sets the values needed for other componenets */
        {
            ID = Identifier();
        }

        private static string Identifier()
        /* Generates a 6 character ID for the client */
        {
            // new random class
            Random rand = new Random();

            //init variables
            int stringlen = rand.Next(6, 6);
            int randValue;

            string id = "";
            char letter;

            //generate ID
            for (int i = 0; i < stringlen; i++)
            {
                // Generating a random num from 0-26
                randValue = rand.Next(0, 26);

                //annnnd converting it to text/char
                letter = Convert.ToChar(randValue + 65);

                //appending to id
                id = id + letter;
            }

            //last but not least, setting the value. Could also be a return
            //ID = id;
            return id;


        }


    }

}