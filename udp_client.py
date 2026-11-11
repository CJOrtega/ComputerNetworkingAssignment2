# Cristopher Ortega
# CN4713: Net-Centric Computing
# Assignment 2

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Don't wait forever if the server never replies
client.settimeout(5.0)

message = "Cristopher Ortega"

try:
    client.sendto(message.encode(), ("127.0.0.1", 6000))
    print("Message sent:", message)

    response, address = client.recvfrom(1024)
    print("Server response:", response.decode())
except socket.timeout:
    print("Timeout: no response from the server after 5 seconds.")
finally:
    client.close()
