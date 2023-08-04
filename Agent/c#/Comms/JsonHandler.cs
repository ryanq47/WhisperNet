using System;
using System.Collections.Generic;
using System.Management.Automation;
using JsonStruct;
using Newtonsoft.Json;

using static JsonStruct.MyJsonStruct;


namespace Client.Comms
{
    //using internal so only the assmbly can access it. Might need to tighten down later
    internal static class JsonHandler
    {
        //serves as a test only
        internal static void Test()
        {
            Console.WriteLine("\tJsonHandler.CS: Success.");
        }

        //takes args of data to turn into json
        /// <summary>
        /// This method converts items into a json string. There are a ton of inputs, as seen above. All of these are optional. 
        /// </summary>

        /// <returns>A JSON string representing the provided parameters.</returns>
        internal static string ToJson(
            //generalinfo
            string Action = "!_clientlogin_!", string CID = "default string", string CTYPE = "default string", string Password = "default string",
            //conninfo
            string clientIP = "127.0.0.1", string clientPort = "8080", //And so on, fill the rest out
            //msginfo
            string msgTo = "clientIP", string msgContent = "msgContent", string msgCommand = "Command", string msgValue = "msgValue", string msgLength = "length", string msgHash = "fakehash",
            //statsinfo
            string latestCheckin = "", string deviceHostname = "", string deviceUsername = "",
            //secinfo
            string clientHash = "fakehash", string serverHash = "fakehash"
            )
        {

            JsonStruct.MyJsonStruct mystruct = new JsonStruct.MyJsonStruct
            {
                test = "Hello World",

                //need to do some reasearch as to why I'm still declaring a new instance of general here & in MyJsonStruct
                general = new JsonStruct.MyJsonStruct.generalinfo
                {
                    action = Action,
                    client_id = CID,
                    client_type = CTYPE,
                    password = Password
                },
                conn = new JsonStruct.MyJsonStruct.conninfo
                {
                    client_ip = clientIP,
                    client_port = clientPort
                },

                msg = new JsonStruct.MyJsonStruct.msginfo
                {
                    msg_to = msgTo,
                    msg_content = msgContent,
                    msg_command = msgCommand,
                    msg_value = msgValue,
                    
                    msg_length = msgLength,
                    msg_hash = msgHash
                },

                stats = new JsonStruct.MyJsonStruct.statsinfo
                {
                    latest_checkin = latestCheckin,
                    device_hostname = deviceHostname,
                    device_username = deviceUsername,

                },

                security = new JsonStruct.MyJsonStruct.securityinfo
                {
                    client_hash = clientHash,
                    server_hash = serverHash,

                },


            };

            //convert TO json
            string jsonString = JsonConvert.SerializeObject(mystruct);
            //Console.WriteLine(jsonString);

            return jsonString;
        }

        /// <summary>
        /// Takes JSON String, returns JSON Object.
        /// </summary>
        internal static JsonStruct.MyJsonStruct FromJson(string JsonString = "string")
        {

            //I think this creates a default json type/struct - need to test what it does on fail.
            //string TestJsonString = "{\"general\":{\"action\":\"default string\",\"client_id\":\"default string\",\"client_type\":\"default string\",\"password\":\"default string\"},\"conn\":{\"client_ip\":\"Client IP\",\"client_port\":\"Client Port\"},\"msg\":{\"msg_to\":\"Client IP\",\"msg_content\":\"content\",\"msg_cmd\":\"content\",\"msg_value\":\"content\",\"msg_length\":\"1234\",\"msg_hash\":\"fakehash\"},\"stats\":{\"latest_checkin\":\"tomorrow\",\"device_hostname\":\"ttest.microsoft.com\",\"device_username\":\"1234\"},\"security\":{\"client_hash\":\"hash\",\"server_hash\":\"hash\"},\"test\":\"Hello World\"}";
            //Console.WriteLine(JsonString);

            //THIS fixes it, takes trailing and leading [] chars
            string TrimmedJsonString = JsonString.Trim().Trim('[', ']');
            //Long story short, [] were being added to the Json string, and this would error out. This fixes it, but may cause issues later with certain commands if ever needed
            //string NewJsonString = JsonString.Replace("]", "").Replace("[", "");


            //JsonStruct.MyJsonStruct mystruct = JsonConvert.DeserializeObject<JsonStruct.MyJsonStruct>(JsonString);
            var jsonObject = JsonConvert.DeserializeObject<JsonStruct.MyJsonStruct>(TrimmedJsonString);
            Console.WriteLine(jsonObject.msg.msg_to);
            return jsonObject;


        }
    }
}


    //json structure - note, the json naming does not follow PascalCase as it was created in python first, and as such is different. 
namespace JsonStruct 
{ 
    //the name main will casue some issues
    public class MyJsonStruct
    {

        //cause these classes are not static... we have to create them. Prolly should move this
        //have to be public due to newtonsoft, there may be a way to change
        public generalinfo general;
        public conninfo conn;
        public msginfo msg;
        public statsinfo stats;
        public securityinfo security;

        public string test { get; set; }

        //notes/leftoff: Use newtonsoft, pretty simple, along with the chatGPT example (see below)

        public class generalinfo
        {
            //these guys keep the name the same, allowing you to name variables freely
            [JsonProperty("action")]
            public string action { get; set; }

            [JsonProperty("client_id")]
            public string client_id { get; set; }

            [JsonProperty("client_type")]
            public string client_type { get; set; }

            [JsonProperty("password")]
            public string password { get; set; }
        }

        public class conninfo
        {
            [JsonProperty("client_ip")]
            public string client_ip { get; set; }

            [JsonProperty("client_port")]
            public string client_port { get; set; }
        }

        //might need some work, especially with msg_content being a nested json value in the json desc
        public class msginfo
        {
            public string msg_to { get; set; }

            //see next note, not sure what this will be used for now
            public string msg_content { get; set; }


            //these 2 are no longer nested casue that adds complexity & pain here
            public string msg_command { get; set; }
            public string msg_value { get; set; }

            public string msg_length { get; set; }

            public string msg_hash { get; set; }


        }

        public class statsinfo
        {
            public string latest_checkin { get; set; }

            public string device_hostname { get; set; }

            public string device_username { get; set; }

        }

        public class securityinfo
        {
            public string client_hash { get; set; }

            public string server_hash { get; set; }

        }

    }

}


/*
using System;
using Newtonsoft.Json;

public class Product
{
    public string Name { get; set; }
    public DateTime ExpiryDate { get; set; }
    public decimal Price { get; set; }
    public string[] Sizes { get; set; }
    public NestedObject Nested { get; set; } // Nested property

    public class NestedObject
    {
        public string NestedProperty { get; set; }
    }
}

class Program
{
    static void Main()
    {
        Product product = new Product();
        product.Name = "Apple";
        product.ExpiryDate = new DateTime(2008, 12, 28);
        product.Price = 3.99M;
        product.Sizes = new string[] { "Small", "Medium", "Large" };
        
        // Creating a nested object
        product.Nested = new Product.NestedObject
        {
            NestedProperty = "NestedValue"
        };

        string output = JsonConvert.SerializeObject(product);

        Console.WriteLine(output);
        // Output:
        // {
        //   "Name": "Apple",
        //   "ExpiryDate": "2008-12-28T00:00:00",
        //   "Price": 3.99,
        //   "Sizes": [
        //     "Small",
        //     "Medium",
        //     "Large"
        //   ],
        //   "Nested": {
        //     "NestedProperty": "NestedValue"
        //   }
        // }

        Product deserializedProduct = JsonConvert.DeserializeObject<Product>(output);

        Console.WriteLine(deserializedProduct.Nested.NestedProperty);
        // Output:
        // NestedValue
    }
}
*/