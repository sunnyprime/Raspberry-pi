#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher
ip="192.168.1.102"
client = mqtt.Client()
client.connect(str(ip),1883,60)
keep_going=True
while keep_going:
    msg=str(raw_input("Enter Message: \n"))
    client.connect(str(ip),1883,60)
    client.publish("leds1", str(msg));  #topic/test"
    if(msg=="END"):
        keep_going=False

client.disconnect();
