import socket
s = socket.socket()

target = input('Target URL: ')
tport = int(input('Target Port: '))
s.connect((target, tport))
print(s.recv(1024))
s.close()