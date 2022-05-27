import time
"""
Pin2: internal led (blue)
Pin25: red led
Pin26: orange led
Pin27: green led
"""
def blink4():
    from machine import Pin
    led1=Pin(2,Pin.OUT)
    led2=Pin(25,Pin.OUT)
    led3=Pin(26,Pin.OUT)
    led4=Pin(27,Pin.OUT)
    print("Programm gestartet")
    while True:
        led1.on()
        led2.off()
        led3.on()
        led4.off()
        print("an")
        time.sleep_ms(500)
        led1.off()
        led2.on()
        led3.off()
        led4.on()
        print("aus")
        time.sleep_ms(500)
def blink():
    from machine import Pin
    led=Pin(15,Pin.OUT)
    print("Programm gestartet")
    while True:
        led.on()
        print("an")
        time.sleep_ms(500)
        led.off()
        print("aus")
        time.sleep_ms(500)
      
if __name__ == "__main__":
    blink4()
