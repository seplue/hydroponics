import urequests as requests
import wifi
import json

server_ip = 'http://192.168.43.106:5000/measurement'
# server_ip = 'http://httpbin.org/anything'
my_dict = {'my_key': 'my_value'}
measurement_example = {
    'time_utc': 0,
    'temperature' : 23.1,
    'humidity' : 60.0,
    'light_intensity': 0.7
    }


if __name__ == "__main__":
    wifi.connect()
    r = requests.post(server_ip, json=measurement_example)
    print(r.status_code)
    print(r.content)
    print(r.json)
    print(dir(r))

    print('script end')