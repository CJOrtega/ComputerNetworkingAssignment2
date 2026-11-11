import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("127.0.0.1", 6000))

print("UDP Server is waiting on port 6000...")

data, address = server.recvfrom(1024)

print("Message received:", data.decode())
print("Client address:", address)

server.sendto(f"ACK: received '{data.decode()}' ({len(data)} bytes)".encode(), address)

server.close()

print("UDP Server closed.")
