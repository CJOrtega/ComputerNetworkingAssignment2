# Cristopher Ortega
# CN4713: Net-Centric Computing
# Assignment 2

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5001))
server.listen(1)

print("TCP Server is waiting on port 5001")

client_socket, client_address = server.accept()

print("Client connected:", client_address)

message = client_socket.recv(1024)

print("Message received:", message.decode())

client_socket.send(f"ACK: received '{message.decode()}' ({len(message)} bytes)".encode())

client_socket.close()
server.close()

print("Server closed.")
