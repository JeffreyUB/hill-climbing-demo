import numpy as np
from mountain import generate_mountain
from random_restart import random_restart_global, hill_climb_single
from stochastic import stochastic_hill_climb, smooth_path
from export_2d import export_2d_animation

Z = generate_mountain(size=600) # Generate DEM
center = (Z.shape[0] // 2, Z.shape[1] // 2) # calculate center

# A) SIMPLE HILL CLIMB
simple_path_raw = hill_climb_single(Z, center)
simple_path = smooth_path(simple_path_raw, n_points=300) # Smooth for 10-second animation (300 frames)
export_2d_animation(Z, simple_path, output="simple_climb.mp4", fps=30)

# B) STOCHASTIC HILL CLIMB
stoch_raw = stochastic_hill_climb( # 1st set of parameters
    Z,
    center,
    max_steps=600,      # short or long explorations
    downhill_prob=0.2,  # higher = more downhill/random moves allowed
    patience=50         # how many non-improving moves allowed
)
stoch_1_path = smooth_path(stoch_raw, n_points=300)
export_2d_animation(Z, stoch_1_path, output="stoch_climb_1.mp4", fps=30)

stoch_raw = stochastic_hill_climb( # 2nd set of parameters
    Z,
    center,
    max_steps=800,
    downhill_prob=0.5,
    patience=100
)
stoch_2_path = smooth_path(stoch_raw, n_points=300)
export_2d_animation(Z, stoch_2_path, output="stoch_climb_2.mp4", fps=30)

# C) RANDOM RESTART HILL CLIMB
rand_res_path = random_restart_global(Z, n_restarts=300)
merged_raw = np.vstack([simple_path_raw, rand_res_path]) # Merge center start + global route
global_path = smooth_path(merged_raw, n_points=300)
export_2d_animation(Z, global_path, output="rr_climb.mp4", fps=30)

print("All animations created.")