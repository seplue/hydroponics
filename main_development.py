import time
import wifi
import test_urequests
import uping
import pump
import sensors
import measurement_handling

development = True

wifi.connect()

pump.pump(dev=development)
measurements = sensors.measure_all()
measurement_handling.write_json(measurements)
print(sensors.measure_all())

for x in range(12):
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