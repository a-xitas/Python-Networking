# Simple TCP Client:

import socket

#target_host = 'www.google.com'
#target_port = 80

# creat a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((socket.gethostname(), 1234))

# send some data
#client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')

#receive some data
response = client.recv(4096)

print(response.decode("utf-8"))
client.close()