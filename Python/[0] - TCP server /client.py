import socket

TCP_PORT_TO_BIND = 1234
TCP_ADDR_TO_BIND = '127.0.0.1'

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# iniate a connection to the TCP server there is no return value therefore it will return a error if no
# connection happens

tcp_client.connect((TCP_ADDR_TO_BIND, TCP_PORT_TO_BIND))

msg = input("Input your message here: ")

# The send() function expects msg as bytes-like objects
tcp_client.send(msg.encode())
