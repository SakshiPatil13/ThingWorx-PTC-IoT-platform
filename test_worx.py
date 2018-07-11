import requests  # Import requests library to send requests to Thingworx

url = 'http://52.199.28.120:8080/Thingworx/Things/MyThing/Properties/Temp'
url = 'http://52.199.28.120:8080/Thingworx/Things/MyThing/Properties/Hum'

# temp is one of my property name
value1 = 36    # Upload 12 on Thingworx
value2 = 10 

headers = {
    'Content-Type': 'application/json',
    'appkey': '697ad1c3-ecef-41ba-8fb9-74d34ab34c15',
    'Accept': 'application/json',
    'x-thingworx-session': 'true',
    'Cache-Control': 'no-cache',
}

data = {"Temp": value1, "Hum" : value2}   # JSON data to upload on Thingworx

response = requests.put(url, headers=headers, json=data)
# Note that we have to send put request

print 'Response Code:', response.status_code
# If 200 then data has been uploaded successfully
print 'Response Content:', response.content
