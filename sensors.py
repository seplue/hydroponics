import time
import dht
import BME280
from machine import Pin, ADC

# setup Pins
# sensor = dht.DHT22(Pin(32))
sensor = dht.DHT22(Pin(23))  # testing

adc_pin = Pin(39)
adc = ADC(adc_pin)
adc.atten(adc.ATTN_11DB)

def measure_dht22(dev=0):
    # todo discard the first reading? It is sometimes inaccurate
    
    #time.sleep(2) # only needed if run continuously
    if dev: time.sleep(2)

    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        # todo round values, humidity sometimes displays 62.10001
        # is already rounded, ->floating point inaccuracy
        # alternatively use decimal
        
        if dev == 1:
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity} %")
        return {'temperature' : temperature, 'humidity' : humidity}
    
    except Exception as e:
        print(e)
        return {'temperature' : None, 'humidity' : None}
    


def measure_light_intensity(dev=0):
    try:
        val = adc.read()
        val = val * (3.3 / 4095)
        val = round(val, 2)
        
        if dev == 1: print(val)
        return {'light_intensity': val}
    except Exception as e:
        print(e)
        return {'light_intensity': None}
def measure_all():
    measurements = {}
    # print(measurements)
    measurement_dht22 = measure_dht22()
    # print(measurement_dht22)
    measurement_light_intensity = measure_light_intensity()
    # print(measurement_light_intensity)
    measurements.update(measurement_dht22)
    measurements.update(measurement_light_intensity)
    measurements.update({'time_utc': None})
    
    # if using BME280:
    measurement_bme280 = BME280.return_measurement()
    measurements.update(measurement_bme280)
    
    return measurements
    


if __name__ == "__main__":
    while True:
        print(measure_all())
        # print(measure_dht22())
        time.sleep(2)
    