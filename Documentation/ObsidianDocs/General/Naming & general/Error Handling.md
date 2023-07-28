**Error Handling Documentation: Logging Format**

For consistent and standardized error handling across the project, it is recommended to follow the specified formatting for logging error messages. The prescribed format is as follows:


`logging.debug(f"[<ClassName>.<MethodName>() <Client ID>] <Error Description>: {<Exception Object>}")`

**Explanation:**

1. **`logging.debug`**: The `logging` module is used for generating log messages of varying severity levels. In this case, we are using the `debug` level to log information useful for debugging purposes. Depending on the severity of the error, you may choose different log levels like `info`, `warning`, `error`, or `critical`. <br><br>
    
2. **`<ClassName>`**: Replace this placeholder with the actual name of the class where the error occurred. It helps in identifying the source of the error more easily. <br><br>
    
3. **`<MethodName>`**: Replace this placeholder with the actual name of the method or function in which the error occurred. This aids in pinpointing the specific location of the error. <br><br>
4. **`<Client ID>`**: The ID of the client if applicable. This makes it easier to track down & differentiate between different class instances. <br><br>
    
4. **`<Error Description>`**: Briefly describe the nature of the error that occurred. Use clear and concise language to explain the problem or the reason for the exception.<br><br>
    
5. **`<Exception Object>`**: This should be the actual exception object that was raised during the error. This information will provide details about the specific exception type and possibly additional information like the error message or traceback.<br><br>


Logging.???

1. **`logging.debug`**: Use the debug for anything that is not needed to be seen by the user. <br><br>
    
2. **`logging.warning`**: Anyhting that could be a concern (such as a weird value, or connection) should be a warning. Warnings are allowed to continue operation<br><br>
    
3. **`logging.critical`**: Anything that is so bad, that it requires the program, or current thread to exit. Keep this at a minimal whenever possible