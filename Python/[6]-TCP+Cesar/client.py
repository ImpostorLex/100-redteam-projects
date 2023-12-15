import socket
import threading

TCP_PORT = 4211
BUFF_SIZE = 4096
PRIVATE_IP = "192.168.100.39"  # Replace with the SERVER IP
SHIFT = 6 # Replace Shift number


encrypted_msg = ""
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'


# Create a tcp socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receive_message():

    while True:
        decrypted_msg = ""
        msg = tcp.recv(BUFF_SIZE)
        
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
        


def send_message():
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
                
        tcp.send(encrypted_msg.encode())


tcp.connect((PRIVATE_IP, TCP_PORT))

# Start receiving and sending threads in other words send and recv
# messages asynchronously
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
receive_thread.start()
send_thread.start()
