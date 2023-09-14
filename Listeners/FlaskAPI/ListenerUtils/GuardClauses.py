import logging

'''
Holds all guard clauses for the progam.


'''


def guard_t_f_check(condition, error_message):
    '''
    A guard clause to check conditions

    condition: The condition, i.e. 'username is none'
    error_message: The message to say IF the condition is not met

    example (from AuthenticationDBHandler)

    if guard_clause(username is None, "[*] Username argument is 'None'! Authentication will fail!"):
    
    ->> The guard works by 'if condition', aka checking if it is True. <<-

    '''
    if condition:
        logging.warning(error_message)
        return True
    return False