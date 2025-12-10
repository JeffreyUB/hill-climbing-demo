from src.utils.elevation_api import (
    get_elevation,
    build_coords,
    parse_elevation_response,
)
from src.algorithms.algorithms import random_restart_hill_climb


def run_random_restart(lat, lon):
    coords = build_coords(lat, lon)
    response = get_elevation(coords)

    elevation_data_response_grid = parse_elevation_response(response)

    result = random_restart_hill_climb(elevation_data_response_grid)

    return result
