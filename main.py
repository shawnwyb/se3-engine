import numpy as np

from se3 import SE3
from visualizer import animate_frames


def make_frame_sequence():
    """Move B in A and C in B, then express every frame in A."""
    frame_a = SE3(np.eye(3), np.zeros(3))
    rotation_ab = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    rotation_bc = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])

    sequence = []
    for step in range(120):
        phase = 2 * np.pi * step / 120
        transform_ab = SE3(rotation_ab, [2 + 0.8 * np.sin(phase), 1, 0])
        transform_bc = SE3(rotation_bc, [1, 2 + 0.7 * np.cos(phase), 3])
        sequence.append(
            {
                "A": frame_a,
                "B": transform_ab,
                "C": transform_ab.compose(transform_bc),
            }
        )
    return sequence


if __name__ == "__main__":
    animate_frames(make_frame_sequence())
