# SE(3) Engine

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
