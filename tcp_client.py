# Cristopher Ortega
# CN4713: Net-Centric Computing
# Assignment 2

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5001))

print("Connected to TCP server.")

client.send(b"Cristopher Ortega")

response = client.recv(1024)
print("Server response:", response.decode())

client.close()
print("Client closed.")
