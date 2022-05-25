import time
import ntptime
import wifi


def update_time():
    ntptime.settime()



if __name__ == "__main__":
    wifi.connect()
    
    print(time.localtime())    
    print(time.localtime())
    update_time()

    print(time.localtime(time.mktime(time.localtime()) + 2*3600))

    print(time.localtime())
    
