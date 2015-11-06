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
    url = config["google-sheet-url"]
    payload = {'Core_ID':'{0}'.format(dataJson["coreid"]),
                'Core_Data':'{0}'.format(dataJson["data"])}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
    # print(dataJson["data"])

  if msg.event == "TestingTheNotifyrCode":
    print("OK!")
