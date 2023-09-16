# This file will be utilized as a way to provide information on the bus route and location

import requests
from BTAPI import *
from smsTwilio import *
import datetime
from maps import *

# Route Data
# ToDo: Create a list of bus stops in the order of the route
route = [1114, 1104, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1115,
         1116, 1123, 1124, 1125, 1100]
# ToDo: Create a dictionary of bus stops and their locations
stopLoc = {1114: (37.22978, -80.41997), 1104: (37.23148,-80.42159),1300:(37.23438,-80.42564),1301:(37.23438,-80.42564),
           1302:(37.2348, 80.4259), 1303:(37.2403, 80.4271),1304:(37.2415, 80.4257),1305:(37.2424, 80.4222),1306:(37.2442, 80.4215),
           1307:(37.2452, 80.4215), 1308:(37.2449, 80.4252), 1309:(37.2438, 80.4280), 1310:(37.2431,80.4298),1311:(37.2422, 80.4334),
           1312:(37.2422, 80.4334), 1313:(37.2373, 80.4350), 1314:(37.2358, 80.4342), 1315:(37.2342, 80.4334), 
           1115:(37.22683, -80.42617), 1116:(37.2216,-80.424),1123:(37.22069, -80.4223),1124:(37.22245, -80.41893),
           1125:(37.2239, 80.4169),1100:(37.22876, -80.41924)}

targetStop = 1313


def routeInfo(curStop, curPos, targetStop):
    # Defining the circular bus route as a list of the stop sequences
    circular_bus_route = [1114, 1104, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 
        1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1115, 1116,
        1123, 1124, 1125, 1100, 1114]  # Circular route back to 1114
    
    # Check if the current and target stops are valid
    if curStop not in circular_bus_route or targetStop not in circular_bus_route:
        return "Invalid current or target stop"

    # Find the waypoints from the current stop to the target stop
    cur_index = circular_bus_route.index(curStop)
    target_index = circular_bus_route.index(targetStop)

    # Find the bus route
    # Create an array of waypoints 
    return


if __name__ == "__main__":
    all_buses = get_all_bus_info()
    for bus in all_buses:
        if bus['routeId'] == 'TOM':
            real_time_info = bus["states"][0]
            print(
                f"Bus {bus['routeId']} is at {real_time_info['realtimeLatitude']}, {real_time_info['realtimeLongitude']}, going {real_time_info['speed']} mph."
            )
            # ToDo: Make the method below function properly
            routeInfo(bus['stopId'], (real_time_info['realtimeLatitude'], real_time_info['realtimeLongitude']), targetStop)
            
            
    
    # check if weekend or weekday
    
    
    if datetime.datetime.today().weekday() < 5:
        # weekday
        print("Weekday")
        
    else:
        # weekend
        print("Weekend")
    
    
    
