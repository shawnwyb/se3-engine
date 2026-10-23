import numpy as np
from se3 import SE3

if __name__ == "__main__":
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
    print(se3.compose(se3.inverse()).T)


