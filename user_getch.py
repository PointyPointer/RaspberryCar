# Python 3
import socket

#Used to get a single char as input
from getch import getch

HOST = 'x.x.x.x'  	# Address to the raspberry pi
PORT = 55555       	# Port to connect to (port opened on the pi)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This fails if raspberry is not running host program
s.connect((HOST, PORT))

print('Use <wasd> to controll the car, b to break. c to stop(remember to hit enter to send)')
while True:
	inp = getch()
	s.send(inp.encode()) # send command over the socket

	if 'c' in inp:
		print('Stopping car')
		break

# close the connection
s.close()
