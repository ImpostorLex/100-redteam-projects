import argparse
import socket
import ipaddress

print("Use --help to show the available commands")
parser = argparse.ArgumentParser(description='A script with a short description.')
parser.add_argument('-i', '--ip', type=str, help='The IPv4 address', required=True)
parser.add_argument('-p', '--port', type=str, help='The number of ports to scan default top 1000 ports', default=1000)


args = parser.parse_args()
ip_add = args.ip
port = int(args.port)

def is_valid_ip(ip_add):
    try:
        ipaddress.ip_address(ip_add)
        return True
    except ValueError:
        return False
    
def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except (socket.timeout, socket.error):
        return False

if is_valid_ip(ip_add):
    for port_num in range(port + 1):
        if is_port_open(ip_add, port_num):
            print(f"Port number: {port_num} is open")
            
        
