import socket
import threading


HOST = "127.0.0.1"
PORT = 5000

stop_event = threading.Event()


def receive_messages(connection):
   
    buffer = bytearray()

    try:
        while not stop_event.is_set():
            data = connection.recv(4096)
            if not data:
                print("\nThe server closed the connection.")
                break

            buffer.extend(data)
            while b"\n" in buffer:
                line, _, remaining = buffer.partition(b"\n")
                buffer[:] = remaining
                print(line.decode("utf-8"))
    except (ConnectionError, OSError, UnicodeDecodeError):
        if not stop_event.is_set():
            print("\nThe connection ended.")
    finally:
        stop_event.set()


def main():
    username = input("Choose a chat name: ").strip()
    if not username or "\n" in username:
        print("Please enter a non-empty chat name.")
        return

    try:
        connection = socket.create_connection((HOST, PORT), timeout=5)
    except OSError as error:
        print(f"Could not connect to the chat server: {error}")
        print("Start server.py first, then run this client again.")
        return

    connection.settimeout(None)
    connection.sendall((username + "\n").encode("utf-8"))
    print("Connected. Type a message and press Enter. Type /quit to leave.")

    receiver = threading.Thread(
        target=receive_messages,
        args=(connection,),
        daemon=True,
    )
    receiver.start()

    try:
        while not stop_event.is_set():
            message = input()
            if message.strip().lower() == "/quit":
                break
            if message.strip():
                connection.sendall((message + "\n").encode("utf-8"))
    except (EOFError, KeyboardInterrupt):
        print("\nLeaving the chat...")
    except (ConnectionError, OSError) as error:
        print(f"\nMessage was not sent because the connection ended: {error}")
    finally:
        stop_event.set()
        try:
            connection.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        connection.close()
        receiver.join(timeout=1)


if __name__ == "__main__":
    main()

