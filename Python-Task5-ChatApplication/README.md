Chat Application

A basic command line chat application using Python sockets and threading. Start the server and 2 or more clients on the same computer.

Features

Multiple clients can connect to the server.

Each client has a chat name.

Messages have a timestamp at the beginning.

Clients can see who has joined and left the chat.

Receiving messages in a thread means you can receive messages while typing.

No third party libraries used.

Requirements

Python 3

No third party libraries.

3 terminal windows to test with 2 clients.

Running Locally

Open 3 terminal windows in this directory.

Terminal 1 - Run the server.

python server.py

Terminal 2 - Run the first client.

python client.py

Set a chat name.

Terminal 3 - Run the second client.

python client.py

Set a different chat name. Type a message into either of the client terminals. To exit the chat type /quit. To stop the server press Ctrl+C.

If your system uses python3 then replace python with python3.

How it Works

The server (server.py) listens on 127.0.0.1:5000.

A new thread is started for each client that connects.

The client (client.py) sends the typed messages. A new thread is started for receiving messages.

Each message ends with a newline character.

Troubleshooting

Client won’t connect. Make sure to run server.py first.

Port is in use. Close any programs that are using port 5000 or change the PORT variable in both server.py and client.py to the same unused port.

No messages showing. Ensure that the server is running and that both clients have connected.

What I Have Practised

Basic client-server communication.

Python sockets.

Threading for parallel tasks.

Error handling for connections and clients disconnecting.

Limitations

This version is set up to be used locally. The chat messages are not encrypted and the program does not save any messages to file. This should not be used for private/sensitive conversations.
