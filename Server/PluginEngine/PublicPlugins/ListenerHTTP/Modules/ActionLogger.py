import json
import threading
from datetime import datetime

class ActionLogger:
    """
     A (singleton) logger specifically for logging actions taken by users & interactions with clients.
     Outptus a file with JSON entries, with details for each action.

    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ActionLogger, cls).__new__(cls)
                cls._instance._log_entries = []
                cls._instance.file_path = "Action_Log.json"  # Define the path where logs will be stored
            return cls._instance

    def log(self, request_id = None, response_id = None, action = None, status = None, details = None, request = None, response = None, client = None):
        """
        Logs an action with its status and detailed message into the log file as JSON.

        :param request_id: The id of the request
        :param response_id: The id of the response, if applicable.
        :param action: The action performed.
        :param status: The status of the action (e.g., success, fail).
        :param details: Detailed information or output of the action.
        :param request: The data that is being sent to the client.
        :param response: The data that is being sent BACK from the client, to the server/listener.
        """
        entry = {
            "log_timestamp": datetime.now().isoformat(),
            "client":client,
            "request_id": request_id,
            "response_id": response_id,
            "action": action,
            "status": status,
            "details": details,
            "request": request,
            "response": response
        }
        self._log_entries.append(entry)
        self._write_to_file(entry)

    def _write_to_file(self, entry):
        """
        Writes a single log entry to the file. Ensures each entry is appended to a JSON file.
        
        :param entry: The log entry to be written.
        """
        with open(self.file_path, 'a') as file:
            json.dump(entry, file)
            file.write('\n')  # Write each entry on a new line for easier parsing.

    def retrieve_logs(self):
        """
        Retrieves all log entries from the log file.
        
        :return: A list of all log entries.
        """
        with open(self.file_path, 'r') as file:
            return [json.loads(line) for line in file]

# Example usage of JsonLogger
if __name__ == "__main__":
    logger = ActionLogger()
    logger.log(
        "req001", "resp001", "Initialize System", "success", 
        "System initialized without errors.", {"command": "init"}, {"result": "ok"}
    )
    logger.log(
        "req002", "resp002", "Send Command", "fail", 
        "Failed to send command due to timeout.", {"command": "reboot"}, {"error": "timeout"}
    )

    # Print all logs
    logs = logger.retrieve_logs()
    for log in logs:
        print(log)
