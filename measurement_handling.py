import json
import requests
import wifi

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
      
    print(json_object)
    print(type(json_object))
    # json_object is of type list which contains dictionaries
    return json_object
    
def write_json(x):

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
    
        
        
def send_measurement(x):
    """
    dont forget to delete sent measurements
    """
    measurements = read_json()
    for m in measurements:
        try:
            # send measurements
            r = requests.post(server_ip, json=m)
            r.status_code
            # if successful, delete the measurement from the list
            # if sending is unsuccessful write all remaining measurements back to the file
            
            measurements.remove(m)
            pass
        except Exception as e:
            # if an expection happenes during sending, write all remaining measurements back to the file
            # and break 
            write_json(measurements)
            break
    pass

if __name__ == "__main__":
    # read_json()
    # write_json(measurement_example)
    add_measurement(measurement_example)