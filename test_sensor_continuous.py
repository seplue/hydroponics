import sensor
import time

wrong_responses = 0
correct_responses = 0

while True:
    response = sensor.measure_dht22() 
    if type(response) == list:
        correct_responses = correct_responses+1
    elif type(response) == OSError:
        wrong_responses = wrong_responses+1
    else:
        pass
    print(f'wrong responses: {wrong_responses}')
    print(f'correct responses: {correct_responses}')
    time.sleep(2)