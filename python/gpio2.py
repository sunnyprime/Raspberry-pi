import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM,7)
GPIO.setup(4,GPIO.OUT)
GPIO.cleanup()
GPIO.output(4,False)
GPIO.output(4,True)
print("Running")
time.sleep(2)
GPIO.output(4,False)
GPIO.cleanup()
