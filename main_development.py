import wifi
import test_urequests
import uping
import pump

development = True

wifi.connect()
pump.pump(dev=development)