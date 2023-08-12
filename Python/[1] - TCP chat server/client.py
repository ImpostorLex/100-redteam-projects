import socket
import threading

TCP_PORT = 4211
BUFF_SIZE = 4096
PRIVATE_IP = ""  # Replace with the SERVER IP

# Create a tcp socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_message():

    while True:
        msg = tcp.recv(BUFF_SIZE)

        if len(msg) == 0:
            break
        print(f"\nUser: {msg.decode()}")


def send_message():

    while True:
        reply = input("Input your message here: ")
        tcp.send(reply.encode())


tcp.connect((PRIVATE_IP, TCP_PORT))

# Start receiving and sending threads in other words send and recv
# messages asynchronously
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
receive_thread.start()
send_thread.start()
