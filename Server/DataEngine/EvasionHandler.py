'''
Like CS's malleable profile, but called evasion profiles cause legal reasons probably

TLDR: This alters how the server responds, and interacts to/with clients.

Anyways

Takes: JSON string

Does actions
    - Add random padding, etc
    - Other evasion stuff
    - (later) sleep/jitter ranges

Reutrns: Json String


## Big question? Call at start of server, or per malicious client handler? (leaning towards option 2)

'''
import yaml
import random
import inspect
import logging

import DataEngine.JsonHandler

function_debug_symbol = "[^]"

class EvasionProfile:
    def __init__(self, sys_path = None, evasionprofile_file_path = None):
        self.profile_data = None
        self.json_dict = None
        self.sys_path = sys_path
        self.evasionprofile_file_path = evasionprofile_file_path   

        self._yaml_load()

    def _yaml_load(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        ## this is dumb. lots of room for bad errors
        print(f"{self.sys_path} + {self.evasionprofile_file_path}")
        profile_path = self.sys_path + self.evasionprofile_file_path
        try:
            with open(profile_path, 'r') as yaml_file:
                profile_data = yaml.safe_load(yaml_file)
            
            self.profile_data = profile_data

        except Exception as e:
            print(f"[EvasionHandler.yaml_load()] Error loading YAML: {e}")
        ## takes YAML profile, and loads it.

    def mystify(self, json_string):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        """
        ~~~ Is a mystery... ~~~ Just kidding. Obsfucates & pads the commands going to the client so they evade detection.

        json_string (str): The json String to modify

        Returns a (modified) json string
        """
        print(" === MYSTIFY ===")


        ## turns into dict...
        self.json_dict = DataEngine.JsonHandler.json_ops.from_json(json_string)

        ## does actions...

        ## JSON getting duplicated somewhere in here
        if self.json_dict:
            # Decided to do a self.json_dict instead of a local variable to keep readibility & reduce any temp local variables
            self._create_blank_value_padding(self.json_dict)

        else:
            print("[DataEngine.EvasionHandler.EvasionProfile.mystify()] Error with JSON dict.")

        serialized_modified_json_string = DataEngine.JsonHandler.json_ops.serialize(self.json_dict)

        print(serialized_modified_json_string)

        ## returns modioofied json string
        return serialized_modified_json_string

        ## on failure, just return the original string?

    def _create_blank_value_padding(self, json_dict = None):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        """Adds random data to the blank key pairs. DOES NOT overwrite any pairs with data in them

        sets self.json_dict to new values
        """
    
        for outer_key, inner_dict in json_dict.items():
            for inner_key in inner_dict:
                print("INNER KEy:" + inner_dict[inner_key])

                if inner_dict[inner_key] == "" or inner_dict[inner_key] == None:
                    # Set new value for each inner_key
                    inner_dict[inner_key] = self._generate_random_data()
        
        print(json_dict)
        self.json_dict = json_dict
        

    def _generate_random_data(self):
        logging.debug(f"{function_debug_symbol} {inspect.stack()[0][3]}")

        '''generates & retunrs random chars from YAML file/evasion profile'''

        char_set = self.profile_data['Padding']['Characters']
        minlength = self.profile_data['Padding']['MinLength']
        maxlength = self.profile_data['Padding']['MaxLength']
        
        ## temprarily adding SCRAM so I know the feild is scrambled
        random_string = "SCRAM" + ''.join(random.choice(char_set) for _ in range(minlength, maxlength))
        return random_string