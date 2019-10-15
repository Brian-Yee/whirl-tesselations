# /usr/bin/env python
# pylint: disable=invalid-name
"""
A code port of the 15th pentagonal tiling

http://jsfiddle.net/jolumij/1qh7zav9/
"""
import itertools
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np

import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg
plt.rcParams["figure.figsize"] = (40,40)

H = np.sqrt(3)
TRANS = np.array([[9 * H + 12, 3], [H + 1, H + 3]])

def construct_supercell():
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
    X_3 = X_1 - TRANS[1]

    X_2 = -X_1 + TRANS[0] + np.array([H, 1])
    X_4 = X_2 - TRANS[1]

    return np.vstack([half_cell(X_1, X_3), half_cell(X_4, X_2)])


def half_cell(x, y):
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


def render(polygons):
    """
    Draw a collection of polygons.

    Arguments:
        polygons: np.array
            A list of polygons with vertices arranged clockwise.
    """
    _, ax = plt.subplots()

    poly_collection = matplotlib.collections.PolyCollection(
        polygons, color="white", edgecolor="black"
    )

    ax.add_collection(poly_collection)
    ax.autoscale_view()
    ax.set_aspect("equal")

    plt.show()

def whirl_plot(polygon, step=1e-1):
    for i in range(40):
        to_plot = np.vstack([polygon, polygon[0]])
        plt.plot(to_plot[:, 0], to_plot[:, 1], c='black', linewidth=0.1)

        diff = polygon - np.roll(polygon, 1, axis=0)
        norm_velocity = diff/np.linalg.norm(diff, axis=1, keepdims=True)

        polygon -= step * norm_velocity

def main():
    """
    Main function to interface with CLI.
    """
    mesh = list(itertools.product(range(2), range(6)))
    translations = np.dot(mesh, TRANS)


    supercell = construct_supercell()

    polygons = np.vstack([trans + supercell for trans in translations])

    for polygon in polygons:
        whirl_plot(polygon)

    plt.gca().set_aspect("equal")

    plt.gca().axis("off")

    canvas = FigureCanvasAgg(plt.gcf())
    canvas.draw()

    stream, (width, height) = canvas.print_to_buffer()
    img = np.fromstring(stream, np.uint8).reshape((height, width, 4))

    plt.imsave("images/whirl-15.png", _trim_border(img))

    # plt.savefig('whirl', bbox_inches='tight', pad=0)
    raise SystemExit

    render(polygons)

def _trim_border(img):
    """
    Trims white space border of a numpy image.
    Arguments:
        img: np.array
            Numpy image.
    Returns:
        img: np.array
            Numpy image with no white border space.
    """
    for i in range(img.shape[0]):
        if np.any(img[i, :, :] != 255):
            img = img[i:, :, :]
            break

    for i in range(img.shape[0] - 1, 0, -1):
        if np.any(img[i, :, :] != 255):
            img = img[: i + 1, :, :]
            break

    for i in range(img.shape[1]):
        if np.any(img[:, i, :] != 255):
            img = img[:, i:, :]
            break

    for i in range(img.shape[1] - 1, 0, -1):
        if np.any(img[:, i, :] != 255):
            img = img[:, : i + 1, :]
            break

    return img

if __name__ == "__main__":
    main()
