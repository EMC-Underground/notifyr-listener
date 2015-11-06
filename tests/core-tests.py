import json

with open('config.json') as data_file:
  config = json.load(data_file)

def test_call():
  url = "https://api.particle.io/v1/devices/events/"
  headers = {'Authorization': 'Bearer {0}'.format(config["token"]),
                'Content-Type': 'application/x-www-form-urlencoded'}
  payload = {'name':'TestingTheNotifyrCode', 'data':'This is a test'}
  r = requests.post(url, headers=headers, params=payload)
  # data = "name=TestingTheNotifyrCode&data=This is a test"
  response = r.json()
#  if response["ok"] == "true":
#    return 0
