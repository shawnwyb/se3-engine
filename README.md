# SE(3) Engine

A coordinate frame is an origin and three perpendicular unit directions. The same physical point can have different coordinates in different frames, so converting between them requires knowing their relative rotation and translation.

These rigid transformations form SE(3), the special Euclidean group in three dimensions. They preserve distances and handedness, with no stretching or mirror flips. This project represents them as 4x4 homogeneous matrices and uses them to convert points, compose and invert transforms, and visualize moving frames.

Tests check point conversion, composition, inversion, and rotation validity. An animation shows a chain of moving frames.

<img width="520" alt="readme-demo" src="https://github.com/user-attachments/assets/147e755f-d0e9-40c7-a530-9926364a75b4" />

## Setup

```bash
# Create and activate a virtual environment (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Run the moving-frame visualizer
python main.py

# Run the SE(3) checks
python -m unittest -v
```

To leave the virtual environment:

```bash
deactivate
```

The visualizer draws frames A, B, and C in A's coordinates. B turns and moves
relative to A, C moves relative to B, and `compose()` places C in A. Red,
green, and blue arrows show each frame's x, y, and z axes. B starts at the
orientation from the hand calculation and completes one turn.
