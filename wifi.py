from CREDENTIALS import network_list
import network
import time

sta_if = network.WLAN(network.STA_IF)

def connect(stay_active=True, dev=False):
    if sta_if.isconnected() == True:
        print(f'already connected to {sta_if.config('essid')}')
        
    else:
        # activate wifi in station modus
        sta_if.active(True)
        # scan and create list of available wifi connections
        print('scanning available wifi networks')
        scan = sta_if.scan()
        scan_list = []
        for x in scan:
            scan_list.append(x[0].decode('utf-8'))
        print(scan_list)
         
        # try to connect to every network in CREDENTIALS.py if it is in scan_list
        for network in network_list:
            if network[0] in scan_list:
                try:        
                    print(f'trying to connect to: {network[0]}')
                    sta_if.connect(network[0], network[1])
                except Exception as e:
                    print(e)
                    
                for x in range(10):
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
                    pass
            else:
                print(f'{network[0]} not available')

        if not stay_active:
            sta_if.active(False)
            
            
        
if __name__ == "__main__":
    connect(dev=True, stay_active=False)
