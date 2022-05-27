import time
import wifi
import test_urequests
import uping
import pump
import sensors
import save_measurements
import send_measurements

development = True

wifi.connect()

pump.pump(dev=development)
measurements = sensors.measure_all()
save_measurements.save(measurements)

for x in range(12):
    send_measurements.send("a")
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