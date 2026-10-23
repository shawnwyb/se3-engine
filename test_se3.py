import unittest

import numpy as np

from se3 import SE3


class TestSE3(unittest.TestCase):
    def test_transform_point_and_inverse(self):
        transform = SE3(
            np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
            np.array([4, 1, 2]),
        )
        point = np.array([2, 3, 5])

        np.testing.assert_array_equal(transform.transform_point(point), [1, 3, 7])
        np.testing.assert_array_equal(
            transform.inverse().transform_point([1, 3, 7]), point
        )
        np.testing.assert_array_equal(transform.compose(transform.inverse()).T, np.eye(4))

    def test_compose_two_transforms(self):
        transform_ab = SE3(
            np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),
            np.array([2, 1, 0]),
        )
        transform_bc = SE3(
            np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
            np.array([1, 2, 3]),
        )
        expected_ac = np.array(
            [[0, -1, 0, 4], [-1, 0, 0, 0], [0, 0, -1, 3], [0, 0, 0, 1]]
        )
        point_c = np.array([2, 1, 1])

        composed = transform_ab.compose(transform_bc)
        np.testing.assert_array_equal(composed.T, expected_ac)
        np.testing.assert_array_equal(composed.transform_point(point_c), [3, -2, 2])
        np.testing.assert_array_equal(
            transform_ab.transform_point(transform_bc.transform_point(point_c)),
            [3, -2, 2],
        )


if __name__ == "__main__":
    unittest.main()
