import network_controller
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

running = True

while running:
	inp = network_controller.get_input()

	if inp == 'w':
		robot.forward()
	if inp == 'a':

		robot.left(speed=0.5)
	if inp == 'd':
		robot.right(speed=0.5)
	if inp == 's':
		speed_left, speed_right = robot.value
		if speed_left == 0 and speed_right == 0:
			robot.backward()
		else:
			robot.stop()

	# Input is '' if connection stops
	if inp == 'c' or inp == '':
		robot.stop()
		print("Turning off robot")
		running = False
	speed_left, speed_right = robot.value
	
	print 'Motor speed: Left:{} , Right:{}'.format( speed_left , speed_right )

network_controller.close()