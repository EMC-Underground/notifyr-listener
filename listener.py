from sseclient import SSEClient
from flask import Flask, url_for, request, jsonify
import json, requests, atexit

with open('config.json') as data_file:
  config = json.load(data_file)

messages = SSEClient('{0}/notifyr?access_token={1}'
                        .format(config["particle-url"],config["token"]))

for msg in messages:
  #event = str(msg.event).encode('ascii', 'ignore').decode('ascii')
  #data = str(msg.data).encode('ascii', 'ignore').decode('ascii')
  #print(event)
  #print(data)
  # print(msg.event)
  if msg.event == "notifyr/announce":
    # print(msg.data)
    dataJson = json.loads(msg.data)
    # print(dataJson["data"])

  if msg.event == "TestingTheNotifyrCode":
    print("CONFIRMED")
