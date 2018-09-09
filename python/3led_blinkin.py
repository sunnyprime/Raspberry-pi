import RPi.GPIO as GPIO
import time

i=0.2
l1=4
l2=17
l3=27
rang=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)



for x in range(0,rang):
    GPIO.output(l1, True)
    print("Running")
    time.sleep(i)
    
    GPIO.output(l1, False)
    GPIO.output(l2, True)
    time.sleep(i)
    
    GPIO.output(l2, False)
    GPIO.output(l3, True)
    time.sleep(i)

    GPIO.output(l3, False)

GPIO.cleanup()
print("Stopped")















