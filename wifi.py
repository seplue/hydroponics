from CREDENTIALS import network_list
import network
import time

sta_if = network.WLAN(network.STA_IF)

def connect(stay_active=True, dev=False):
    if sta_if.isconnected() == True:
        print(f'already connected to {sta_if.config('essid')}')
        
    else:
        sta_if.active(True)
        print(sta_if.scan())

        for network in network_list:
            try:        
                print(f'trying to connect to: {network}')
                sta_if.connect(network[0], network[1])
            except Exception as e:
                print(e)
                
            for x in range(5):
                time.sleep(1)
                status = sta_if.isconnected()
                print(f'connection status: {status}')
                if status == True:
                    break
                else:
                    pass
            if sta_if.isconnected() == True:
                print(f"connected to: {sta_if.config('essid')}")
                break
            else:
                sta_if.disconnect()

        if not stay_active:
            sta_if.active(False)
            
            
        
if __name__ == "__main__":
    connect(dev=True)
