import requests

headers = {
    "Host": "www.ridebt.org",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.ridebt.org",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Referer": "https://www.ridebt.org/",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Content-Type": "json",
}


def get_all_bus_info():
    params = {
        "option": "com_ajax",
        "module": "bt_map",
        "format": "json",
        "Itemid": "101",
        "method": "getBuses",
    }

    response = requests.post(
        "https://www.ridebt.org/index.php", params=params, headers=headers
    )
    return response.json()["data"]


def get_route_info(bus_name):
    params = {
        "option": "com_ajax",
        "module": "bt_map",
        "format": "json",
        "Itemid": "101",
        "method": "getPatternPoints",
        "patternName": bus_name,
    }

    response = requests.post(
        "https://www.ridebt.org/index.php", params=params, headers=headers
    )
    return response.json()["data"]


all_buses = get_all_bus_info()

for bus in all_buses:
    real_time_info = bus["states"][0]
    print(
        f"Bus {bus['routeId']} is at {real_time_info['realtimeLatitude']}, {real_time_info['realtimeLongitude']}, going {real_time_info['speed']} mph."
    )