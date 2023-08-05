import time
import ntptime
import wifi
# if connected to thonny, thonny initializes esp with local time (not utc)!

def update_time():
    try:
        ntptime.settime()
    except Exception as e:
        print(e)
    finally:
        print(time.localtime())


if __name__ == "__main__":
    #wifi.connect()
    #print(time.localtime())
    update_time()
    # to print localtime
    # print(time.localtime(time.mktime(time.localtime()) + 2*3600))

    
