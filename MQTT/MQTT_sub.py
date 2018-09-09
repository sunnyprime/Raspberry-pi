#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("leds1")

def on_message(client, userdata, msg):
        a=msg.payload.decode()
        print(a)
        
    
client = mqtt.Client()
client.connect("192.168.1.102",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()