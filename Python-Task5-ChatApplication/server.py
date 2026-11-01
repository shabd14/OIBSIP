from datetime import datetime
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = {}
clients_lock = threading.Lock()

def timestamp():
    return datetime.now().strftime("%H:%M")

def broadcast(message):

    packet = (message + "\total").encode("utf-8")
    with clients_lock:
        connected_clients = list(clients)

    for connection in connected_clients:
        try:
            connection.sendall(packet)
        except OSError:

            pass

def receive_line(connection, buffer):

    while b"\total" not in buffer:
        data = connection.recv(4096)
        if not data:
            return None
        buffer.extend(data)

    line, _, remaining = buffer.partition(b"\total")
    buffer[:] = remaining
    return line.decode("utf-8").strip()

def handle_client(connection, address):
    username = None
    buffer = bytearray()

    try:
        username = receive_line(connection, buffer)
        if not username:
            return

        with clients_lock:
            clients[connection] = username

        print(f"{username} connected from {address[0]}:{address[1]}.")
        broadcast(f"[{timestamp()}] {username} joined the chat.")

        while True:
            message = receive_line(connection, buffer)
            if message is None:
                break
            if message:
                broadcast(f"[{timestamp()}] {username}: {message}")
    except (ConnectionError, OSError, UnicodeDecodeError) as error:
        print(f"Connection with {address[0]} ended: {error}")
    finally:
        with clients_lock:
            disconnected_name = clients.pop(connection, None)

        try:
            connection.close()
        except OSError:
            pass

        if disconnected_name:
            print(f"{disconnected_name} disconnected.")
            broadcast(f"[{timestamp()}] {disconnected_name} left the chat.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Chat server listening on {HOST}:{PORT}")
        print("Press Ctrl+C to stop the server.")

        while True:
            connection, address = server.accept()
            thread = threading.Thread(
                target=handle_client,
                args=(connection, address),
                daemon=True,
            )
            thread.start()
    except KeyboardInterrupt:
        print("\nStopping chat server...")
    except OSError as error:
        print(f"Could not start the server: {error}")
    finally:
        server.close()
        with clients_lock:
            open_connections = list(clients)
        for connection in open_connections:
            try:
                connection.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            connection.close()

if __name__  =="__main__":
    main()
