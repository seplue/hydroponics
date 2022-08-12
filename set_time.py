import time
import ntptime
import wifi


def update_time():
    try:
      print("Local time before synchronization：%s" %str(time.localtime()))
      #make sure to have internet connection
      ntptime.settime()
      print("Local time after synchronization：%s" %str(time.localtime()))
    except:
      print("Error syncing time")



if __name__ == "__main__":
    wifi.connect()
    update_time()

    
