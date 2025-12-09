import numpy as np

# path finding for random restart
def hill_climb_single(Z, start):

    path = [start]
    x, y = start

    while True:
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

        current_height = Z[x, y]
        heights = [Z[i, j] for (i, j) in neighbors]

        best_idx = np.argmax(heights)
        best_neighbor = neighbors[best_idx]

        if Z[best_neighbor] <= current_height:
            break

        x, y = best_neighbor
        path.append((x, y))

    return np.array(path)

# implementing many generations starting at various points
def random_restart_global(Z, n_restarts=100, must_start=None):
    best_path = None
    best_height = -np.inf

    # evaluating starting point
    if must_start is not None:
        path = hill_climb_single(Z, must_start)
        peak = path[-1]
        peak_height = Z[peak[0], peak[1]]
        best_path = path
        best_height = peak_height

    # test other random restarts
    for _ in range(n_restarts):
        start = (
            np.random.randint(0, Z.shape[0]),
            np.random.randint(0, Z.shape[1])
        )

        path = hill_climb_single(Z, start)
        peak = path[-1]
        peak_height = Z[peak[0], peak[1]]

        if peak_height > best_height:
            best_height = peak_height
            best_path = path

    return best_path
