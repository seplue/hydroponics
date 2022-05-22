import time

def blink():
    from machine import Pin
    led=Pin(2,Pin.OUT)
    print("Programm gestartet")
    while True:
        led.on()
        print("an")
        time.sleep_ms(500)
        led.off()
        print("aus")
        time.sleep_ms(500)
      
if __name__ == "__main__":
    blink()
