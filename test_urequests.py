import urequests
import wifi
wifi.connect()

url = 'https://catfact.ninja/fact'

response = urequests.get(url)
print(response.text)