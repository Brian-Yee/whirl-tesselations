#!/usr/bin/env python
# pylint: disable=invalid-name
"""
Functions dedicated to constructing pentagonal tiling tiles.
"""
import numpy as np

H = np.sqrt(3)
TRANS_15 = np.array([[9 * H + 12, 3], [H + 1, H + 3]])


def tile_15():
    """
    Construct the 12-part supercell of the type-15 pentagonal tiling.

    Returns:
        np.array
            Type-15 pentagonal tiling supercell.
    """
    x_m = np.array([0, 1, 2, 2, 2, 3, 3, 3, 5, 5, 2, 3])
    x_b = np.array([0, 0, 0, 1, 2, 2, 4, 6, 6, 6, 3, 5])
    y_m = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1])
    y_b = np.array([0, 1, 0, 0, 0, 1, 1, 1, 3, 1, 0, 1])

    X_1 = np.dstack([x_m * H + x_b, y_m * H + y_b]).squeeze()
    X_3 = X_1 - TRANS_15[1]

    X_2 = -X_1 + TRANS_15[0] + np.array([H, 1])
    X_4 = X_2 - TRANS_15[1]

    return np.vstack([half_cell_15(X_1, X_3), half_cell_15(X_4, X_2)])


def half_cell_15(x, y):
    """
    Construct half of the type-15 pentagonal tiling supercell.

    Arguments:
        x: np.array
           Pre-calculated constants for cell constrcution.
        y: np.array
           Pre-calculated constants for cell constrcution.

    Returns:
        np.array
            Half of the type-15 pentagonal tiling supercell.
    """
    return np.array(
        [
            [x[0], x[1], y[3], y[2], y[1]],
            [x[1], x[2], y[5], y[4], y[3]],
            [x[2], x[3], x[10], y[6], y[5]],
            [x[4], x[5], x[7], x[11], x[10]],
            [x[10], x[11], y[8], y[7], y[6]],
            [x[7], x[8], x[9], y[8], x[11]],
        ]
    )
