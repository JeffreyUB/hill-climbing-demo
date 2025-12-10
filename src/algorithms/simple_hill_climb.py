from src.utils.elevation_api import (
    get_elevation,
    build_coords,
    parse_elevation_response,
    sort_elevation_response,
)
from src.algorithms.algorithms import simple_hill_climb


def run_simple(lat, lon):
    coords = build_coords(lat, lon)

    response = get_elevation(coords)

    elevation_data_response_grid = parse_elevation_response(response)

    elevation_data_sorted = sort_elevation_response(elevation_data_response_grid)

    result = simple_hill_climb(elevation_data_sorted, elevation_data_response_grid)

    return result
