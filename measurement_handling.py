import json
import urequests as requests
import wifi
from CREDENTIALS import server_ip

file_name = 'MEASUREMENTS.py'

measurement_example = {
    'time_utc': 0,
    'temperature' : 23.1,
    'humidity' : 60.0,
    'light_intensity': 0.7
    }


def read_json():
    # general function to open and read json file
    
    # Opening JSON file
    with open(file_name, 'r') as openfile:
      
        # Reading from json file
        json_object = json.load(openfile)
      
    # print(json_object)
    # print(type(json_object))
    # json_object is of type list which contains dictionaries
    return json_object
    
def write_json(x):
    # check if x is list, if not put x in a list
    if isinstance(x, list):
        pass
    else:
        x = [x]
    
    # Serializing json
    json_object = json.dumps(x)

    # Writing to sample.json
    with open(file_name, 'w') as outfile:
        outfile.write(json_object)
        
        
def add_measurement(x):
    measurements = read_json()
    print(measurements)
    
    measurements.append(x)
    print(measurements)
    
    write_json(measurements)
    
        
        
def send_measurement():
    print("started send_measurement()")
    """
    dont forget to delete sent measurements
    """
    measurements = read_json()
    print(type(measurements))
    print(measurements)
    for m in list(measurements):
        try:
            # send measurements
            r = requests.post(server_ip, json=m)
            # if successful, delete the measurement from the list
            # if sending is unsuccessful write all remaining measurements back to the file
            
            print(f"Status code is {r.status_code}")
            if r.status_code == 200:
                measurements.remove(m)    

        except Exception as e:
            # if an expection happenes during sending, write all remaining measurements back to the file
            # and break 
            write_json(measurements)
    # write the list back to file (this also empties the file in case all measurements were successfully sent)
    write_json(measurements)   


if __name__ == "__main__":
    #write_json(measurement_example)
    #read_json()
    send_measurement()
    # add_measurement(measurement_example)