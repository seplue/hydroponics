import time
import wifi
import test_urequests
import uping
import pump
import sensors
import measurement_handling
from machine import Pin
           
def main_hiking():
    while True:
        measurements = sensors.measure_all()
        print(f"measurement made: {measurements}")
        measurement_handling.add_measurement(measurements, always_check_time=False)
        # time.sleep(60*5)
        time.sleep(6)

main_hiking()
