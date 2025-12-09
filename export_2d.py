import matplotlib
matplotlib.use("Agg")  # off-screen backend
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
import numpy as np

# 2d animation: terrain heatmap, cyan line path of algo, red dot hiker position
# path = 2D numpy array of elevations (tuples of row, col)
def export_2d_animation(Z, path, output="climb_2d.mp4", fps=30):
    # Make sure path is a numpy array
    path = np.array(path)
    rows = path[:, 0]
    cols = path[:, 1]

    fig, ax = plt.subplots(figsize=(6, 6))

    # Show terrain
    im = ax.imshow(
        Z,
        cmap="terrain",
        origin="lower",  # so row 0 is at bottom
        interpolation="bilinear"
    )
    fig.colorbar(im, ax=ax, shrink=0.7, label="Elevation")

    # Plot entire path as a static cyan line
    path_line, = ax.plot(
        cols,
        rows,
        color="cyan",
        linewidth=2,
        alpha=0.7,
        label="Path"
    )

    # Red dot for current climber position
    climber_point, = ax.plot(
        [],
        [],
        "ro",
        markersize=6,
        label="Climber"
    )

    ax.set_xlim(0, Z.shape[1])
    ax.set_ylim(0, Z.shape[0])
    ax.set_xlabel("X (column index)")
    ax.set_ylabel("Y (row index)")
    ax.set_title("Hill-Climb Path (2D View)")
    ax.legend(loc="upper right")

    writer = FFMpegWriter(fps=fps, bitrate=4000)

    print("Rendering 2D animation...")

    with writer.saving(fig, output, dpi=150):
        for r, c in zip(rows, cols):
            climber_point.set_data([c], [r])
            writer.grab_frame()

    plt.close(fig)
    print(f"Done. 2D animation saved as {output}")
