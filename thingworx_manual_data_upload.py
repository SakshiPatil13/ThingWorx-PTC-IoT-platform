import requests
import json

api_key = 'f9fc2bec-1724-4f29-bacf-9fd0f86136a6'
headers = {'Content-Type': 'application/json', 'appKey': api_key}

#payload = { 'lmtech_thing' : 12}
#url2 = 'http://52.201.57.6/Thingworx/Things/lmtech_thing/Properties/12 appKey==1645ab09-4dd5-48c4-99f7-df05449324da 12'
thingworx_url = 'http://PP-1804040542ZE.Devportal.Ptc.Io8080/Thingworx/Things/lmtech_thing/Properties appKey==1645ab09-4dd5-48c4-99f7-df05449324da'
print 'getting the value'
#response = requests.get(thingworx_url, headers=headers, json=payload, verify=False)
response = requests.get(thingworx_url)
print 'res', response
