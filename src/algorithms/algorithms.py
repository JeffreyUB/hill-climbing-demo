import random


def simple_hill_climb(sorted_elevation_data, response_grid):
    path = []
    climbing = True
    start = sorted_elevation_data[0]
    index = response_grid.index(start)
    path.append((index, response_grid[index][0], f"Starting at coordinates {response_grid[index]}"))
    steps = 0
    while climbing:
        n_points = int(len(response_grid) ** 0.5)
        up, down, left, right = index - n_points, index + n_points, index - 1, index + 1
        best_neighbor = None
        best_elev = response_grid[index][0]
        for neighbor in [up, down, left, right]:
            if 0 <= neighbor < len(response_grid):
                if response_grid[neighbor][0] > best_elev:
                    best_neighbor = neighbor
                    best_elev = response_grid[neighbor][0]
        if best_neighbor == None:
            break
        steps += 1
        index = best_neighbor
        path.append((index, best_elev, f"Moved to neighbor at coordinates {response_grid[index]}"))

    return steps, best_elev, response_grid[index], path

def stochastic_hill_climb(sorted_elevation_data, response_grid):
    path = []
    climbing = True
    start = sorted_elevation_data[0]
    index = response_grid.index(start)
    path.append((index, response_grid[index][0], f"Starting at coordinates {response_grid[index]}"))
    steps = 0
    while climbing:
        n_points = int(len(response_grid) ** 0.5)
        up, down, left, right = index - n_points, index + n_points, index - 1, index + 1
        uphills = []
        best_elev = response_grid[index][0]
        for neighbor in [up, down, left, right]:
            if 0 <= neighbor < len(response_grid):
                if response_grid[neighbor][0] > best_elev:
                    uphills.append(neighbor)
                    # best_elev = response_grid[neighbor][0]
        if not uphills:
            break
        path.append(f"Potential Uphill candidates {uphills}")
        chosen_uphill = random.choice(uphills)
        steps += 1
        index = chosen_uphill
        path.append((index, best_elev, f"Moved to randomly chosen uphill neighbor at coordinates {response_grid[index]}"))

    return steps, response_grid[index][0], response_grid[index], path


def random_restart_hill_climb(response_grid, restarts=5):
    steps = 0
    highest_elevation = float("-inf")
    path = []
    best_index = 0
    iteration = 1
    while restarts > 0:
        climbing = True
        index = random.randint(0, len(response_grid) - 1)
        path.append((index, response_grid[index][0], f"Starting at randomly chosen coordinates {response_grid[index]}"))
        best_elev = response_grid[index][0]
        while climbing:
            n_points = int(len(response_grid) ** 0.5)
            up, down, left, right = index - n_points, index + n_points, index - 1, index + 1
            best_neighbor = None
            best_elev = response_grid[index][0]
            for neighbor in [up, down, left, right]:
                if 0 <= neighbor < len(response_grid):
                    if response_grid[neighbor][0] > best_elev:
                        best_neighbor = neighbor
                        best_elev = response_grid[neighbor][0]
            if best_neighbor == None:
                break
            steps += 1
            index = best_neighbor
            path.append((index, best_elev, f"Moved to best uphill neighbor at coordinates {response_grid[index]}"))
        if best_elev > highest_elevation:
            highest_elevation = best_elev
            best_index = index
            iteration = (5 - restarts + 1)
            
        restarts -= 1
        path.append((index, best_elev, f"Unable to move from {response_grid[index]} at elevation {best_elev}. Restarting. {restarts} restarts left"))

    path.append((index, best_elev, f"Highest elevation was reached at elevation {highest_elevation} at {response_grid[best_index]} during attempt {iteration}."))
    return steps, highest_elevation, response_grid[index], path




