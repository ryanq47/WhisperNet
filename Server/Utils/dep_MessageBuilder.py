import uuid
import time
from flask import jsonify
from PluginEngine.PublicPlugins.ListenerHTTP.Utils.DataSingleton import Data
import json

class MessageHelper:
    @staticmethod
    def generate_unique_id() -> str:
        """
        Generate a unique message ID using UUIDv4.

        Returns:
            str: A unique UUIDv4 string.
        """
        return str(uuid.uuid4())

    @staticmethod
    def generate_timestamp() -> int:
        """
        Generate a current timestamp.

        Returns:
            int: The current timestamp in seconds since the epoch.
        """
        return int(time.time())

def api_request(status: str = "success", data: dict = None, error_message: str = None, data_items: list = None, **kwargs) -> dict:
    """
    Helper function to create/construct a request JSON string to send between parts of the stack.

    Args:
        status (str): Status of the request, e.g., "success" or "failure".
        data (dict): Data to be included in the request.
        error_message (str): Error message, if any.
        data_items (list): List of tuples (key, value) to add to the data dict.
        **kwargs: Additional keyword arguments to include in the request.

    Returns:
        dict: The constructed request dictionary.
    """
    data_singleton = Data()

    # Initialize request structure
    request = {
        "rid": MessageHelper.generate_unique_id(),  # Unique identifier for this request
        "timestamp": MessageHelper.generate_timestamp(),  # Current timestamp
        "status": status,
        "data": data if data else {},
        "error": error_message if error_message else {}
    }

    # Add additional data items if provided
    if data_items:
        for key, value in data_items:
            request["data"][key] = value

    # Remove error key if it has no useful content
    if data_singleton.Config.get_value("responses.return_error_message"):
        if not request["error"]:
            del request["error"]

    # Remove data key if it has no useful content
    if not request["data"]:
        del request["data"]

    # Add any additional keyword arguments, excluding None values
    request.update({k: v for k, v in kwargs.items() if v is not None})

    # Return the request dictionary
    return request

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
    @staticmethod
    def build_prepared_request(status: str = "success", error_message: str = None, data_items: list = None, **kwargs) -> dict:
        """
        Build a prepared request using the VesselBuilder and api_request functions. AKA an "all in one" function

        Just pass in the sync keys that you need in the request, and it returns a dict object with
        everything in it!

        Args:
            status (str): Status of the request, e.g., "success" or "failure".
            error_message (str): Error message, if any.
            data_items (list): List of tuples (key, value) to add to the data dict.
            **kwargs: Additional keyword arguments for building the vessel and request.

        Returns:
            dict: The prepared request dictionary.
        """
        # Build the vessel using the provided kwargs

        # problem is here.
        vessel = VesselBuilder.build_vessel(**kwargs)
        
        print("vessel")
        print(vessel)

        # Prepare the request body using api_request function
        prepared_request = api_request(
            status=status,
            data=vessel,
            error_message=error_message,
            data_items=data_items
        )
        
        return prepared_request
    
    @staticmethod
    def create_action(client_nickname: str, action: str, executable: str, command: str) -> dict:
        """
        Create an action dictionary.

        Args:
            client_nickname (str): Nickname of the client.
            action (str): Action to be performed.
            executable (str): Executable to be used.
            command (str): Command to be executed.

        Returns:
            dict: The constructed action dictionary.
        """
        return {
            "client_nickname": client_nickname,
            "action": action,
            "executable": executable,
            "command": command
        }

    @staticmethod
    def create_listener_http_command_sync(client_nickname: str, action: str, executable: str, command: str) -> dict:
        """
        Create a listener HTTP command sync dictionary.

        Args:
            client_nickname (str): Nickname of the client.
            action (str): Action to be performed.
            executable (str): Executable to be used.
            command (str): Command to be executed.

        Returns:
            dict: The constructed listener HTTP command sync dictionary.
        """
        return {
            "client_nickname": client_nickname,
            "action": action,
            "executable": executable,
            "command": command
        }

    @staticmethod
    def create_client_exfil_sync(somedata: str, chunk: int, size: int, encoding: str) -> dict:
        """
        Create a client exfil sync dictionary.

        Args:
            somedata (str): Data to be exfiltrated.
            chunk (int): Chunk number.
            size (int): Size of the chunk.
            encoding (str): Encoding of the data.

        Returns:
            dict: The constructed client exfil sync dictionary.
        """
        return {
            "somedata": somedata,
            "chunk": chunk,
            "size": size,
            "encoding": encoding
        }

    @staticmethod
    def create_client_info(nickname: str) -> dict:
        """
        Create a client info dictionary.

        Args:
            nickname (str): Nickname of the client.

        Returns:
            dict: The constructed client info dictionary.
        """
        return {
            "nickname": nickname
        }

    @staticmethod
    def wrap_actions(*actions: dict) -> dict:
        """
        Wrap actions into a dictionary.

        Args:
            *actions (dict): Actions to be wrapped.

        Returns:
            dict: The wrapped actions dictionary.
        """
        return {"Actions": list(actions)}

    @staticmethod
    def wrap_listener_http_command_sync(*commands: dict) -> dict:
        """
        Wrap listener HTTP command syncs into a dictionary.

        Args:
            *commands (dict): Listener HTTP command syncs to be wrapped.

        Returns:
            dict: The wrapped listener HTTP command syncs dictionary.
        """
        return {"ListenerHttpCommandSync": list(commands)}

    @staticmethod
    def wrap_client_exfil_sync(*syncs: dict) -> dict:
        """
        Wrap client exfil syncs into a dictionary.

        Args:
            *syncs (dict): Client exfil syncs to be wrapped.

        Returns:
            dict: The wrapped client exfil syncs dictionary.
        """
        return {"ClientExfilSync": list(syncs)}

    @staticmethod
    def wrap_client_info(info: dict) -> dict:
        """
        Wrap client info into a dictionary.

        Args:
            info (dict): Client info to be wrapped.

        Returns:
            dict: The wrapped client info dictionary.
        """
        return {"ClientInfo": info}

    @staticmethod
    def build_vessel(**kwargs) -> dict:
        """
        Build a vessel dictionary from provided keyword arguments.

        Args:
            **kwargs: Keyword arguments for building the vessel.

        Returns:
            dict: The constructed vessel dictionary.
        """
        vessel = {}

        if 'actions' in kwargs:
            vessel.update(VesselBuilder.wrap_actions(*kwargs['actions']))

        if 'listener_http_command_sync' in kwargs:
            vessel.update(VesselBuilder.wrap_listener_http_command_sync(*kwargs['listener_http_command_sync']))

        if 'client_exfil_sync' in kwargs:
            vessel.update(VesselBuilder.wrap_client_exfil_sync(*kwargs['client_exfil_sync']))

        if 'client_info' in kwargs:
            vessel.update(VesselBuilder.wrap_client_info(kwargs['client_info']))

        return vessel


'''
# Example usage

# Create individual entries
action1 = VesselBuilder.create_action("clientname", "powershell1", "ps.exe", "net user /domain add bob")
action2 = VesselBuilder.create_action("clientname", "powershell2", "ps.exe", "net user /domain add bob")

listener_command1 = VesselBuilder.create_listener_http_command_sync("clientname", "powershell1", "ps.exe", "net user /domain add bob")
listener_command2 = VesselBuilder.create_listener_http_command_sync("clientname", "powershell2", "ps.exe", "net user /domain add bob")

client_exfil_sync1 = VesselBuilder.create_client_exfil_sync("sensitivedata123", 0, 4096, "base64")

client_info = VesselBuilder.create_client_info("name")

# Build vessel with actions and other data
vessel = VesselBuilder.build_vessel(
    actions=[action1, action2],
    listener_http_command_sync=[listener_command1, listener_command2],
    client_exfil_sync=[client_exfil_sync1],
    client_info=client_info
)

# Print the vessel JSON
print("Vessel JSON:")
print(json.dumps(vessel, indent=2))
'''