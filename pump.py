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
        
    pin_pump = Pin(2, Pin.OUT)
    
    pin_pump.on()
    time.sleep(duration)
    pin_pump.off()
    
if __name__ == "__main__":
    pump(dev=True)