
import socket
import threading
import os.path
from ftplib import FTP

TCP_PORT = 4211
BUFF_SIZE = 4096
PRIVATE_IP = "192.168.100.39"  # Replace with the SERVER IP

is_logged_in = False
# Create a tcp socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_message():

    while True:
        msg = tcp.recv(BUFF_SIZE)

        if len(msg) == 0:
            break

        if msg.decode() == False:

            print(f"\nftp> Logged in failed.")
        else:
            is_logged_in = True
            print(f"\nftp> {msg.decode()}")


list_of_commands = ['upload', 'help', 'download', 'list']


def send_message():

    while is_logged_in is False:
        user = input("ftp> Enter FTP username: ")
        passwd = input("ftp> Enter FTP password: ")

        combined = f"{user},{passwd}"

        if len(combined) < 2:

            print("Account does not exists or empty input")
        else:
            tcp.send(combined.encode())

    while is_logged_in is True:

        command = input(f"ftp> type 'help' to see available commands")

        print(f"{command}")


try:
    tcp.connect((PRIVATE_IP, TCP_PORT))

    # Start receiving and sending threads in other words send and recv
    # messages asynchronously
    receive_thread = threading.Thread(target=receive_message)
    send_thread = threading.Thread(target=send_message)
    receive_thread.start()
    send_thread.start()
except ConnectionRefusedError:

    print("Server is not up!")
