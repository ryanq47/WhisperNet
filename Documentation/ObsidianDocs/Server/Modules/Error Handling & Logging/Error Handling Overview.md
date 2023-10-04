After multiple different implementations of error handling, I found the "raise" method the most effective. Each Engine will have a file in it named "ErrorDefinitions.py" - which contain the errors for each module. 

Each error block will:
- Get the error info
- Get the calling function
- Log each error
- Print the error to the screen

```Example Error:

class YAML_LOAD_ERROR(Exception):

    def __init__(self):
		## Getting the error info
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
		## Getting the calling function
        calling_function = inspect.stack()[1][3]

		## setting original error var
        original_error = exc_value

		## logging error
        logging.debug(f"{calling_function}: {original_error}")

		## Printing error to screen.
        super().__init__(f"{calling_function}: {original_error}")
```


This simplifies the error process greatly. Previously, I had to call an inspect on each error, and 'logging.debug' it. Now, I just "raise RELEVANT_ERROR_TYPE" and it handles all of that for me.