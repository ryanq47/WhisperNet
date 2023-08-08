import logging
import Data.JsonHandler
import Comms.CommsHandler

class Trees:

    def user_input_tree(user_input = None, cookie = None, conn = None):
        '''
        The decision tree for the user_inputs. if a command is meant for the server, it gets passed to the server from here
        '''

        if user_input.lower() in ["help", "", None]:
            print("Help Menu:\n\t'help'\t: Spawns this menu\n\t'exit'\t: Exits the program")

        elif user_input.lower() == "exit":
            exit("Exiting...")

        else:
            ## parse & pass to server
            '''
            Iddeas

            client_id command command args
                .split, [0] : msg_to
                .split [1]... : msg_command
            '''

            ## split into list
            parsed_input = user_input.split()

            ## get agent_id
            send_to = parsed_input[0]
            ## getting rid of space after client_id, parsing from original user_input
            command = user_input[len(parsed_input[0]) + 1:]

            logging.debug(f"[DecisionTree.Trees.user_input_tree()] list input: '{parsed_input}', parsed client: '{send_to}' parsed command: '{command}' -- Watch for any odd spaces if you are getting errors")

            
            json_string_for_server = Data.JsonHandler.json_ops.to_json_for_server(
                action = "!_userlogin_!",
                auth_type = "cookie",
                auth_value = cookie,
                msg_to=send_to,
                msg_command = command
                )
            
            ## something is up, messages seemingly not getting sent over
            print(conn)
            Comms.CommsHandler.send_msg(conn=conn, msg=json_string_for_server)
            #print(Comms.CommsHandler.receive_msg(conn=conn))







'''
Parser notes

    input   :  'bob one two'
    list    :  ['bob', 'one', 'two']
    ID      :  AABBC12
    command :  reload file.exe


    ## breaking the parser:

    ## multiple spaces on input will (may...) break the command section. be careful with spaces lol

        input   :  '     bob one two'
        list    :  ['bob', 'one', 'two']
        ID      :  AABBC12
        command :  '     reload file.exe'


'''