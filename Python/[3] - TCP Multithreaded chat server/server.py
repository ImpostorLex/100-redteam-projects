import socket
import threading
import struct
TCP_PORT = 4211
BUFF_SIZE = 4096
CLIENTS = []

# Create a tcp socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the private IP address of the machine, if it does not exists use localhost instead
def get_ip():

    # Returns a tuple index 0 IP address and index 1 port assigned when
    # using socket.socket
    local_address = tcp.getsockname()[0]

    if local_address:

        return local_address

    # Use 127.0.0.1 instead.
    else:

        return "127.0.0.1"


def receive_message(foo):

    while True:
        msg = foo.recv(BUFF_SIZE)
        for client in CLIENTS:
            if client != foo:
                try:
                    client.send(msg)
                except:
                    # Handle broken connections or errors
                    pass
        
        
private_ip = get_ip()

# These two are outside as this only binds the IP and PORT and it tells the server socket it is in listening mode.
tcp.bind((private_ip, TCP_PORT))
tcp.listen()


def accept_multiple_client():
    # Listen for incoming connection
    while True:
        conn, addr = tcp.accept()
        # Receive name from client
        msg = conn.recv(BUFF_SIZE)
        print(f"A client name: {msg.decode()} connected to the server")
        CLIENTS.append(conn)
        # Start a new thread to handle the connection for each client
        client_thread = threading.Thread(target=receive_message, args=(conn,))
        client_thread.start()

multiple_client_thread = threading.Thread(target=accept_multiple_client)
multiple_client_thread.start()

