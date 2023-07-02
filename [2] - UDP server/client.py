import socket
import threading

UDP_PORT = 4211
BUFF_SIZE = 4096
PRIVATE_IP = "192.168.100.39"  # Replace with the SERVER IP

IP = "127.0.0.2"
# Create a tcp socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def receive_message():

    while True:
        msg, addr = udp.recvfrom(BUFF_SIZE)

        if len(msg) == 0:
            break
        print(f"\nUser {addr}: {msg.decode()}")


def send_message():

    while True:
        reply = input("Input your message here: ")
        udp.sendto(reply.encode(), (PRIVATE_IP, UDP_PORT))


udp.bind((IP, 9992))


# Start receiving and sending threads in other words send and recv
# messages asynchronously
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
receive_thread.start()
send_thread.start()
