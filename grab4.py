import socket
import time
socket.setdefaulttimeout(2)
s = socket.socket()
t = socket.socket()
u = socket.socket()

target = "attack.samsclass.info"
s.connect((target, 3100))
tport = int(input('Target Port: '))
t.connect((target, tport))
time.sleep(2)
u.connect((target,3003))
print(u.recv,1024)
s.close()
t.close()
u.close()


