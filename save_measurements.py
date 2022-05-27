import json

measurement_example = {
    'temperature' : 23.1,
    'humidity' : 60.0,
    'light': 0.7,
    'time_utc': 0,
    }

def save(x):
    pass

# Python program to write JSON
# to a file


import json

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary)

# Writing to sample.json
with open("MEASUREMENTS.py", "w") as outfile:
	outfile.write(json_object)
