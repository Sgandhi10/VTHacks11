# This file will be utilized as a way to provide information on the bus route and location

import requests
from BTAPI import *
from smsTwilio import *
import datetime
from maps import *
import time
from char_lcd import *

# Route Data
# ToDo: Create a list of bus stops in the order of the route
route = [1114, 1104, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1115,
         1116, 1123, 1124, 1125, 1100]
# ToDo: Create a dictionary of bus stops and their locations
stopLoc = {1114: (37.22978, -80.41997), 1104: (37.23148, -80.42159), 1300: (37.23438, -80.42564), 1301: (37.23438, -80.42564),
           1302: (37.2348, -80.4259), 1303: (37.2403, -80.4271), 1304: (37.2415, -80.4257), 1305: (37.2424, -80.4222), 1306: (37.2442, -80.4215),
           1307: (37.2452, -80.4215), 1308: (37.2449, -80.4252), 1309: (37.2438, -80.4280), 1310: (37.2431, -80.4298), 1311: (37.2422, -80.4334),
           1312: (37.2422, -80.4334), 1313: (37.2373, -80.4350), 1314: (37.2358, -80.4342), 1315: (37.2342, -80.4334),
           1115: (37.22683, -80.42617), 1116: (37.2216, -80.424), 1123: (37.22069, -80.4223), 1124: (37.22245, -80.41893),
           1125: (37.2239, -80.4169), 1100: (37.22876, -80.41924)}

targetStop = 1313


def routeInfo(curStop: int, targetStop: int):
    # Check if the current and target stops are valid
    if curStop not in route or targetStop not in route:
        return "Invalid current or target stop"

    # Find the waypoints from the current stop to the target stop
    cur_index = route.index(curStop)
    target_index = route.index(targetStop)

    # Find the bus route
    # Create an array of waypoints
    return route[cur_index:target_index+1] if cur_index < target_index else route[cur_index:] + route[:target_index+1]


def getClosestBus(_route, targetStop):
    all_buses = get_all_bus_info()
    waypoints = []
    capacity = 0
    closerBus = None
    for bus in all_buses:
        if bus['routeId'] == _route:
            real_time_info = bus["states"][0]
            print(
                f"Bus {bus['routeId']} is at {real_time_info['realtimeLatitude']}, {real_time_info['realtimeLongitude']}, going {real_time_info['speed']} mph."
            )
            # ToDo: Make the method below function properly
            route = routeInfo(
                (int)(bus['stopId']),
                (int)(targetStop))
            twaypoints = [((float)(real_time_info['realtimeLatitude']), (float)(
                real_time_info['realtimeLongitude']))] + [stopLoc[stop] for stop in route[1:]]
            print(twaypoints)
            if len(waypoints) == 0 or len(twaypoints) < len(waypoints):
                closerBus = bus
                waypoints = twaypoints

    totalTime = 0
    for i in range(len(waypoints)-1):
        time = getDirections(waypoints[i], waypoints[i+1])
        if time == -1:
            print("No directions found.")
            continue
        totalTime += time
        print(time)
    print(totalTime)
    capacity = (int)(closerBus['capacity'])
    return totalTime, capacity, len(waypoints)


def main():
    bRoute = "TOM"
    targetStop = 1313
    totalTime, capacity, numWaypoints = getClosestBus(bRoute, targetStop)
    print(totalTime, capacity, numWaypoints)
    displayData((str)(round(totalTime/60)) + " mins", (str)(100 - capacity))
    if totalTime > 300:
        sendSMS('+19732166660',
                f"Bus {bRoute} is {round(totalTime/60)} minutes away from your stop. Availability is {100 - capacity}%.")
        while totalTime > 300:
            time.sleep(max((totalTime - 300) * .75, 30))
            totalTime, capacity, numWaypoints = getClosestBus(
                bRoute, targetStop)

            totalTime *= 1.2  # Bus tends to move slower
            totalTime += 30 * \
                numWaypoints if capacity > 50 else 0  # Bus tends to stop longer
            print(totalTime, capacity, numWaypoints)
        sendSMS(
            '+19732166660', f"Bus {bRoute} is {round(totalTime/60)} minutes away from your stop. Availability is {100 - capacity}%.")
    else:
        print(totalTime, capacity, numWaypoints)


if __name__ == "__main__":
    while True:
        if buttonPressed():
            main()

