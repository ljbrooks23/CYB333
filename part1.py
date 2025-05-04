#!/usr/bin/env python3

import socket


HOST = '127.0.0.1' # ip of the localhost
PORT = 50000 # port it will listen on


# Make a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Use bind to link socket with host and port
mysock.bind((HOST, PORT))
# Listen on the socket
mysock.listen(1)
print(f"Listening on {HOST}:{PORT}")

# Accept a connection from a client
conn, addr = mysock.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = conn.recv(1024)
print(f"Received data: {data.decode()}")

# Create a port scanner
def port_scanner(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the connection attempt
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

