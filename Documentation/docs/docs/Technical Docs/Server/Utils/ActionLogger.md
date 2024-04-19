### Class: ActionLogger

#### Description
`ActionLogger` is a singleton class designed to log actions taken by users and interactions with clients to a JSON file. It ensures that all log entries are written securely even from multiple threads. It's basically a CYA logger, just so actions can be tracked/proven that you did or didn't do something.

#### Methods

##### `__new__(cls)`
- **Description**: Ensures that only one instance of `ActionLogger` exists (singleton pattern). Initializes the log storage path.
- **Returns**: An instance of `ActionLogger`.

##### `log(request_id, response_id, action, status, details, request, response, client)`
- **Description**: Logs an action with details about the request, action performed, status, and additional details.
- **Parameters**:
  - `request_id`: Identifier for the request.
  - `response_id`: Identifier for the response.
  - `action`: Description of the action performed.
  - `status`: Status of the action (e.g., 'success', 'fail').
  - `details`: Additional details about the action.
  - `request`: Data sent to the client.
  - `response`: Data received from the client.
  - `client`: Identifier or details of the client.

##### `_write_to_file(entry)`
- **Description**: Appends a log entry to the JSON log file.
- **Parameters**:
  - `entry`: The log entry dictionary to be written to the file.

##### `retrieve_logs()`
- **Description**: Retrieves and returns all log entries from the log file.
- **Returns**: A list of log entries.

#### Usage Example
You are not required to use every key for each log entry. However, it is highly recommended to use request_id along with request to track the request data and its associated identifier. Similarly, pairing response_id with response is preferred to effectively trace the responses corresponding to the requests.

```python
## Init/access singleton
logger = ActionLogger()

## Log an action
logger.log(
    request_id="req001", 
    response_id="", 
    action="Initialize System", 
    status="success", 
    details="System initialized without errors.", 
    request={"command": "init"}, 
    response=""
)

## Getting all logs
logs = logger.retrieve_logs()
for log in logs:
    print(log)

```


#### Log Example:

Below is an expanded log. Each entry will be condensed/properly serialized. 

```
{
  "log_timestamp": "2024-04-18T23:07:37.252798",
  "client": "Nickname",
  "request_id": null,
  "response_id": null,
  "action": "Recieved response",
  "status": null,
  "details": null,
  "request": null,
  "response": {
    "request_id": "req_1713499657",
    "timestamp": 1713499657,
    "status": "success",
    "result": {
      "data": "Example result data"
    },
    "error": {
      "code": null,
      "message": null
    }
  }
}
```

###### Serialized log

```
{"log_timestamp": "2024-04-18T23:07:37.252798", "client": "Nickname", "request_id": null, "response_id": null, "action": "Recieved response", "status": null, "details": null, "request": null, "response": {"request_id": "req_1713499657", "timestamp": 1713499657, "status": "success", "result": {"data": "Example result data"}, "error": {"code": null, "message": null}}}
```