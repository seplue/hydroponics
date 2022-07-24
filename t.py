import time

while True:
    for x in range(100):
        time.sleep(0.1)
        if x%2 == 0:
            print(f'{x} is divisible by 2')
        else:
            pass