#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("192.168.43.6",1883,60)
for a in range(1,5):
    client.connect("192.168.43.6",1883,60)
    client.publish("topic/test", a);
client.connect("192.168.43.6",1883,60)    
client.publish("topic/test", "END");
client.disconnect();