# Python 2

# Own module to handle the connection
import network_controller
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

# Max speed 1, 0 is stop
def normalize_input(d):
	for k in d:
		
		if d[k] > 1:
			d[k] = 1
		
		elif d[k] < -1:
			d[k] = -1
	
	return d

running = True
movment = {'x':0,'y':0}
inc = 0.3

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

	# Break down
	if inp == 'b' :
		movment = {'x':0,'y':0}

	# If value somehow gets over limit, reduce it to limit
	movment = normalize_input(movment)

	# Robot loses grip if turn is more then 50%
	# Focus more on turn
	if abs(movment['x']) > 0.5:
		if movment['x'] > 0.5
			robot.right(speed=movment['x'])
		elif movment['x'] < -0.5:
			robot.left(speed=abs(movment['x']))

	else:
		# Sends the robot forwards
		if movment['y'] > 0:
			if movment['x'] > 0:
				robot.forward( speed=movment['y'], curve_right=movment['x'] )
			else:
				robot.forward( speed=movment['y'], curve_left=abs(movment['x']) )
		
		# Sending robot backwards
		elif movment['y'] < 0:
			if movment['x'] > 0:
				robot.backward( speed=abs(movment['y']), curve_right=movment['x'] )
			else:
				robot.backward( speed=abs(movment['y']), curve_left=abs(movment['x']) )

		# Make sure robot stops if no speed
		else:
			robot.stop()

	# Input is '' if connection stops
	if inp == 'c' or inp == '':
		print('Stopping car')
		movment = {'x':0,'y':0}
		running = False

	speed_left, speed_right = robot.value
	
	print 'Motor speed: Left:{} , Right:{}'.format( speed_left , speed_right )

network_controller.close()