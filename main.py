import numpy as np

class SE3:
    def __init__(self, R, t):
        self.matrix = np.eye(4)
        self.matrix[:3, :3] = R
        self.matrix[:3, 3] = t
    
    def convertbtoa(self, b):
        a = np.dot(self.matrix, b)
        return a

R = np.array(
    [[0, -1, 0],
     [1, 0, 0],
     [0, 0, 1]])

t = np.array([4, 1, 2])

se3 = SE3(R, t)

b = np.array([2, 3, 5, 1])

print(se3.convertbtoa(b))


