import paho.mqtt.client as mqtt
import json
import time
import datetime


def on_connect(client, userdata, flags, rc):
    client.subscribe("pi/weather")

def on_message(client, userdata, msg):

    json_obj = json.loads(msg.payload.decode());
    json_obj.update({"Date_Time":str(datetime.datetime.now())});
    post_data = json.dumps(json_obj)
    print("post_data");


client = mqtt.Client()
client.connect("192.168.43.67",1883,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
