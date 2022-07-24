import time
import dht
from machine import Pin, ADC

# setup Pins
sensor = dht.DHT22(Pin(32))

adc_pin = Pin(39)
adc = ADC(adc_pin)
adc.atten(adc.ATTN_11DB)

def measure_dht22(dev=0):
    #time.sleep(2) # only needed if run continuously
    if dev: time.sleep(2)

    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        # todo round values, humidity sometimes displays 62.10001
        
        if dev == 1:
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")
        return {'temperature' : temperature, 'humidity' : humidity}
    
    except Exception as e:
        print(e)
        return None
    


def measure_light(dev=0):
    val = adc.read()
    val = val * (3.3 / 4095)
    val = round(val, 2)
    
    if dev == 1: print(val)
    return {'light': val}

def measure_all():
    measurements = {}
    # print(measurements)
    measurement_dht22 = measure_dht22()
    # print(measurement_dht22)
    measurement_light = measure_light()
    # print(measurement_light)
    measurements.update(measurement_dht22)
    measurements.update(measurement_light)
    
    return measurements
    


if __name__ == "__main__":
    while True:
        print(measure_all())
        time.sleep(2)
    