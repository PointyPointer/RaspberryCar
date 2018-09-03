# Python 2
import socket

HOST = 'x.x.x.x'  	# Address to the raspberry pi
PORT = 55555	    # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The server needs to bind a port others can interact with
s.bind((HOST, PORT))

# Allow one connection to be made
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

def get_input():
	return conn.recv(1).decode().lower()

def close():
	s.close()
	print 'connection stoped'