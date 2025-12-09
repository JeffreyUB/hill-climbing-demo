import numpy as np

def camera_follow(path, Z, height=300, back=40):
    cams = []
    for (x, y) in path:
        # Clamp integer indices
        xi, yi = int(x), int(y)
        zi = Z[xi, yi]
        cams.append({
            "eye": {
                "x": x - back,
                "y": y - back,
                "z": zi + height
            },
            "center": {
                "x": x,
                "y": y,
                "z": zi + 10
            }
        })
    return cams
