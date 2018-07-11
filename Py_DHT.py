import sys
import Adafruit_DHT
import time
import requests
import json



url = 'http://52.199.28.120:8080/Thingworx/Things/work_thing/Properties/temp'

url1 = 'http://52.199.28.120:8080/Thingworx/Things/work_thing/Properties/hum'

headers = {
    'Content-Type': 'application/json',
    'appkey': '697ad1c3-ecef-41ba-8fb9-74d34ab34c15',
    'Accept': 'application/json',
    'x-thingworx-session': 'true',
    'Cache-Control': 'no-cache',
}



while True:

    print '\n\n\nUploding Temperature and Humidity: \n '
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'type of data', humidity
    print 'type of data', type(temperature)
    data = {
            "hum": humidity,
            "temp": temperature}
    #json_data = json.dumps(data)
    #r = requests.post('http://192.168.0.8:1880/payload',json_data)
    res2 = requests.put(url, headers=headers, json=data)
    print res2.status_code, res2.content
    res1 = requests.put(url1, headers=headers, json=data)
    print res1.status_code, res1.content
    print(humidity,temperature)
    print '\nDone Uploading!'
    #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} % '.format(temperature, humidity)
    time.sleep(10)










