#!/usr/bin/env python3
from random import uniform
import time
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

topic_name = "clients/123/hello/world"
mqtt_broker = "localhost"
mqtt_client = mqtt.Client("Temperature_Sensor")
mqtt_client.on_connect = on_connect
mqtt_client.connect(mqtt_broker, 1883, 60)

while True:
  randNumber = uniform(20.0, 22.0)
  mqtt_client.publish(topic_name, randNumber)
  print("MQTT: Just published " + str(randNumber) + " to topic " + str(topic_name))
  time.sleep(3)
