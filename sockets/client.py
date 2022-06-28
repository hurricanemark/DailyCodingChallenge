import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

clientSock.connect(('192.168.160.1', 43210))
message = "I am CLIENT. I am sending this message to the server."
clientSock.sendall(message.encode('utf-8'))

from_server = clientSock.recv(1024)
clientSock.close()
print (from_server)
