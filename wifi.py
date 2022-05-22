from CREDENTIALS import network_list
import network
import time
import uping

sta_if = network.WLAN(network.STA_IF)

def connect(stay_active=True):

    
    sta_if.active(True)
    print(sta_if.scan())

    for network in network_list:
        try:        
            print('trying to connect to')
            print(network)
            sta_if.connect(network[0], network[1])
        except Exception as e:
            print(e)
            
        for x in range(5):
            time.sleep(1)
            status = sta_if.isconnected()
            print(status)
            if status == True:
                break
            else:
                pass
        if sta_if.isconnected() == True:
            break
        else:
            sta_if.disconnect()

    print(uping.ping('1.1.1.1'))
    print(sta_if.config('essid'))
    #sta_if.active(False)
