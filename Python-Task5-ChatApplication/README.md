# Chat Application

A beginner-tier, two-user command-line chat built with Python sockets and threads. The server accepts clients on localhost, adds a timestamp to messages, and tells the remaining users when someone disconnects.

## Requirements

- Python 3
- No third-party packages
- Two terminal windows for the clients, plus one for the server

## Run on one computer

Open three PowerShell terminals in this folder.

In terminal 1, start the server:

```powershell
python server.py
```

In terminal 2, start the first client and enter a chat name:

```powershell
python client.py
```

In terminal 3, start the second client and enter a different chat name:

```powershell
python client.py
```

Type a message in either client terminal. It appears in both clients with a time prefix. Type `/quit` to leave; the other client receives a disconnect notice. Press Ctrl+C in the server terminal to stop the server.

## How it works

- `server.py` listens on `127.0.0.1:5000` and uses a thread for each connected client.
- `client.py` uses one thread to receive messages while the main thread waits for typed messages.
- Newline characters separate messages so multiple messages can be sent over the same socket connection.

## Privacy and security

This beginner version runs on the same computer and does not save chat messages to disk. Messages are not encrypted, so do not use it for private or sensitive conversations. The server relays messages to connected clients only.

