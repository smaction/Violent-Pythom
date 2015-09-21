import socket
socket.setdefaulttimeout(2)
s=socket.socket()



target = input('Target host name (like www.ccsf.edu): ')
tport = 80
a = "HEAD / HTTP/1.1\nHost: {0} \n\n".format(target)
print(a)
s.connect((target, tport))
s.send(bytes(a,'UTF-8'))
print(s.recv(1024))
s.close()