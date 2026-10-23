import numpy as np

class SE3:
    def __init__(self, R, t):
        self.T = np.eye(4)
        self.T[:3, :3] = R
        self.T[:3, 3] = t
    
    def convertbtoa(self, b):
        b_homogeneous = np.append(b, 1)
        return (self.T @ b_homogeneous)[:-1]

    def convertatob(self, a):
        a_homogeneous = np.append(a, 1)
        R_transposed = self.T[:3, :3].T
        a_origin = -R_transposed @ self.T[:3, 3]

        T_inverse = np.eye(4)
        T_inverse[:3, :3] = R_transposed
        T_inverse[:3, 3] = a_origin

        return (T_inverse @ a_homogeneous)[:-1]
    
    def inverse(self):
        R_transposed = self.T[:3, :3].T
        a_origin = -R_transposed @ self.T[:3, 3]

        T_inverse = np.eye(4)
        T_inverse[:3, :3] = R_transposed
        T_inverse[:3, 3] = a_origin

        return T_inverse


R = np.array(
    [[0, -1, 0],
     [1, 0, 0],
     [0, 0, 1]])
t = np.array([4, 1, 2])

se3 = SE3(R, t)

b = np.array([2, 3, 5])
a = se3.convertbtoa(b)
print(a)
back = se3.convertatob(a)
print(back)


