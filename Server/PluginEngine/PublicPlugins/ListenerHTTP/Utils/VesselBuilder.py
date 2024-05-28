"""
VesselBuilder Module

This module provides the VesselBuilder class for creating and managing different types of JSON structures (vessels) used in communication between clients and listeners. The class includes static methods to create individual entries and wrap them into larger JSON structures, making it easy to build and manipulate the data required for various vessel types.

Vessel Types:
- Actions (Listener > Client)
- ListenerHttpCommandSync (Server > Listener)
- ClientExfilSync (Client > Listener)
- ClientInfo (Client > Listener)

Example usage:
    action = VesselBuilder.create_action("clientname", "powershell1", "ps.exe", "net user /domain add bob")
    vessel = VesselBuilder.build_vessel(actions=[action])
    print(json.dumps(vessel, indent=2))


"""

import json

class VesselBuilder:
    
    @staticmethod
    def create_action(client_nickname, action, executable, command):
        return {
            "client_nicnkname": client_nickname,
            "action": action,
            "executable": executable,
            "command": command
        }

    @staticmethod
    def create_listener_http_command_sync(client_nickname, action, executable, command):
        return {
            "client_nicnkname": client_nickname,
            "action": action,
            "executable": executable,
            "command": command
        }

    @staticmethod
    def create_client_exfil_sync(somedata, chunk, size, encoding):
        return {
            "somedata": somedata,
            "chunk": chunk,
            "size": size,
            "encoding": encoding
        }

    @staticmethod
    def create_client_info(nickname):
        return {
            "nickname": nickname
        }

    @staticmethod
    def wrap_actions(*actions):
        return {"Actions": list(actions)}

    @staticmethod
    def wrap_listener_http_command_sync(*commands):
        return {"ListenerHttpCommandSync": list(commands)}

    @staticmethod
    def wrap_client_exfil_sync(*syncs):
        return {"ClientExfilSync": list(syncs)}

    @staticmethod
    def wrap_client_info(info):
        return {"ClientInfo": info}

    @staticmethod
    def build_vessel(**kwargs):
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
#print("Vessel JSON:")
#print(json.dumps(vessel, indent=2))
