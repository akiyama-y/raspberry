#!/usr/bin/python

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import sys
import json
from time import sleep

mqtt_broker="nabewari.mydns.jp"
state = "off"

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT) #PIN:11, GPIO:17

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("tree")

def on_message(client, userdata, msg):
    value = json.loads(msg.payload)
    mode = value.get('mode')
    tree_light(mode)

def tree_light(mode):
    state = mode

    print "mode: {0}".format(mode)

    if mode == "off":
        GPIO.output(11, False)
    elif mode == "on":
        GPIO.output(11, True)
    elif mode == "report":
        for i in range(3):
            GPIO.output(11, True)
            sleep(3)
            GPIO.output(11, False)
            sleep(1)
        state = "off"

tree_light("on")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(mqtt_broker, 1883, 300)
    client.loop_start()
    while True:
           sleep(5)
except KeyboardInterrupt:
    print "exit"
    client.loop_stop()

