import plotly.graph_objects as go
import numpy as np

def build_animation_surface(Z, path, cams, out_html="climb.html"):
    x = np.arange(Z.shape[0])
    y = np.arange(Z.shape[1])

    fig = go.Figure()

    # Static terrain surface
    fig.add_trace(go.Surface(
        z=Z,
        x=x,
        y=y,
        colorscale="OrRd",
        showscale=False,
        opacity=1.0
    ))

    # Climber point (animated)
    fig.add_trace(go.Scatter3d(
        x=[path[0, 0]],
        y=[path[0, 1]],
        z=[Z[int(path[0, 0]), int(path[0, 1])]],
        mode="markers",
        marker=dict(size=6, color="cyan")
    ))

    frames = []

    for i in range(len(path)):
        px, py = path[i]
        zi = Z[int(px), int(py)]

        frames.append(go.Frame(
            data=[
                go.Surface(z=Z),  # unchanged
                go.Scatter3d(
                    x=[px],
                    y=[py],
                    z=[zi],
                    mode="markers",
                    marker=dict(size=6, color="cyan")
                )
            ],
            layout=dict(
                scene_camera=dict(
                    eye=cams[i]["eye"],
                    center=cams[i]["center"]
                )
            )
        ))

    fig.frames = frames

    # Animation settings
    fig.update_layout(
        width=900,
        height=700,
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.5)
        ),
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(label="Play",
                         method="animate",
                         args=[None, {"frame": {"duration": 33},  # ~30 fps => 5 sec animation
                                      "fromcurrent": True}])
                ]
            )
        ]
    )

    fig.write_html(out_html)
    return fig
