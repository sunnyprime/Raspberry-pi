import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
for x in range(0,5):
    GPIO.output(12, True)
    print("Running")
    time.sleep(10)
    GPIO.output(12, True)
    time.sleep(10)
GPIO.cleanup()
print("Stopped")
