import time
import dht
from machine import Pin, ADC

# setup Pins
sensor = dht.DHT22(Pin(27))

adc_pin = Pin(39)
adc = ADC(adc_pin)
adc.atten(adc.ATTN_11DB)

def measure_dht22(dev=0):
    #time.sleep(2) # only needed if run continuously

    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        if dev == 1:
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")
        return {'temperature' : temperature, 'humidity' : humidity}
    
    except Exception as e:
        print(e)
        return e
    


def measure_light(dev=0):
    val = adc.read()
    val = val * (3.3 / 4095)
    val = round(val, 2)
    
    if dev == 1: print(val)
    return val

def measure_all():
    measurements = measure_dht22()
    measurements['light'] = measure_light()
    
    return measurements
    


if __name__ == "__main__":
    measure_dht22(dev=1)
    measure_light(dev=1)
    time.sleep(2)
    print(measure_all())