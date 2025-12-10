import numpy as np
import random
from scipy.interpolate import splprep, splev

# random neighbor selection, w/ certain level of exploration
def stochastic_hill_climb(Z, start, max_steps=500, downhill_prob=0.2, patience=50):
    x, y = start
    path = [(x, y)]
    no_improve = 0

    for _ in range(max_steps):
        neighbors = [
            (x+1, y), (x-1, y),
            (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1),
            (x+1, y-1), (x-1, y+1)
        ]

        # keep in bounds
        neighbors = [
            (i, j) for (i, j) in neighbors
            if 0 <= i < Z.shape[0] and 0 <= j < Z.shape[1]
        ]

        if not neighbors:
            break

        # pick one random neighbor
        nx, ny = random.choice(neighbors)
        current_h = Z[x, y]
        next_h = Z[nx, ny]

        # consider accepting the move
        if next_h > current_h or random.random() < downhill_prob:
            x, y = nx, ny
            path.append((x, y))
            no_improve = 0
        else:
            no_improve += 1

        # too many failed moves = stop
        if no_improve > patience:
            break

    return np.array(path)

def smooth_path(path, n_points=200):
    x, y = path[:, 0], path[:, 1]
    tck, _ = splprep([x, y], s=5)
    u = np.linspace(0, 1, n_points)
    x_new, y_new = splev(u, tck)
    return np.vstack([x_new, y_new]).T
