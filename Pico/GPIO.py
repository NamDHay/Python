import RPi.GPIO as GPIO
import time

#pin definitions
pwmPin = 18
ledPin = 23
butPin = 17

duty = 75

#set
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setup(butPin,GPIO.IN, pull_up_down = GPIO.PUD_UP)

pwm = GPIO.PWM(pwmPin,200)

GPIO.output(ledPin,GPIO.LOW)
pwm.start(duty)
try:
    while 1:
        #if button not pressed, do something
        if GPIO.input(butPin):
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.LOW)
        #if button pressed, do something
        else:
            pwm.ChangeDutyCycle(duty)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(100*duty)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.5)
except KeyboardInterrupt:
    pwm.stop
    GPIO.cleanup()