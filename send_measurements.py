# Python program to read JSON
# from a file

def send(x):
    pass
  
  
import json
  
# Opening JSON file
with open('MEASUREMENTS.py', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
print(json_object)
print(type(json_object))
print(json_object['cgpa'])