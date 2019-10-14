"""
A code port of the 15th pentagonal tiling

http://jsfiddle.net/jolumij/1qh7zav9/
"""
# /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import itertools

from matplotlib.collections import PolyCollection

H = np.sqrt(3)
TRANS = np.array([[9 * H + 12, 3], [H + 1, H + 3]])


def construct_unit_cell():
    x_m = np.array([0, 1, 2, 2, 2, 3, 3, 3, 5, 5, 2, 3])
    x_b = np.array([0, 0, 0, 1, 2, 2, 4, 6, 6, 6, 3, 5])
    y_m = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, -1])
    y_b = np.array([0, 1, 0, 0, 0, 1, 1, 1, 3, 1, 0, 1])

    X_1 = np.dstack([x_m * H + x_b, y_m * H + y_b]).squeeze()
    X_3 = X_1 - TRANS[1]

    X_2 = -X_1 + TRANS[0] + np.array([H, 1])
    X_4 = X_2 - TRANS[1]

    return np.vstack([half_cell(X_1, X_3), half_cell(X_4, X_2)])


def half_cell(x, y):
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


def render(polygons):
    _, ax = plt.subplots()
    poly_collection = PolyCollection(polygons, color="white", edgecolor="black")

    ax.add_collection(poly_collection)
    ax.autoscale_view()
    ax.set_aspect("equal")

    plt.show()


def main():
    unit_cell = construct_unit_cell()
    translations = [np.dot(x, TRANS) for x in itertools.product(range(2), range(6))]

    tiling = np.array([trans + unit_cell for trans in translations])
    polygons = tiling.reshape(-1, 5, 2)

    render(polygons)


if __name__ == "__main__":
    main()
