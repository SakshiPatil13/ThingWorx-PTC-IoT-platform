import requests
import json

url = 'http://52.199.28.120:8080/Thingworx/Things/work_thing/Properties/temp'

url1 = 'http://52.199.28.120:8080/Thingworx/Things/work_thing/Properties/value1'
headers = {
    'Content-Type': 'application/json',
    'appkey': '516a7ace-8c01-4744-8640-08226e3fcc3a',
    'Accept': 'application/json',
    'x-thingworx-session': 'true',
    'Cache-Control': 'no-cache',
}

data = {
	"temp": 100
}

res1 = requests.put(url1, headers=headers)
print res1.status_code, res1.content

print '------------------------------------'
res2 = requests.put(url, headers=headers, json=data)
print res2.status_code, res2.content
