import numpy as np

class SE3:
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

R = np.array(
    [[0, -1, 0],
     [1, 0, 0],
     [0, 0, 1]])
t = np.array([4, 1, 2])

se3 = SE3(R, t)

point = np.array([2, 3, 5])
transformed_point = se3.transform_point(point)
print(transformed_point)
print(se3.inverse().transform_point(transformed_point))


