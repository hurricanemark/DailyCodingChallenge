import socket # Import socket module

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

host = socket.gethostbyname(socket.gethostname()) # Get local machine name
port = 43210 # Reserve a port for your service.
serverSock.bind((host, port)) # Bind to the port

serverSock.listen(5) # Now wait for client connection.
print('Server %s ' % host, end=' ')
print('is listening on port %d' % port)

while (True):
    connection, addr = serverSock.accept() # Establish connection with client.
    print("Got connection from %s", str(addr))
    from_client = ''
    while True:
        data = connection.recv(1024)
        if not data: break
        from_client += data.decode('utf-8')
        print (from_client)
        connection.sendall(from_client.encode('utf-8'))
    connection.close() # Close the connection
    print ('client disconnected')