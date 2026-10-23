import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def draw_frame(ax, transform, name, length=0.8):
    """Draw a frame's origin and three axes in A coordinates."""
    origin = transform.transform_point([0, 0, 0])
    for axis_name, direction, color in (
        ("x", [1, 0, 0], "red"),
        ("y", [0, 1, 0], "green"),
        ("z", [0, 0, 1], "blue"),
    ):
        tip = transform.transform_point(np.array(direction) * length)
        arrow = tip - origin
        ax.quiver(*origin, *arrow, color=color, arrow_length_ratio=0.18)
        ax.text(*tip, f"{name} {axis_name}", color=color)
    ax.scatter(*origin, color="black", s=18)
    ax.text(*origin, name, color="black")


def draw_scene(ax, frames):
    """Draw one moment of the A -> B -> C frame chain."""
    ax.clear()
    for name, transform in frames.items():
        draw_frame(ax, transform, name)

    origins = [transform.transform_point([0, 0, 0]) for transform in frames.values()]
    ax.plot(*np.array(origins).T, color="gray", linestyle="--", alpha=0.6)
    ax.set(
        xlim=(-1, 7), ylim=(-3, 3), zlim=(-1, 5),
        xlabel="A x", ylabel="A y", zlabel="A z",
    )
    ax.set_box_aspect((8, 6, 6))
    ax.set_title("Moving coordinate frames (red x, green y, blue z)")


def animate_frames(frame_sequence):
    """Show a sequence of A-coordinate frame poses."""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection="3d")
    animation = FuncAnimation(
        fig,
        lambda index: draw_scene(ax, frame_sequence[index]),
        frames=len(frame_sequence),
        interval=60,
    )
    plt.show()
    return animation
