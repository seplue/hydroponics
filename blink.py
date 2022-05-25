import time
"""
Pin13: internal led
Pin27
Pin33: red led
Pin15: orange led
Pin32: green led
"""
def blink4():
    from machine import Pin
    led1=Pin(13,Pin.OUT)
    led2=Pin(33,Pin.OUT)
    led3=Pin(15,Pin.OUT)
    led4=Pin(32,Pin.OUT)
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
