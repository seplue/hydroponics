import time
import wifi
import test_urequests
import uping
import pump
import sensors
import measurement_handling
from machine import Pin

development = True
led_orange=Pin(26,Pin.OUT)

# only pump
"""def main():
    
    while True:
        led_orange.on()
        pump.pump(30, 0, False)
        led_orange.off()
        time.sleep(60)
"""      
# do everything

def main():
    sent_since_measurement = False
    time_checked = False
    wifi.connect()

    while True:
        pump.pump(60, 0, dev=development)
        
        measurements = sensors.measure_all()
        print(f"measurement made: {measurements}")
        measurement_handling.add_measurement(measurements)
        sent_since_measurement = False
        
        for x in range(12):
            #check if not sent_since_measurement
            if not sent_since_measurement:
                #check if internet connected, if not try reconnecting
                wifi.connect()
                measurement_handling.send_measurement()
            
            # if connected, send measurements
            # if no more measurements in MEASUREMENT.py set sent_since_measurement = True
            # wait for 5 min
            print("waiting for 5 min")
            time.sleep(5)
"""
"""


"""
connect to wifi
    get internet time
measure
pump
measure

for next 1h:
    try to connect to wifi every x min
    if successful:
        send data
        update clock


"""
main()