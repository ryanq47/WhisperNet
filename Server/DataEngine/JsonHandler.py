import json
import fastjsonschema
import re

## should proooooly be a static method due to the compile method, have it return the validate object to self.json_compiled
## then pass that into the json_parser so it has the compiled data without re-compiling

class json_ops:
    def __init__(self):
        ## compiles the JSON schema on init
        self.fast_json_compile()

    def fast_json_compile(self):
        """
        A method to compile

        """

        ## may run into issues with some of these, worst case then don't validate those feilds

        ## this is a little confusing, but basically, it's defining what to check.
        ## the properties feild tells it where the proerties are, and the required are the required keys
        schema = {
            "type": "object",
            "properties": {
                "Main": {
                    "type": "object",
                    "properties": {
                        "general": {
                            "type": "object",
                            "properties": {
                                "client_id": {"type": "string"},
                                "client_type": {"type": "string"}
                            },
                            "required": ["client_id", "client_type"]
                        },
                        "conn": {
                            "type": "object",
                            "properties": {
                                "client_ip": {"type": "string"},
                                "client_port": {"type": "integer"}
                            },
                            "required": ["client_ip", "client_port"]
                        },
                        "msg": {
                            "type": "object",
                            "properties": {
                                "msg_to": {"type": "string"},
                                "msg_content": {
                                    "type": "object",
                                    "properties": {
                                        "command": {"type": "string"},
                                        "value": {"type": "string"}
                                    },
                                    "required": ["command"]
                                },
                                "msg_length": {"type": "integer"},
                                "msg_hash": {"type": "string"}
                            },
                            "required": ["msg_to", "msg_content", "msg_length", "msg_hash"]
                        },
                        "stats": {
                            "type": "object",
                            "properties": {
                                "latest_checkin": {"type": "string"},
                                "device_hostname": {"type": "string"},
                                "device_username": {"type": "string"}
                            },
                            "required": ["latest_checkin", "device_hostname", "device_username"]
                        },
                        "security": {
                            "type": "object",
                            "properties": {
                                "client_hash": {"type": "string"},
                                "server_hash": {"type": "string"}
                            },
                            "required": ["client_hash", "server_hash"]
                        }
                    },
                    "required": ["general", "conn", "msg", "stats", "security"]
                }
            },
            "required": ["Main"]
        }

        self.validate = fastjsonschema.compile(schema)
        #return validate


    def convert_and_validate(self, json_string="data"):
        """
        Takes JSON data, parses it, and returns a dict. The goal of this function is to identify any missing critical
        keys, (see the readme) and any empty values.

        Additinally, this is a bit of a security handler, as non-valid JSON data will yeild an error, and there will be options
        to drop a host, block them, ignore, etc on any "poking around" someone might do.

        data: Takes the json string
        json_validate_data: compiled JSON thingy to validate JSON
        """
        #print(json_string)
        json_object = None
        ## Sanity check to make sure JSON is actually JSON b4 passing into validator
        try:
            # Python Obj             #raw JSON
            json_object = json.loads(json_string)
            #print("JSON data is valid.")


            ## checking if json conforms to schema
            #bypassing
            '''if self.validate(json_object):
                return json_object

            else:
                return False'''
            return json_object

            #logging.debug("[JSON Parser] JSON is valid")

        except json.JSONDecodeError as e:
            print(f"JSON data is not valid. Error message: {e}")
            # logging.warning("[JSON Parser] JSON is not valid!")
            ## no need to return value as this will only be seen by code. return 1 for fail
            return False
        except Exception as e:
            print(f"error with JSON: {e}")
            return False

    def validate(self, json_object):
        """
        This validates the json data to the schema defined above. Basically, if no errors occur, it
        returns true, which allows the json object to be returned in the convert_and_validate function

        json_objet: A json string to validate
        """

        ## Validation json data
        try:
            ## takes json_object variable, not raw json
            self.validate(json_object)
            print("Data is valid")
            # logging.warning("[JSON Parser] Error validating JSON")
            return True
        except fastjsonschema.JsonSchemaException as jse:
            print(jse)
            # logging.warning(f"[JSON Parser] Error validating JSON {jse}")
            return False
        except Exception as e:
            print(e)
            #logging.warning(f"[JSON Parser] Error validating JSON {e}")
            return False

        #return json_object



def json_packer():
    """
    Takes data & packs it into json for sending? not sure if needed yet
    """
    pass

'''
## Test Data set
json_data1 = {
    "Main": {
        "general": {
            "client_id": "superman",
            "client_type": "fclient"
        },
        "conn": {
            "client_ip": "1234",
            "client_port": 6969
        },
        "msg": {
            "msg_to": "server",
            "msg_content": "maliciouspayloadfilecontents",
            "msg_length": 50,
            "msg_hash": ""
        },
        "stats": {
            "latest_checkin": "time.now",
            "device_hostname": "hostname",
            "device_username": "username"
        },
        "security": {
            "client_hash": "test",
            "server_hash": "test"
        }
    }
}

validated_stuff = fast_json_compile()
json_convert_and_validate(validated_stuff, json.dumps(json_data1))'''
