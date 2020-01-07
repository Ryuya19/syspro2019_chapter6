#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('input degrees (-90 ~ 90)')
print('<br>')
print('<input type="text" name="deg">')
print('<input type="submit" value="送信">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

form = cgi.FieldStorage()
value = form.getvalue("led")

if value == 'ON':
	GPIO.output(14, GPIO.HIGH)
	print('LED ON')

elif value == 'OFF':
	GPIO.output(14, GPIO.LOW)
	print('LED OFF')


