import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

def setservo(deg):
    GPIO.cleanup()
    servo = GPIO.PWM(2, 50)
    servo.ChangeDutyCycle(2.5)
    servo.ChangeDutyCycle(((1.9 / 180) * deg + 0.5) * 5)
    time.sleep(1)
    GPIO.cleanup()


for i in range(10):
    setservo(-90)
    setservo(90)


