import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(
    b"Hello from the UDP client",
    ("127.0.0.1", 6000)
)

response, address = client.recvfrom(1024)

print("Server response:", response.decode())
client.close()
