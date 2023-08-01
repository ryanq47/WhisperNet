class CommsData:
    @staticmethod
    def client():
        sleep_string = '''{"general": {"action": "sleep", "client_id": "", "client_type": "", "password": ""}, "conn": {"client_ip": "", "client_port": ""}, "msg": {"msg_to": "", "msg_content": "", "msg_command": "sleep", "msg_value": "", "msg_length": "", "msg_hash": ""}, "stats": {"latest_checkin": "", "device_hostname": "", "device_username": ""}, "security": {"client_hash": "", "server_hash": ""}}'''