from machine import Pin, ADC
from time import sleep

adc_pin = Pin(39)
adc = ADC(adc_pin)
adc.atten(adc.ATTN_11DB)

def measure_light(dev=0):
    val = adc.read()
    val = val * (3.3 / 4095)
    val = round(val, 2)
    
    if dev == 1: print(val)
    return val

if __name__ == "__main__":
    measure_light(dev=1)
        