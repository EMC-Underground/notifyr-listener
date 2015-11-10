from sseclient import SSEClient
import json, requests, atexit, os

# Start collecting stream from the particle cloud
messages = SSEClient('{0}/notifyr?access_token={1}'
                       .format(os.environ['PARTICLE-URL'],os.environ['TOKEN']))

for msg in messages:
  # When the event is found
  if msg.event == os.environ['EVENT']:

    # Grab the event data
    dataJson = json.loads(msg.data)

    # Set the url for the google sheet
    url = os.environ['GOOGLE-SHEET-URL']

    # Specify the spread sheet value
    payload = {'Core_ID':'{0}'.format(dataJson["coreid"]),
               'Core_Data':'{0}'.format(dataJson["data"])}

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
    # print(dataJson["data"])
