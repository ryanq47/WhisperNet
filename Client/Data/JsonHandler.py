import json
import re

## should proooooly be a static method due to the compile method, have it return the validate object to self.json_compiled
## then pass that into the json_parser so it has the compiled data without re-compiling

class json_ops:
    @staticmethod 
    def from_json(json_string="data") -> dict:
        """Convert json STRINGS into a Python Object (aka dict)

        Args:
            json_string (str, optional): the JSON string

        Returns:
            dict: A pyhton dict

        On errors:
            Returns False
        """
        json_object = None
        ## Sanity check to make sure JSON is actually JSON b4 passing into validator
        try:
            # Python Obj             #raw JSON
            json_object = json.loads(json_string)
            return json_object

        except json.JSONDecodeError as e:
            print(f"[DataEngine.JsonHandler.from_json() ] JSON data is not valid. Error message: {e}")
            return False
        except Exception as e:
            print(f"[DataEngine.JsonHandler.from_json()] error with JSON: {e}")
            #print(json_string)
            return False

    @staticmethod
    def serialize(dict = None):
        '''Serialzie to a JSON string from a Dict'''
        try:
            json_str = json.dumps(dict)
            return json_str
        except Exception as e:
            print(f"[DataEngine.JsonHandler.serialize()] error with serizalining to JSON: {e}")
            return False


    @staticmethod
    def to_json(
        ## General
        action = "sleep", client_id = "", client_type = "", password="",
        ## conn
        client_ip = "", client_port = "",
        ##msg
        msg_to = "", msg_content = "", msg_command = "sleep", msg_value = "", msg_length ="", msg_hash =  "",
        ## stats
        latest_checkin = "", device_hostname = "", device_username = "", timestamp = "",
        ## Security: 
        client_hash = "", server_hash = ""

    ):
        """
        Takes data & packs it into json for sending. Use serialize if you already have a json string
        """
        json_dict = {
            "general": {
                "action": action,
                "client_id": client_id,
                "client_type": client_type,
                "password": password
            },
            "conn": {
                "client_ip": client_ip,
                "client_port": client_port
            },
            "msg": {
                "msg_to": msg_to,
                "msg_content": msg_content,
                "msg_command": msg_command,
                "msg_value": msg_value,
                "msg_length": msg_length,
                "msg_hash": msg_hash
            },
            "stats": {
                "latest_checkin": latest_checkin,
                "device_hostname": device_hostname,
                "device_username": device_username,
                "timestamp": timestamp
            },
            "security": {
                "client_hash": client_hash,
                "server_hash": server_hash
            }
        }

        #print(json_dict)

        json_str = json.dumps(json_dict)

        return json_str

    @staticmethod
    def to_json_for_client(
        ## General
        action = "!_userlogin_!", client_id = "", client_type = "", auth_type = "", auth_value="",
        ## conn
        client_ip = "", client_port = "",
        ##msg
        msg_to = "", msg_content = "", msg_command = "sleep", msg_value = "", msg_length ="", msg_hash =  "",
        ## stats
        latest_checkin = "", device_hostname = "", device_username = "", timestamp = "",
        ## Security: 
        client_hash = "", server_hash = ""

    ):
        """
        Takes data & packs it into json for sending between server & client. Use serialize if you already have a json string
        """
        json_dict = {
            "general": {
                "action": action,
                "client_id": client_id,
                "client_type": client_type,
                "auth_type":auth_type,
                "auth_value": auth_value
            },
            "conn": {
                "client_ip": client_ip,
                "client_port": client_port
            },
            "msg": {
                "msg_to": msg_to,
                "msg_command": msg_command,
                "msg_value": msg_value,
                "msg_length": msg_length,
                "msg_hash": msg_hash
            },
            "stats": {
                "latest_checkin": latest_checkin,
                "device_hostname": device_hostname,
                "device_username": device_username,
                "timestamp": timestamp
            },
            "security": {
                "client_hash": client_hash,
                "server_hash": server_hash
            }
        }

        #print(json_dict)

        json_str = json.dumps(json_dict)

        return json_str

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

#print(json_ops.to_json())