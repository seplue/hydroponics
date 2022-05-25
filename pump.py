"""

"""
import time
from machine import Pin

def pump(duration=60, interval=60, dev=False):
    # set up time (duration in sec, interval in min)
    interval = interval*60
    if dev: # if in development mode, make it faster
        duration = duration/60
        interval = interval/360
        duration = 3
        interval = 10
        
    pin_pump = Pin(21, Pin.OUT)
    
    print("pump start")
    pin_pump.on()
    time.sleep(duration)
    pin_pump.off()
    print("Pump end")
    
if __name__ == "__main__":
    pump(dev=True)