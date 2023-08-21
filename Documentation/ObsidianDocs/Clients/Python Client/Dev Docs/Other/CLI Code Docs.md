# CLI Interface Technical Documentation

## Overview

The Command-Line Interface (CLI) module provides an interactive command-line environment for users to interact with the application's features and functionalities. The module employs a prefix-based navigation system to categorize and execute commands efficiently. This technical documentation outlines the code flow and components of the CLI interface to help developers understand its implementation.

## Components

### 1. `Trees` Class

The `Trees` class forms the core of the CLI interface. It defines the decision trees for user inputs and routes commands to their corresponding actions. The class contains the following methods:

#### `home_tree(user_input = None)`

- This method processes user inputs and delegates commands to their respective actions.
- It utilizes the prefix-based approach to categorize and execute commands.
- The `dispatch` dictionary maps command prefixes to corresponding action methods.
- If a prefix matches, the associated action is retrieved and executed.
- If a "show" command is detected, it routes to the `prefix_show_tree` method.

#### `prefix_show_tree(cmd = None)`

- This method handles "show" prefix commands and routes to their sub-commands.
- It uses the `dispatch` dictionary to map sub-commands to their actions.
- If a valid sub-command is detected, the corresponding action is executed.
- If an invalid sub-command is detected, an error message is displayed.

### 2. `SystemDefaultActions` Class (UDPAT EME)

The SystemDefaultActions class defines methods that correspond to different actions triggered by user commands. These methods handle specific functionalities and are linked to the `dispatch` dictionaries in the `Trees` class.

### 3. Command Structure

The command structure follows the pattern `prefix [sub_command] [options]`. Each command begins with a prefix, which categorizes the command's purpose. Sub-commands refine the command further, and options provide additional arguments if required.

### 4. Parser Notes

The documentation provides important information regarding the input parsing process. It underscores the potential challenges with multiple spaces in input and offers examples for clarification.

## Code Flow

1. The CLI session is initiated by executing the Python script that contains the CLI module.

2. Users are presented with a command prompt, allowing them to input commands.

3. User inputs are processed in the `home_tree` method of the `Trees` class.

4. The prefix of the input is extracted by splitting the input string and retrieving the first word.

5. The extracted prefix is used to determine the action to be executed from the `dispatch` dictionary.

6. If a valid action is found, it is executed. If the action is `prefix_show_tree`, the sub-command is extracted and processed.

7. If an invalid action is detected, an error message is displayed.

8. If the action is `prefix_show_tree`, the appropriate sub-command action is executed based on the `dispatch` dictionary.

9. Results of the executed actions are displayed to the user.
