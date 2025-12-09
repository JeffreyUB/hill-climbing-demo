from src.utils.elevation_api import get_elevation, build_coords, parse_elevation_response, sort_elevation_response
from src.algorithms.algorithms import simple_hill_climb
def run_simple():
    coords = build_coords()
    # print(coords)
    response = get_elevation(coords)
    # print(elevation_data)

    elevation_data_response_grid = parse_elevation_response(response)

    # response = sort_elevation_response(parsed)
    # print(response)
    elevation_data_sorted = sort_elevation_response(elevation_data_response_grid)

    # for i in range(10):
    #     print(elevation_data[i])
    print(elevation_data_response_grid)
    result = simple_hill_climb(elevation_data_sorted, elevation_data_response_grid)
    return result

ans = run_simple()
print(f"ans is {ans}")