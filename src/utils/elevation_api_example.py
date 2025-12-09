import requests
import numpy as np
import json

import matplotlib.pyplot as plt

# locations: List of locations, separated by | in latitude, longitude format, similar to the Google Elevation API.
# curl 'https://api.open-elevation.com/api/v1/lookup?locations=10,10|20,20|41.161758,-8.583933'


center_lat, center_lon = 41.161758, -73.923
# my coordinates {"results":[{"latitude":41.161758,"longitude":-8.583933,"elevation":117.0}]} 

span = 0.02
n_points = 20

lats = np.linspace(center_lat - span, center_lat + span, n_points)
lons = np.linspace(center_lon - span, center_lon + span, n_points)
coords = [{"latitude": lat, "longitude": lon} for lat in lats for lon in lons]
print(f"type data {type(coords)}")


url = "https://api.open-elevation.com/api/v1/lookup"
print("Retrieving elevation data")
response = requests.post(url, json={"locations": coords})
response.raise_for_status()
data = response.json()
print(f"type data {type(data)}")