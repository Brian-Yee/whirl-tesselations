#!/usr/bin/env python
# pylint: disable=invalid-name, bad-whitespace
"""
Functions dedicated to constructing pentagonal tiling tiles.
"""
import numpy as np


def tile_15():
    """
    Construct the 12-part supercell of the type-15 pentagonal tiling.

    Returns:
        np.array
            Type-15 pentagonal tiling supercell.
    """
    H = np.sqrt(3)
    basis = np.array([[9 * H + 12, 3], [H + 1, H + 3]])

    # fmt: off
    x_m = np.array([0, 1, 2, 2, 2, 3, 3, 3, 5, 5,  2,  3])
    x_b = np.array([0, 0, 0, 1, 2, 2, 4, 6, 6, 6,  3,  5])
    y_m = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1])
    y_b = np.array([0, 1, 0, 0, 0, 1, 1, 1, 3, 1,  0,  1])

    X_1 = np.stack([x_m * H + x_b, y_m * H + y_b], axis=-1)
    X_3 = X_1 - basis[1]

    X_2 = -X_1 + basis[0] + np.array([H, 1])
    X_4 = X_2 - basis[1]
    # fmt: on

    return basis, np.vstack([half_cell_15(X_1, X_3), half_cell_15(X_4, X_2)])


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
    # fmt: off
    half_cell = np.array(
        [
            [ x[0],  x[1],  y[3],  y[2],  y[1]],
            [ x[1],  x[2],  y[5],  y[4],  y[3]],
            [ x[2],  x[3], x[10],  y[6],  y[5]],
            [ x[4],  x[5],  x[7], x[11], x[10]],
            [x[10], x[11],  y[8],  y[7],  y[6]],
            [ x[7],  x[8],  x[9],  y[8],  x[11]],
        ]
    )
    # fmt: on
    return half_cell


def tile_14():
    """
    Construct the supercell of the type-14 pentagonal tiling.

    Returns:
        np.array
            Type-15 pentagonal tiling supercell.
    """
    s = np.sqrt(57)

    y1 = (s - 3) / 8  # sin (C/2)
    y2 = (3 * s - 17) / 16  # cos C
    x1 = np.sqrt(6 * s - 2) / 8  # cos (C/2)
    x2 = np.sqrt(102 * s - 546) / 16  # sin(C)
    basis = np.array([[3 * x1 + 3 * x2, -y1 + 2 + y2], [x2, 2 + 6 * y1 - y2]])

    # fmt: off
    A = np.array(
        [
            [0, 0],
            [2 * x2 + x1, 0],
            [2 * x2 + 2 * x1, -y1],
            [2 * x2, -3 * y1],
            [0, -1]
        ]
    )
    # fmt: on

    B = A * [1, -1]
    C = np.stack([-A[:, 0] + 4 * x2 + 3 * x1, A[:, 1] - y1], axis=-1)
    D = np.stack([C[:, 0], -y1 + B[:, 1]], axis=-1)

    offsets = np.array([[0, 2], [x2, -y2], [-2 * x1, 2 * y1]])

    E = np.vstack(
        [D[3, :], B[[2, 3], :], B[3, :] + offsets[0], B[3, :] + offsets[:2].sum(axis=0)]
    )
    F = np.vstack(
        [
            B[3, :] + offsets[:2].sum(axis=0),
            D[3, :],
            D[3, :] + offsets[1],
            D[3, :] + offsets[:2].sum(axis=0),
            D[3, :] + offsets.sum(axis=0),
        ]
    )

    return basis, np.array([A, B, C, D, E, F])
