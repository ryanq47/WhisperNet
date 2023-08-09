Handles all JSON serialization, and deserialization. 


### Todo
- [x] FromJson
	- [x] Fairly simple, just destruct, and return that object. Ask chatgpt if stuck
- [ ] Test/QA Args for ToJson
- [ ] Fix return for Fromjson, it crashes on bad json. See notes in code

## Client.Comms (namespace)
- ### JsonHandler (class)
	- ToJson()
		- Takes args, and converts into valid JSON format for the C2 server. 
		- Returns string
	- FromJson()
		- Takes JSON, converts back to C# objects.
		- Returns object.
			- Access objects with 'objectname.general.conn'
	- Test()
		- A test string to make sure everything is still properly accessible. Just prints a short debug msg



## JsonStruct (namespace)
The namespace holding all the JSON structure. Each class here is a part of the structure, I don't fully understand how it works, but I do know that it spits out a JSON string when called correctly. 