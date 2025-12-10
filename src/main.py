from src.algorithms.simple_hill_climb import run_simple
from src.algorithms.stochastic_hill_climb import run_stochastic
from src.algorithms.random_restart_hill_climb import run_random_restart
from src.utils.data import MOUNTAINS
from src.utils.metrics import format_response, write_output


def main():
    print("Choose a location to run a hill climbing algorithm on:\n")
    print(
        "Options:\n Mt Everest: 1\n Mount Marcy: 2\n Hunter Mountain: 3\n Camel's Hump: 4\n"
    )
    while True:
        location_choice = input("Enter choice (1-4): ")
        if location_choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Enter a valid choice\n")

    lat, lon = MOUNTAINS[location_choice]

    print(
        "\nChoose which Hill climbing Algorithm to run on the terrain:\n\nSimple Hill Climbing: 1\nStochastic Hill Climbing: 2\nRandom Restart Hill Climbing: 3\n"
    )
    while True:
        algo_choice = input("Enter choice (1-3): ")
        if algo_choice in ["1", "2", "3"]:
            break
        else:
            print("Enter a valid choice\n")

    if algo_choice == "1":
        steps, elevation, coords, path = run_simple(lat, lon)
        format_response(steps, elevation, coords)
        write_output(path, algorithm="Simple Hill Climb")

    if algo_choice == "2":
        steps, elevation, coords, path = run_stochastic(lat, lon)
        format_response(steps, elevation, coords)
        write_output(path, algorithm="Stochastic Hill Climbing")

    if algo_choice == "3":
        steps, elevation, coords, path = run_random_restart(lat, lon)
        format_response(steps, elevation, coords)
        write_output(path, algorithm="Random Restart Hill Climbing")


if __name__ == "__main__":
    main()
