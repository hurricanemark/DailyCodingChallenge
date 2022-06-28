import socket


def banner(ip, port):
    sock = socket.socket()
    sock.connect_ex((ip, int(port)))
    res = sock.recv(1024)
    type(res)
    print(res)
    
    
if __name__ == '__main__':
    ip = input("Please enter the IP address: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)


