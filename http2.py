import socket
socket.setdefaulttimeout(2)
s=socket.socket()



target = "attack.samsclass.info"
tport = 80
user = input('Username: ')
pw = input('Password: ')
length = len(user) + len(pw) +5

s.connect((target, tport))
a = "POST /python/login1.php HTTP/1.1\nHost: " + target \
+ "\nContent-Length: "+ str(length) \
+ "\nContent-Type: application/x-www-form-urlencoded" \
+ "\n\nu=" + user + "&p=" + pw
print(a)
s.send(bytes(a,'UTF-8'))
print(s.recv(1024))
s.close()