#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber
ip="192.168.1.102"


def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(str(topic))

def on_message(client, userdata, msg):
        a=msg.payload.decode()
        return a
        
        
    
client = mqtt.Client()
client.connect(str(ip),1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
