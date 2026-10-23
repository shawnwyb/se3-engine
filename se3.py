import numpy as np

class SE3:
    """Represent a rigid transform from a source frame to a target frame.

    R's columns are the source axes expressed in the target frame; t is
    the source origin expressed in the target frame. self.T stores the
    4-by-4 homogeneous transform that combines R and t.

    transform_point() converts a point, inverse() returns the reverse
    transform, and compose(other) applies other first, then this transform.
    """

    def __init__(self, R, t):
        self.T = np.eye(4)
        self.T[:3, :3] = R
        self.T[:3, 3] = t
    
    def transform_point(self, point):
        point_homogeneous = np.append(point, 1)
        return (self.T @ point_homogeneous)[:-1]
    
    def inverse(self):
        R_transposed = self.T[:3, :3].T
        inverse_translation = -R_transposed @ self.T[:3, 3]
        return SE3(R_transposed, inverse_translation)

    def compose(self, other):
        composed_transform = self.T @ other.T
        composed_R = composed_transform[:3, :3]
        point_t = composed_transform[:3, 3]
        return SE3(composed_R, point_t)
