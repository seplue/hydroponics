import time
import set_time
import wifi
import pump
import sensors
import measurement_handling
from machine import Pin

development = False


# continuously pump
def main():
    while True:
        pump.pump(1, 60, False)
    


"""
# do everything
def main():
    # setup: try to connect to wifi and update internet time
    wifi.connect()
    set_time.update_time()

    # main loop
    while True:
        # pump
        pump.pump(60, 0, dev=development)
        
        # create measurement (without added time)
        measurement = sensors.measure_all()
        print(f"measurement made: {measurement}")
        measurement_handling.add_measurement(measurement)
        sent_since_measurement = False
        
        # sending measuerements
        # over the one hour until next pumping
        for x in range(12):
            #check if not sent_since_measurement
            if not sent_since_measurement:
                #check if internet connected, if not try reconnecting
                wifi.connect()
                # if connected, send measurements
                measurement_handling.send_measurements()
            # if no more measurements in MEASUREMENT.py set sent_since_measurement = True
            if measurement_handling.number_of_measurements_saved() == 0:
                sent_since_measurement = True
                
            # wait for 5 min
            print("waiting for 5 min")
            time.sleep(5) #5*60 for 5 min

"""
if __name__ == "__main__":
    main()
