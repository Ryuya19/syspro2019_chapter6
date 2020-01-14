#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO
import servo    #servo movement

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('input degrees (-90 ~ 90)')
print('<br>')
print('<input type="text" name="deg">')
print('<input type="submit" value="send">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.cleanup()

form = cgi.FieldStorage()
value = int(form.getvalue("deg"))
servo.setservo(value)
print('SERVO TURNING FOR ' + value)
