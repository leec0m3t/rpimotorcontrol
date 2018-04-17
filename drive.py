# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

class Motor:
	def __init__(self, en, pin_1, pin_2):
		self.en = en
		self.pin_1 = pin_1
		self.pin_2 = pin_2

		GPIO.setup( en , GPIO.OUT )
		GPIO.setup( pin_1 , GPIO.OUT )
		GPIO.setup( pin_2 , GPIO.OUT )

		self.pwm = GPIO.PWM( en , 100 )
		self.pwm.start( 100 )

	def forward(self):
		GPIO.output( self.pin_1 , 1 )
		GPIO.output( self.pin_2 , 0 )

	def backward(self):
		GPIO.output( self.pin_1 , 0 )
		GPIO.output( self.pin_2 , 1 )

	def stop(self):
		GPIO.output( self.pin_1 , 0 )
		GPIO.output( self.pin_2 , 0 )

	def unknown(self):
		GPIO.output( self.pin_1 , 1 )
		GPIO.output( self.pin_2 , 1 )

GPIO.setmode( GPIO.BCM )

leftMotor = Motor( 26 , 19 , 13 ) # EN = 37, PIN_1 = 35, PIN_2 = 33
rightMotor = Motor( 0 , 6 , 5 ) # EN = 27, PIN_1 = 31, PIN_2 = 29
frontMotor = Motor( 11 , 9 , 10 ) # EN = 23, PIN_1 = 21, PIN_2 = 19

angleNum = 0.1

def go():
	leftMotor.forward()
	rightMotor.forward()

def back():
	leftMotor.backward()
	rightMotor.backward()

def left():
	frontMotor.forward()
	sleep(angleNum)
	frontMotor.stop()

def right():
	frontMotor.backward()
	sleep(angleNum)
	frontMotor.stop()

def pause():
	frontMotor.stop()
	leftMotor.stop()
	rightMotor.stop()

leftMotor.pwm.ChangeFrequency( 50000 )
rightMotor.pwm.ChangeFrequency( 50000 )

leftMotor.pwm.ChangeDutyCycle ( 35 )
rightMotor.pwm.ChangeDutyCycle ( 35 )

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

	elif op == "1":
		leftMotor.pwm.ChangeDutyCycle ( 10 )
		rightMotor.pwm.ChangeDutyCycle ( 10 )

	elif op == "2":
		leftMotor.pwm.ChangeDutyCycle ( 20 )
		rightMotor.pwm.ChangeDutyCycle ( 20 )

	elif op == "3":
		leftMotor.pwm.ChangeDutyCycle ( 30 )
		rightMotor.pwm.ChangeDutyCycle ( 30 )

	elif op == "4":
		leftMotor.pwm.ChangeDutyCycle ( 40 )
		rightMotor.pwm.ChangeDutyCycle ( 40 )

	elif op == "5":
		leftMotor.pwm.ChangeDutyCycle ( 50 )
		rightMotor.pwm.ChangeDutyCycle ( 50 )

	elif op == "6":
		leftMotor.pwm.ChangeDutyCycle ( 60 )
		rightMotor.pwm.ChangeDutyCycle ( 60 )

	elif op == "7":
		leftMotor.pwm.ChangeDutyCycle ( 70 )
		rightMotor.pwm.ChangeDutyCycle ( 70 )

	elif op == "8":
		leftMotor.pwm.ChangeDutyCycle ( 80 )
		rightMotor.pwm.ChangeDutyCycle ( 80 )

	elif op == "9":
		leftMotor.pwm.ChangeDutyCycle ( 90 )
		rightMotor.pwm.ChangeDutyCycle ( 90 )

	elif op == "0":
		leftMotor.pwm.ChangeDutyCycle ( 100 )
		rightMotor.pwm.ChangeDutyCycle ( 100 )

	else:
		splited = op.split() #ex) set front dc 100

		if len(splited) != 0:

			if splited[0] == "set":

				if splited[1] == "front":

					if splited[2] == "dc":
						frontMotor.pwm.ChangeDutyCycle ( float(splited[3]) )

					elif splited[2] == "freq":
						frontMotor.pwm.ChangeFrequency( float(splited[3]) )

					else:
						print("Correct operation, Please\n")

				elif splited[1] == "back":

					if splited[2] == "dc":
						leftMotor.pwm.ChangeDutyCycle ( float(splited[3]) )
						rightMotor.pwm.ChangeDutyCycle ( float(splited[3]) )

					elif splited[2] == "freq":
						leftMotor.pwm.ChangeFrequency( float(splited[3]) )
						rightMotor.pwm.ChangeFrequency( float(splited[3]) )

					else:
						print("Correct operation, Please\n")

				else:
					print("Correct operation, Please\n")

			elif splited[0] == "angle":
				angleNum = float(splited[1])

			else:
				print("Correct operation, Please\n")

		else:
			print("Correct operation, Please\n")

GPIO.cleanup()

