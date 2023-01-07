# logec-attack
Welcome to Logec-Attack (LA) - A (minimal attempt at a) clone of Cobalt Strike, created to learn how offensive tools work. <br>


## _How does LA work?:_

LA works off a client server model, similar to how a CS Beacon, or even a Meterpreter instance works. You input commands into the server,
and the client recieves, and runs them. Your job is to get the client onto the target machine, and let LA take care of the rest. 

## _Getting Started:_
Run 'pip install -r requirements.txt' to install the needed packages, then 'python3 logec-attack.py'

To run the client, cd into 'agent/client/' and run 'python3 client.py' - Note: The default IP and Port it tries to connect to are '127.0.0.1' and '5064'

## "The Rest"

### _The Main Shell:_ <br>
  The "Main Shell" is the first point of contact with the target, it's very simple, on purpose***. It uses Python's build in subprocess module to run commands on the target system - and from what I can tell, this is not picked up by Windows Defender at this time, as subprocess is used quite often. Where things may get hairy, is the connection back to the Server. The client tries to connect every 30 seconds (until connected) by default, and a firewall may block that. 

_*** Note, the shell is not fully interactive, so no nano, cd, or any password prompts, etc. Doing so will result in either a program freeze, or an "INVALID COMMAND" error._

To listen for a client connection, click Target -> Listen For Connection. In the popup, enter the listener details. 
>![image](https://user-images.githubusercontent.com/91687869/206892006-c2031f89-ba95-447d-a056-fafd5edcd133.png)

>Click Listen, and LA will now be listening: <br>
>![image](https://user-images.githubusercontent.com/91687869/206892035-3a962ef6-ea08-4c3a-8078-65969c6a9927.png)

> Upon connection, LA will display 'Connected' with a green background ****
>![image](https://user-images.githubusercontent.com/91687869/206892202-4a92ab41-e5ed-46db-835a-c5318190fa9a.png)

> Once connected, you can now use the Main Shell! (remeber, use simple commands, nothing interactive)
![image](https://user-images.githubusercontent.com/91687869/206931214-3fb2aaf5-93a6-429c-8ba4-9e0cd7a75855.png)



_****: Known bug, 'Connected' may not turn green, but if it says connected, you are connected_ <br>



### Now let's get into the fun stuff - but fair warning, these actions are very loud, and could set off a lot of alarms:

### _Target Info:_
  The 'Target Info' button gathers some data about your target, such as their IP address, OS version, and Device HostName. This is unlikely to set off any alarms, but still be cautious. Access via 'Target' -> 'Target Info'

### _Reverse Shells:_
  Currently, there are 3 reverse shells avaible using Python, Perl, and Ruby*. Once connected via the "Main Shell", you can click Target -> Spawn Shell -> Language (Hover over language of choice) -> Linux or Windows**
 
>Selecting a shell:<br>
![image](https://user-images.githubusercontent.com/91687869/206891032-7c476ffb-4bea-4438-ae5a-74da547982cf.png)

>Shell Popup menu:<br>
![image](https://user-images.githubusercontent.com/91687869/206891820-3fbadd92-7b2f-4e80-8d4e-03f9aeb0419d.png)


At the moment, LA _cannot_ catch the shell for you, so you have to start your own listener using netcat (nc -lvnp PORT). 

* = Note, the ruby shell is not fully interactive at this time (No nano, vi, or any password prompts etc) <br>
** Explicit windows shells are coming, for now you can just enter the location of cmd.exe in the 'program' feild as a workaround

### _The Destruction Tab: <br>_
  Forewarning - The name is very fitting to all modules here for a reason, they will break, disable, and/or outright demolish a system - so be very careful. <br>
  >Encryption Menu:<br>
  'Encrypt Files': A module that will encrypt a target directory via AES encryption - you can even choose your own password. <br>
   ![image](https://user-images.githubusercontent.com/91687869/206891627-b1a39a5e-c0ec-4f60-aafb-773afe33e5b4.png)

  


### _Diagrams:_ <br>

>Network Diagram: <br>
>![image](https://user-images.githubusercontent.com/91687869/206885050-58326a5f-c243-4931-a7ea-725d1f92bf0f.png) <br>

>Program Layout: <br>
>![image](https://user-images.githubusercontent.com/91687869/206885056-85b932d1-1344-4020-8336-522bf4b36e1b.png)

### _School:_ <br>
#### 1. Define and write your own custom Python class(es) and/or Python GUI environment.<br>
PyQt GUI enviornment, multiple custom classes throughout the project.<br>

####  2. Define and write your own at least three methods or functions (init doesnot count).<br>
Multiple throuhgout the project<br>

####  3. Use at least one list.<br>
Lists in the file transfer module, and in logec-attack.py in the data_download_thread method<br>

####  4. Use of at least one dictionary.<br>


####  5. Use at least three modules we used in class – tkinter, breezypythongui, pygame, datetime, random etc.<br>

Random is used in the encryption module, DateTime is used in client.py, Threading is used througout the project.<br>

####  6. Use of read or write to files.<br>
The file transfer module reads, and writes files<br>

####  7. Use of exceptions handling: try, except.<br>
try/except used throughout the entire project, mainly for error handling<br>

####  8. Use of if/else/elif, loops, data entry validation.<br>
If/Else/Elif & loops used througout the project<br>

####  9. Explore and apply one Python concept we did not learn in class. Provide appropriate coding comments to designate this in code file and README documentation.<br>
I used PyQt, which we did not use in class, to develop the GUI<br>

####  10. All students will use GitHub to share student’s work with the faculty<br>

### Personal take on this project:

I had a ton of fun working on this - and I plan to continue working on it. However, there are some pitfalls/things I would do differently. First one being the lack of 'signals' in PyQt, which prevented me from making proper changes to the GUI accross threads. I lose some onscreen feedback from different modules due to this, and I plan to implement signals in future releases. <br>

The other big pitfall is that this is written in python... and as such, compiling to machine code is very tough. AFAIK, there is no easy way to cross compile python code - so the client has to be compiled (via pyinstaller, or py2exe) on the respective OS that it is targeting. I am going to start learning some C, which will fix this issue, but that is a ways out. <br>

I did learn a lot though, specifically socket programming, which will be a huge advantage in my career. Without this final, I probably would not have pushed myself to learn it, as it takes some time to properly understand. Another upside was working with PyQt, man it was quite a steep learning curve, but was 100% worth it - I used to be scared of GUI apps, but now they are a walk in the park. 


