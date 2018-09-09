import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


GPIO.output(4, True)
print("Running")
time.sleep(1.01)
GPIO.output(4, False)
GPIO.cleanup()
print("Stopped")
