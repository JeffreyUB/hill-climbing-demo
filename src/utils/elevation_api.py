import requests
import numpy as np

# url = "https://api.open-elevation.com/api/v1/lookup"

# response = requests.post(url, json={"locations": coords})
# response.raise_for_status()
# data = response.json()

def get_elevation(coords, url="https://api.open-elevation.com/api/v1/lookup"):
# {
#    "results":
#    [
#       {
#          "longitude":10.0,
#          "elevation":515,
#          "latitude":10.0
#       },
#       {
#          "longitude":20.0,
#          "elevation":545,
#          "latitude":20.0
#       },
#       {
#          "latitude":41.161758,
#          "elevation":117,
#          "longitude":-8.583933
#       }
#    ]
# }
    response = requests.post(url, json={"locations": coords})
    response.raise_for_status()
    data = response.json()
    return data

def build_coords(lat=41.161758, lon=-73.923, n_points=20, span=0.02):
    "Returns lat and longtitude and builds coordinates for get elevation request."
    lats = np.linspace(lat - span, lat + span, n_points)
    lons = np.linspace(lon - span, lon + span, n_points)
    coords = [{"latitude": lat, "longitude": lon} for lat in lats for lon in lons]
    return coords

def parse_elevation_response(data):
    # "input looks like # {
#    "results":
#    [
#       {
#          "longitude":10.0,
#          "elevation":515,
#          "latitude":10.0
#       },
#       {
#          "longitude":20.0,
#          "elevation":545,
#          "latitude":20.0
#       },
#       {
#          "latitude":41.161758,
#          "elevation":117,
#          "longitude":-8.583933
#       }
#    ]
# }"
    results = []
    # results_dic = defaultdict(list)
    for response in data["results"]:
        longitude = response.get("longitude")
        elevation = response.get("elevation")
        latitude = response.get("latitude")
        results.append((elevation, longitude, latitude))
        
    return results

def sort_elevation_response(data):
    # "input looks like # {
#    "results":
#    [
#       {
#          "longitude":10.0,
#          "elevation":515,
#          "latitude":10.0
#       },
#       {
#          "longitude":20.0,
#          "elevation":545,
#          "latitude":20.0
#       },
#       {
#          "latitude":41.161758,
#          "elevation":117,
#          "longitude":-8.583933
#       }
#    ]
# }"
    sorted_data = sorted(data)
    return sorted_data
