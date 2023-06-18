import socket

# Establishes a TCP socket
tcp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind address
TCP_PORT = 1234
TCP_IP = "127.0.0.1"
BUFF_SIZE = 4096

tcp1.bind((TCP_IP, TCP_PORT))

# Listen for incomming connection and only accept one connection at a time.
tcp1.listen()

# Accept connection from clients
# The conn is the new socket object that can be used to send and receive data while the addr is the address that is bounded
conn, addr = tcp1.accept()

print(f"Connection accepted from address {addr}")


while True:
    msg = conn.recv(BUFF_SIZE)

    if not msg:
        break
    print(msg.decode())
