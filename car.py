# Python 2

# Own module to handle the connection
import network_controller

running = True
movment = {'x':0,'y':0}
inc = 0.5

while running:
	inp = network_controller.get_input()

	if inp == 'w':
		movment['y'] += inc
	if inp == 'a':
		movment['x'] -= inc
	if inp == 'd':
		movment['x'] += inc
	if inp == 's':
		movment['y'] -= inc

	if inp == 'c' or inp == '':
		print('Stopping car')
		movment = {'x':0,'y':0}
		running = False
	
	print 'x:{} , y{}'.format(movment['x'], movment['y'])

network_controller.close()