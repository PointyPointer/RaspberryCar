# Python 2

# Own module to handle the connection
import network_controller
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

# Max speed 1, 0 is stop
def normalize_input(d):
	for value in d.values():
		
		if value > 1:
			value = 1
		
		elif value < -1:
			value = -1
	
	return d

running = True
movment = {'x':0,'y':0}
inc = 0.5

while running:
	inp = network_controller.get_input()

	if inp == 'w' and movment['y'] < 1:
		movment['y'] += inc
	if inp == 'a' and movment['x'] > -1:
		movment['x'] -= inc
	if inp == 'd' and movment['x'] > 1:
		movment['x'] += inc
	if inp == 's' and movment['y'] > -1:
		movment['y'] -= inc

	# Break down
	if inp == 'b' :
		movment = {'x':0,'y':0}

	# If value somehow gets over limit, reduce it to limit
	movment = normalize_input(movment)

	# Sends the robot forwards
	if movment['y'] > 1:
		if movment['x'] > 0:
			robot.forward( speed=movment['y'], curve_right=movment['x'] )
		else:
			robot.forward( speed=movment['y'], curve_left=abs(movment['x']) )
	
	# Sending robot backwards
	elif movment['y'] < 1:
		if movment['x'] > 0:
			robot.backward( speed=movment['y'], curve_right=movment['x'] )
		else:
			robot.backward( speed=movment['y'], curve_left=abs(movment['x']) )

	# Input is '' if connection stops
	if inp == 'c' or inp == '':
		print('Stopping car')
		movment = {'x':0,'y':0}
		running = False

	speed_left, speed_right = robot.value()
	
	print 'Motor speed: Left:{} , Right:{}'.format( speed_left , speed_right )

network_controller.close()