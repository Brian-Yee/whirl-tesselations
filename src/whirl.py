#!/usr/bin/env python
"""
Code for generating whirl plots.
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg

plt.rcParams["figure.figsize"] = (40, 40)


def whirl_plot(polygons, iterations, step=1e-1, **kwargs):
    """
    Create a modified whirl plot for an arbitrary polygon.

    Traditionally whirl plots are limited to n-gons, to plot for an arbtirary polygon we
    express the construction of the whirl as subsequent connections between points while
    solving the mice-problem.

    Arguments:
        polygons: np.array
            A polygon of points stored as
                ((x_1, y_1), (x_2, y_2), ..., (x_n, y_n))
            and verticaly stacked.
        iterations: int
            Number of iterations from starting state of mice problem
        step: float
            Velocity of mice.
        kwargs: dict(str, object)
            Keyword arguments for matplotlib.
    """
    for polygon in polygons:
        for _ in range(iterations):
            # pylint: disable=invalid-name
            xy = np.vstack([polygon, polygon[0]])
            plt.plot(*np.hsplit(xy, 2), **kwargs)

            diff = polygon - np.roll(polygon, 1, axis=0)
            norm_velocity = diff / np.linalg.norm(diff, axis=1, keepdims=True)

            polygon -= step * norm_velocity

    plt.gca().set_aspect("equal")
    plt.gca().axis("off")

    canvas = FigureCanvasAgg(plt.gcf())
    canvas.draw()

    stream, (width, height) = canvas.print_to_buffer()
    img = np.fromstring(stream, np.uint8).reshape((height, width, 4))

    plt.imsave("images/whirl-15.png", _trim_border(img))


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
