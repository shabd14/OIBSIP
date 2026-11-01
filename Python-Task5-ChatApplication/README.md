# Chat Application

This is a simple command-line chat application built with Python sockets and threads. Run the server and two or more clients on the same computer to exchange messages.

## Features

- Supports multiple connected clients.
- Lets each client choose a chat name.
- Adds a time prefix to chat messages.
- Shows join and leave notices.
- Uses a receiving thread so incoming messages can appear while the user types.
- Uses only Python's standard library.

## Requirements

- Python 3
- No third-party packages
- Three terminal windows to try the example with two clients

## Run it locally

Open three terminal windows in this folder.

**Terminal 1 – start the server:**

```bash
python server.py
```

**Terminal 2 – start the first client:**

```bash
python client.py
```

Enter a chat name when prompted.

**Terminal 3 – start the second client:**

```bash
python client.py
```

Enter a different chat name. Type a message in either client terminal to send it to the connected clients. Type `/quit` to leave the chat. Press `Ctrl+C` in the server terminal to stop the server.

If your system uses `python3`, replace `python` with `python3` in the commands.

## How it works

- `server.py` listens on `127.0.0.1:5000`.
- The server starts a separate thread to handle each client connection.
- `client.py` sends typed messages and runs a separate thread to receive messages.
- Newline characters mark the end of each message.

## Troubleshooting

- **The client cannot connect:** Start `server.py` first, then run the clients.
- **The port is already in use:** Close another program using port `5000` or change `PORT` in both `server.py` and `client.py` to the same unused port.
- **Messages do not appear:** Make sure the server is still running and both clients connected successfully.

## What this project helped me practise

- Basic client-server communication
- Python sockets
- Using threads for concurrent tasks
- Handling connection errors and client disconnections

## Limitations

This version is configured for local use on the same computer. Chat messages are not encrypted, and the program does not save messages to disk. Do not use it for private or sensitive conversations.
