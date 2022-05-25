import time
import dht
from machine import Pin

def measure_dht22():
    sensor = dht.DHT22(Pin(27))
    #time.sleep(2) # only needed if run continuously

    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity} %")
        return [temperature, humidity]
    
    except Exception as e:
        print(e)
        return e

if __name__ == "__main__":
    print(measure_dht22())