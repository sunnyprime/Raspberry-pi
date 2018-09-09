# Raspberry pi
Raspberrypi basic installation,static ip creatrion and apache server creations

![RPI](https://github.com/sunnyprime/Raspberry-pi/blob/master/91zSu44%2B34L._SX569_.jpg)

![RPI_PIN](https://github.com/sunnyprime/Raspberry-pi/blob/master/oDRh4lpYwoZHHrJiQR64.png)


### Download and [Noobs Operating System](https://www.raspberrypi.org/downloads/noobs/)

1. Extract all the files to memory card.

2. Put memory card in raspberry Pi .

3. Follow The Simple Steps.



### GPIO Sample

```
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
for x in range(0,5):
    GPIO.output(12, True)
    print("Running")
    time.sleep(10)
    GPIO.output(12, False)
    time.sleep(10)
GPIO.cleanup()
print("Stopped")
