import socket

s=socket.socket()
print "Socket created successfully..."

host=socket.gethostname()

port=12345
s.bind(('',port))
print "Waiting for connection request from client...."

s.listen(5)

c, addr = s.accept()
print "Connection created sending data...."

c.send("Hello World....")

c.close()
