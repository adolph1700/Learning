import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#encode converts a string to UTF-8 or bytes
mysock.send(cmd)
while(True):
	data =  mysock.recv(512) # 512 charcters
	if (len(data)<1):
		break					#end of transmission
	print(data.decode())
#decode converts UTF-8 data to unicode
mysock.close()