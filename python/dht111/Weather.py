#!/usr/bin/python
import sys
import Adafruit_DHT
import sys
sys.path.append('/home/pi/lcd')
import lcd
lcd.lcd_init()

print 'running'

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    #lcd.lcd_init()
    #int a,b='{0:0.1f}','{1:0.1f}'.format(temperature, humidity)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    temp="Temperature"+str({0:0.1f})
    #lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    #lcd.lcd_string("Temperatue")
    #lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    #lcd.lcd_string("humidity")
    print temp