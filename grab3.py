import socket
socket.setdefaulttimeout(2)
s = socket.socket()

target = "attack.samsclass.info"
tport = int(input('Target Port: '))
s.connect((target, tport))
print(s.recv(1024))
s.close()