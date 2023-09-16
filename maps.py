import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os

# Replace with your own API key
load_dotenv()

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_MAPS'))

def getDirections(origin, destination):
    # Get directions and estimate travel time
    directions = gmaps.directions(
        origin,
        destination,
        mode="driving",  # You can change the mode to "walking", "transit", or others as needed
        departure_time=datetime.now(),
    )

    if directions:
        duration = directions[0]["legs"][0]["duration"]["text"]
        print(f"Estimated travel time: {duration}")
    else:
        print("No directions found.")
        
    return directions

if __name__ == "__main__":
    # Define the origin and destination coordinates
    # Replace with your origin coordinates (latitude, longitude)
    origin = (40.7128, -74.0060)
    # Replace with your destination coordinates
    destination = (40.730610, -73.935242)
    
    getDirections(origin, destination)
