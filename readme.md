Hey there! Still working on the readme, in a nutshell, this project is a C2 suite, that includes a server, client, and RAT/Malicious client(Currently in C#, working on a C & A python variant) - with a few other tidbits thrown in.
It's currently in development, but I'm getting close to a release(ish) build. 

My motto for this project is "It's not the best, but it's convenient"

Sidenote, I have no idea who 'arponsarker' - He's there because I forgot to change my email before committing on a new machine (apparently he has kali@kali linked to his account)

In the meantime, here's some cool screenshots:

### C2 Main Page
![image](https://user-images.githubusercontent.com/91687869/234416166-722eb93f-b3d4-4bb1-9e8c-50f12fcc26c5.png)


### Custom PortScanner:
![image](https://user-images.githubusercontent.com/91687869/234417517-0f68fec6-f52d-4ddf-a0b2-85a07047c03b.png)


Note, these next 2 may get nuked on future iterations of the suite, as they eat up time that could be going towards the C2 part

### Credential Bruteforcer
![image](https://user-images.githubusercontent.com/91687869/234416770-44ead565-d5c7-403b-89f0-789bb772b1c4.png)

### Web URL Fuzzer:
![image](https://user-images.githubusercontent.com/91687869/234416853-493e38fc-d0ad-47e0-b79c-8b5ad7c572fe.png)


### lots of settings:
![image](https://user-images.githubusercontent.com/91687869/234416902-0ef4fe15-aa93-40be-acda-6823613e0797.png)

### A Bash few-click script builder: <br> (handy for CCDC)
![image](https://user-images.githubusercontent.com/91687869/234417953-d50e3520-11ef-4949-becb-7054bcd066dc.png)


### Last but not least, A content tab for easy wordlist downloads (dynamically adds links based on user inputted content in the DB)

![image](https://user-images.githubusercontent.com/91687869/234417188-d083e89f-7b8b-4eb4-adfb-634f4c7d06a1.png)

## Documentation
This is some fairly basic documentation, but it covers how most of the C2 suite interacts, via the network, and the decision trees:
![logec-suite-c2-network-diagram](https://user-images.githubusercontent.com/91687869/235392177-2574a711-4245-4bdd-9f24-a9c636b9b97a.png)
<br>
![logec-suite-c2-decision-diagram drawio](https://user-images.githubusercontent.com/91687869/235392171-28154410-9436-4e86-ad68-d7e856b5243b.png)


## Scapy/libc.a Error

cd /usr/lib/x86_64-linux-gnu/ <br>
ln -s -f libc.a liblibc.a


## Windows Support:
There is no "official" support for windows, however that dosen't mean it won't work. If all the dependencies install from pip, it should run smoothly
