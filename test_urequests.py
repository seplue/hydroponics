import urequests as requests
import wifi
import json

server_ip = 'http://192.168.43.106:5000/test_put'
# server_ip = 'http://httpbin.org/anything'
my_dict = {'my_key': 'my_value'}


if __name__ == "__main__":
    wifi.connect()
    r = requests.post(server_ip, json=my_dict)
    print(r)
    print(r.content)
    print(r.json)
    print(dir(r))

    print('script end')