#!/usr/bin/env python3
import sys
sys.path.append('/home/pi/lcd')
import lcd
import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("pi/weather")

def on_message(client, userdata, msg):
    if msg.payload.decode() == "Hello world!":
        print("H W")
    else:
        #print("Yes!")
        a=msg.payload.decode()
        print(a)
        lcd.lcd_init()
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        lcd.lcd_string("SMART AGRICULTURE", 2)
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string(a, 2)
        if(a=="END"):
            client.disconnect()
    
client = mqtt.Client()
client.connect("192.168.43.6",1883,60)

client.on_connect = on_connect
client.on_message = on_message
lcd.GPIO.cleanup()
client.loop_forever()