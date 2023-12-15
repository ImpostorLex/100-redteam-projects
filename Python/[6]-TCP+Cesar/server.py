import socket
import threading

TCP_PORT = 4211
BUFF_SIZE = 4096
SHIFT = 6

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

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
        decrypted_msg = ""
        msg = conn.recv(BUFF_SIZE)
        
        # Decrypt
        for letter in str(msg.decode()):
            if letter.isnumeric() or not letter.isalnum():
                decrypted_msg += letter
            elif letter.isupper():
                index = uppercase_letters.index(letter)
                decrypted_msg += uppercase_letters[(index - SHIFT) % 26]
            elif letter.islower():
                index = lowercase_letters.index(letter)
                decrypted_msg += lowercase_letters[(index - SHIFT) % 26]
        
        
        if len(msg) == 0:
            break
        print(f"\nReceive encoded: {msg.decode()}")
        print(f"\nReceive decoded: {decrypted_msg}")



def send_message(conn):
    encrypted_msg = ""
    while True:
        print(end='', flush=True)
        
        reply = input("Input your message here: ")
        
        for letter in str(reply):
            if letter.isnumeric() or not letter.isalnum():
                encrypted_msg += letter
            elif letter.isupper():
                index = uppercase_letters.index(letter)
                encrypted_msg += uppercase_letters[(index + SHIFT) % 26]
            elif letter.islower():
                index = lowercase_letters.index(letter)
                encrypted_msg += lowercase_letters[(index + SHIFT) % 26]
        conn.send(encrypted_msg.encode())


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
