## Installation

To install, run:

`pip install -r requirements.txt`

## Neo4j

### Installation

1. Download Neo4j:
    - Visit [Neo4j Deployment Center](https://neo4j.com/deployment-center/?gdb-selfmanaged).
    - Download the "Community" edition for your platform.
    - Follow the installation instructions provided.

### Windows Startup

- Start Neo4j:
    ```
    <neo4jdir>/bin/neo4j.bat start
    ```

### Windows Service Setup (Optional)

- Install as a Windows Service:
    ```
    <neo4jdir>/bin/neo4j.bat windows-service install
    ```
- Start Neo4j:
    ```
    <neo4jdir>/bin/neo4j.bat start
    ```

### Post-Install Setup

1. Access Neo4j:
    - Open a web browser and navigate to `*neo4jip*:7474`.
2. Initial Login:
    - Use the default credentials `neo4j:neo4j`.
3. Change Password:
    - Update your password when prompted.
4. Configure Environment Variables:
    - Create a `.env` file from `env.example.txt`.
    - Add the URI, User, and Password to the `.env` file.

## Starting the Server

To start the server, run:

`python3 server.py --ip 0.0.0.0 --port 5000`



If that doesn't work, hit it with a hammer, and submit an issue in github.