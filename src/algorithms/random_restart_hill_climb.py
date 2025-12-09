from src.utils.elevation_api import get_elevation, build_coords, parse_elevation_response
from src.utils.metrics import format_response, write_output
from src.algorithms.algorithms import random_restart_hill_climb
def run_random_restart():
    coords = build_coords()
    response = get_elevation(coords)

    elevation_data_response_grid = parse_elevation_response(response)

    # elevation_data_sorted = sort_elevation_response(elevation_data_response_grid)

    result = random_restart_hill_climb(elevation_data_response_grid)
    return result

steps, elevation, coords, path = run_random_restart()
format_response(steps, elevation, coords)
write_output(path)