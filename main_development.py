import time
import wifi
import test_urequests
import uping
import pump
import sensors
import measurement_handling

development = True
"""
# only pump
def main():
    
    while True:
        pump.pump(60, 60, False)
        
# do everything
"""
def main():
    sent_since_measurement = False
    wifi.connect()

    while True:
        pump.pump(60, 0, dev=development)
        
        measurements = sensors.measure_all()
        print(measurements)
        measurement_handling.write_json(measurements)
        
        for x in range(12):
            #check if not sent_since_measurement
            #check if internet connected, if not try reconnecting
            # if connected, send measurements
            # if no more measurements in MEASUREMENT.py set sent_since_measurement = True
            # wait for 5 min
            measurement_handling.send_json("a")
            time.sleep(5*60)
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