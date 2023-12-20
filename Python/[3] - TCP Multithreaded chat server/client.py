import socket
import threading
import time

TCP_PORT = 4211
BUFF_SIZE = 4096
PRIVATE_IP = "192.168.100.39"  # Replace with the SERVER IP
name = input("Please enter your name: ")

# Create a tcp socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_message():

    while True:
        msg = tcp.recv(BUFF_SIZE)

        if len(msg) == 0:
            break
        print(f"\n{msg.decode()}")


def send_message():

    while True:
        print(end='', flush=True)
        reply = input("")
        # Append the username
        reply = f"{name}: {reply}"
        tcp.send(reply.encode())


while True:
    try:
        tcp.connect((PRIVATE_IP, TCP_PORT))
        tcp.send(name.encode())
        print("Connected to the server.")
        break  # Break out of the loop if connection is successful
    except socket.error as e:
        print(f"Error: {e}")
        print("Waiting for a server...")
        time.sleep(5) 

# Start receiving and sending threads in other words send and recv
# messages asynchronously
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
receive_thread.start()
send_thread.start()
