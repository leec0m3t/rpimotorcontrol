from time import sleep
import pigpio

class Motor:
	def __init__(self, en, pin_1, pin_2):
		self.en = en
		self.pin_1 = pin_1
		self.pin_2 = pin_2

		pi.set_mode( en , pigpio.OUTPUT )
		pi.set_mode( pin_1 , pigpio.OUTPUT )
		pi.set_mode( pin_2 , pigpio.OUTPUT )

		pi.set_PWM_frequency( en , 100 )
		pi.set_PWM_dutycycle( en , 255 ) # PWM off

	def forward(self):
		pi.write( self.pin_1 , 0 )
		pi.write( self.pin_2 , 1 )

	def backward(self):
		pi.write( self.pin_1 , 1 )
		pi.write( self.pin_2 , 0 )

	def stop(self):
		pi.write( self.pin_1 , 0 )
		pi.write( self.pin_2 , 0 )



pi = pigpio.pi()

leftMotor = Motor( 26 , 19 , 13 ) # EN = 37, PIN_1 = 35, PIN_2 = 33
rightMotor = Motor( 0 , 6 , 5 ) # EN = 27, PIN_1 = 31, PIN_2 = 29
frontMotor = Motor( 11 , 9 , 10 ) # EN = 23, PIN_1 = 21, PIN_2 = 19

while True:
	op = input("OP> ")

	if op == "w":
		go()

	elif op == "s":
		back()

	elif op == "a":
		left()

	elif op == "d":
		right()

	elif op == "q":
		break

	elif op == "e":
		pause()

pi.stop()

"""
pi.set_PWM_dutycycle(4,   0) # PWM off
pi.set_PWM_dutycycle(4,  64) # PWM 1/4 on
pi.set_PWM_dutycycle(4, 128) # PWM 1/2 on
pi.set_PWM_dutycycle(4, 192) # PWM 3/4 on
pi.set_PWM_dutycycle(4, 255) # PWM full on


setpullupdown

"""