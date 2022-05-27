import urequests
import wifi

url = 'http://127.0.0.1:5000/test_put'
url = 'https://catfact.ninja/fact'
url = 'http://echo.jsontest.com/title/ipsum/content/blah'


if __name__ == "__main__":       
    wifi.connect()
    
    """
    response = urequests.get(url)
    print(response.text)
    """
    
    res = urequests.get(url, json={"mytext":"lalala"})
    print(res.json())
        
    print('end')
