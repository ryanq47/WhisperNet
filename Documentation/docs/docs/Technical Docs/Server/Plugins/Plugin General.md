## Plugins

The server utilizes two primary categories of plugins: **Public** and **Control** plugins, each serving distinct purposes within the server's architecture.

### Control Plugins

Control plugins are designed to manage and control the server, accessible through the GUI or from other nodes. These plugins operate on a unified port, facilitating centralized management and control functionalities.

#### Examples:

- **Authentication Plugin:** Handles authentication processes.
  - Endpoint: `/api/login`

### Public Plugins

Public plugins are intended for interaction with external clients, acting as individual mini-servers. Each plugin initializes its own Flask instance and operates on a separate port, ensuring modularity and standalone operability. Communication with the rest of the server or node is exclusively conducted via HTTP, without direct code interaction.

#### Examples:

- **ListenerHTTP:** Manages HTTP get and post requests.
  - Get Endpoint: `/http/get`
  - Post Endpoint: `/http/post`

This distinction between Public and Control plugins enhances the server's modularity, allowing for both integrated and standalone plugin operation.
