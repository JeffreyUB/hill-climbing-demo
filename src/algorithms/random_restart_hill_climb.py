from src.utils.elevation_api import get_elevation, build_coords, parse_elevation_response, sort_elevation_response
from src.algorithms.algorithms import random_restart_hill_climb
def run_random_restart():
    coords = build_coords()
    response = get_elevation(coords)

    elevation_data_response_grid = parse_elevation_response(response)

    # elevation_data_sorted = sort_elevation_response(elevation_data_response_grid)

    result = random_restart_hill_climb(elevation_data_response_grid)
    return result

ans, highest_elevation = run_random_restart()
print(f"ans is {ans} and highest elevation is {highest_elevation}")