import requests

url = 'http://192.168.1.4:11233/child'
data1 = {
    'id': '89263805014',
    'accuracy': 0,
    'altitude': 0,
    'altitudeAccuracy': 0,
    'heading': 0,
    'speed': 0,
    'timeStamp': 123456,
    'latitude': '1',
    'longitude': 23456
    }
data = {'phone': '89261234544', 'type': 0}
response = requests.post(url, data=data1)
print(response.text)
print(response.status_code)