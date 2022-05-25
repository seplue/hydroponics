import wifi
import test_urequests
import uping
import pump

development = True

wifi.connect()
pump.pump(dev=development)

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