
CLI Usage documentation.

# CLI Interface Documentation

The Command-Line Interface (CLI) of the application is designed to provide an interactive environment for interacting with various features and functionalities. The CLI utilizes a prefix-based navigation system to organize and execute different commands. This documentation will guide you through the process of using the CLI interface effectively.

## Command Structure <a name="command-structure"></a>

The CLI interface operates using a prefix-based navigation system. Each command begins with a prefix that categorizes the command's purpose. The general structure is as follows:

```
prefix [sub_command] [options]
```

- **prefix**: Indicates the main category or type of command you want to execute.


		Current Prefixes:
			show   : Shows data
			connect: Connects to...
			





- **sub_command**: If applicable, further refines the command within the chosen prefix category.

		Examples:
			show program data
			connect to server

- **options**: Additional arguments or options that the command might require.

		Not currently implemented YET

For example, to execute a "show" command, you would enter `show [sub_command] [options]`.

## Available Commands <a name="available-commands"></a>

### help

Displays a help menu that provides information about available commands and their usage.

```bash
help
```

### exit

Exits the CLI session.

```bash
exit
```

### clear

Clears the screen, providing a cleaner interface for better readability.

```bash
clear
```


## Show Prefix

### show

Enters the "show" category to execute specific sub-commands related to displaying various information.

```bash
show [sub_command] [options]
```

Sub-commands under the "show" category may include:
- `help`: Displays a help menu specific to the "show" category.
- `platform data`: Displays platform-related information.

Remember that you can always enter the `help` command to get information about available commands and their usage.
### show platform data

Displays information about the platform on which the application is running.

```bash
show platform data
```


## Connect Prefix
### connect to server

Initiates the process of connecting to a server. Additional options may be required.

```bash
connect to server [options]
```
