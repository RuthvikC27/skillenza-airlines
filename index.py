import json
import math

# FORMAT'S DATA
def format_data(arr):
    return [arr[0], (arr[1] + "," + arr[2]).replace('"', ""), arr[3], arr[4]]

# SAVES AND PRINT THE AIRPORTS AND THEIR COUNTS TO JSON FILE
def airports_counts(filename):
    airport_count = {}

    with open(filename, 'r') as file:
        for line in file.readlines():
            airport = line.split(",")

            if(airport[0] == 'Airport.Code'):
                continue
            
            # print(format_data(airport))

            airport = format_data(airport)
            if( airport[1] not in airport_count.keys() ):
                airport_count[airport[1]] = 1
            else:
                airport_count[airport[1]] = airport_count[airport[1]] + 1
    
    with open("count.json", 'w') as file:
        json.dump(airport_count, file, indent=4, sort_keys=True)

        print(json.dumps(airport_count, indent=4, sort_keys=True))
    
    return airport_count

# PRINTS THE MOST COUNTED AIRPORT PLUS IT'S COUNT
def most_counted(airport_count):
    max_val = max(airport_count.values())
    key = find_by_val_dict(max_val, airport_count)

    print(key, max_val)

# PRINTS THE LEAST COUNTED AIRPORT PLUS IT'S COUNT
def least_counted(airport_count):
    min_val = min(airport_count.values())
    key = find_by_val_dict(min_val, airport_count)

    print(key, min_val)

# FIND THE AIRPORT NAME WITH MOST COUNT AND LEAST COUNT
def find_by_val_dict(val, airport_count):

    for airport in airport_count.keys():
        if(airport_count[airport] == val):
            return airport
    
    return None

# PROGRAM EXECUTION STARTS FROM HERE
if __name__ == "__main__":

    airport_count_dict = airports_counts("airlines.csv")

    most_counted(airport_count_dict)
    least_counted(airport_count_dict)

    
    
