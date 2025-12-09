import random
def simple_hill_climb(sorted_elevation_data, response_grid):
    climbing = True
    start = sorted_elevation_data[0]
    index = response_grid.index(start)
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

    return steps

def stochastic_hill_climb(sorted_elevation_data, response_grid):
    climbing = True
    start = sorted_elevation_data[0]
    index = response_grid.index(start)
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
        chosen_uphill = random.choice(uphills)
        steps += 1
        index = chosen_uphill

    return steps


def random_restart_hill_climb(response_grid, restarts=5):
    steps = 0
    highest_elevation = float("-inf")
    while restarts > 0:
        climbing = True
        index = random.randint(0, len(response_grid) - 1)
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
        highest_elevation = max(highest_elevation, best_elev)
        restarts -= 1

    return steps, highest_elevation




