#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO
import servo    #servo movement

print('Content-type: text/html; charset=UTF-8\r\n\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('input degrees (-90 ~ 90)')
print('<br>')
print('<input type="number" name="deg">')
print('<input type="submit" name="sub" value="send">')
print('</form>')


#GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
#GPIO.setup(14, GPIO.OUT)

form = cgi.FieldStorage()
value = form.getvalue("sub")


### add
if value == "send":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    servo.setservo(int(form.getvalue("deg")))

