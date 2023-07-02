import socket
import threading

UDP_PORT = 4211
BUFF_SIZE = 4096
SOURCE_ADD = "127.0.0.2"

RECV_PORT = 9992
# Create a tcp socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the private IP address of the machine, if it does not exists use localhost instead


def get_ip():

    # Returns a tuple index 0 IP address and index 1 port assigned when
    # using socket.socket
    local_address = udp.getsockname()[0]

    if local_address:

        return local_address

    # Use 127.0.0.1 instead.
    else:

        return "127.0.0.1"


def receive_message():

    while True:
        msg, addr = udp.recvfrom(BUFF_SIZE)

        if len(msg) == 0:
            break
        print(f"\nUser {addr}: {msg.decode()}")


def send_message():

    while True:
        reply = input("Input your message here: ")
        udp.sendto(reply.encode(), (SOURCE_ADD, RECV_PORT))


private_ip = get_ip()

udp.bind((private_ip, UDP_PORT))

# Start receiving and sending threads in other words send and recv
# messages asynchronously
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
receive_thread.start()
send_thread.start()
