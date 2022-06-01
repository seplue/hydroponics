import urequests
import wifi
import measurement_handling
import json


url_put = 'http://127.0.0.1:5000/test_put'
url = 'https://catfact.ninja/fact'
url = 'http://echo.jsontest.com/title/ipsum/content/blah'


def test_get(url):
    response = urequests.get(url)
    print(response.text)


def test_put(url):
    res = urequests.put(url, json={"mytext":"lalala"})
    print(res)
    print(res.json())
    
    
def put_json(json):
    res = urequests.put(url_put, json)
    #print(res)
    #print(res.json())
    
def request_put(urlu_put, my_json):
    urequests.request('PUT', url_put, json=my_json)



if __name__ == "__main__":       
    wifi.connect()
#        test_get(url)
#        test_put(url_put)
    #put_json(measurement_handling.measurement_example)
    request_put(url_put, json.dumps(measurement_handling.measurement_example))

    print('end')
