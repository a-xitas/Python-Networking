# Simple TCP Server:

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen(5)

while True:
	client, address = server.accept()
	print(f"Connection from {address} has been accepted and established!")
	client.send(bytes("Welcome to the server!", "utf-8"))
