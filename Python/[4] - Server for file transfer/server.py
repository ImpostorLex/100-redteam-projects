
import socket
import threading

TCP_PORT = 4211
BUFF_SIZE = 4096
IP = "192.168.100.39"

USER = "PIGILAN"
PASSWORD = "IKAWatIKAW"

is_logged_in = False

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_message(conn):

    try:
        while is_logged_in is False:
            msg = conn.recv(BUFF_SIZE)

            creds = (msg.decode()).split(",")

            if creds[0] != USER or creds[1] != PASSWORD:

                reply = False
                conn.send(reply.encode())
            else:

                reply = "Log in succesfully!"
                conn.send(reply.encode())

    except BrokenPipeError:
        print("Client not connected anymore.")


def send_message(conn):

    try:
        while is_logged_in is True:
            reply = input("Input your message here: ")
            conn.send(reply.encode())
    except BrokenPipeError:
        print("Client not connected anymore.")


try:

    tcp.bind((IP, TCP_PORT))

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
except KeyboardInterrupt:

    print("Server Shutting down!")

except:

    print("Something went wrong I dont know if it is the server or the client :)")
