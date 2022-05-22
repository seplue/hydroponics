import urequests
import wifi

if __name__ == "__main__":       
    wifi.connect()
    url = 'https://catfact.ninja/fact'
    response = urequests.get(url)
    print(response.text)
