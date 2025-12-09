def simple_hill_climb(sorted_elevation_data, response_grid):
    climbing = True
    print(response_grid)
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

# def simple_hill_climb(elevation_data):
#     climbing = True
#     index = 0
#     steps = 0
#     n_points = int(len(elevation_data) ** 0.5)

#     while climbing:
#         up, down, left, right = index - n_points, index + n_points, index - 1, index + 1
#         best_neighbor = None
#         best_elev = elevation_data[index][0]
#         for neighbor in [up, down, left, right]:
#             if 0 <= neighbor < len(elevation_data):
#                 neighbor_elev = elevation_data[neighbor][0]
#                 if neighbor_elev > best_elev:
#                     best_neighbor = neighbor
#                     best_elev = neighbor_elev
#         if best_neighbor == None:
#             break
#         steps += 1
#         index = best_neighbor
#         print(f"Step {steps}: index={index}, elevation={elevation_data[index][0]}")

#     return steps

    

# Hill-climbing algorithm
# function HILL-CLIMBING(problem) returns a state
# current ← make-node(problem.initial-state)
# loop do
# neighbor ← a highest-valued successor of current
# if neighbor.value ≤ current.value then
# return current.state
# current ← neighbor
# “Like climbing Everest in thick fog with amnesia”

# soo we got 
    # "input looks like # {
#    "results":
#    [
#       {
#          "longitude":10.0,
#          "elevation":515,
#          "latitude":10.0
#       },
#       {
#          "longitude":20.0,
#          "elevation":545,
#          "latitude":20.0
#       },
#       {
#          "latitude":41.161758,
#          "elevation":117,
#          "longitude":-8.583933
#       }
#    ]
# }"
