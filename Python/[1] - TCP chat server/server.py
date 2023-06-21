import socket
import threading

TCP_PORT = 4211
BUFF_SIZE = 4096


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


def receive_message(conn):

    while True:
        msg = conn.recv(BUFF_SIZE)

        if len(msg) == 0:
            break
        print(f"\nUser: {msg.decode()}")


def send_message(conn):

    while True:
        reply = input("Input your message here: ")
        conn.send(reply.encode())


private_ip = get_ip()

tcp.bind((private_ip, TCP_PORT))

# Listen for incomming connection and only accept one connection at a time.
tcp.listen()


# Accept connection from clients
# The conn is the new socket object that can be used to send and receive data while the addr is the address that is bounded
conn, addr = tcp.accept()

print(f"Connection accepted from address {addr}")

# Start receiving and sending threads in other words send and recv
# messages asynchronously
receive_thread = threading.Thread(target=receive_message, args=(conn,))
send_thread = threading.Thread(target=send_message, args=(conn,))
receive_thread.start()
send_thread.start()
