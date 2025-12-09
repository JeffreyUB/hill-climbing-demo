import numpy as np
from scipy.ndimage import gaussian_filter

# for heatmap (layered noise) returns Z (2D numpy array of elevation)
def generate_mountain(size=600, octaves=4, seed=42):

    np.random.seed(seed)

    Z = np.zeros((size, size))
    freq = 1.0
    amp = 1.0

    for _ in range(octaves):
        noise = np.random.randn(size, size)
        noise = gaussian_filter(noise, sigma=size/(freq*3))
        Z += noise * amp
        freq *= 2
        amp /= 2

    # Make values positive + nice contrast
    Z -= Z.min()
    Z /= Z.max()
    Z *= 2000  # vertical exaggeration for visuals

    # Final smooth pass
    Z = gaussian_filter(Z, sigma=2)

    return Z
