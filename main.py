# /usr/bin/env python
# pylint: disable=too-many-arguments
"""
Pentagonal whirl tiling generator.
"""
import argparse
import itertools
import numpy as np

import src.whirl
import src.tiles


def main(width, height, tile_type, fpath, iterations, step):
    """
    Main function to interface with CLI.
    """
    if tile_type == "pentagon-15":
        basis, supercell = src.tiles.tile_15()
    elif tile_type == "pentagon-14":
        basis, supercell = src.tiles.tile_14()
    elif tile_type == "square":
        basis, supercell = src.tiles.square()
    elif tile_type == "hexagon":
        basis, supercell = src.tiles.hexagon()
    elif tile_type == "triangle":
        basis, supercell = src.tiles.triangle()
    else:
        raise ValueError("Unknown pentagonal tiling.")

    mesh = list(itertools.product(range(width), range(height)))
    translations = np.dot(mesh, basis)

    polygons = np.vstack([trans + supercell for trans in translations])

    src.whirl.whirl_plot(polygons, iterations, step, fpath, c="black", linewidth=0.1)


if __name__ == "__main__":
    # fmt: off
    PARSER = argparse.ArgumentParser(
        description='Create tesslations of pentagonal whirls.'
    )

    PARSER.add_argument(
        'W',
        type=int,
        help='Width of tesselations in tiles.'
    )

    PARSER.add_argument(
        'H',
        type=int,
        help='Height of tesselations in tiles.'
    )

    PARSER.add_argument(
        'polygon',
        type=str,
        help='Type of pentagon'
    )

    PARSER.add_argument(
        'fpath',
        type=str,
        help='Type of pentagon'
    )

    PARSER.add_argument(
        'whirl_iterations',
        type=int,
        help='Number of iterations to whirl a polygon inwards.'
    )

    PARSER.add_argument(
        'whirl_step',
        type=float,
        help='Step size for each whirl.'
    )
    # fmt:on

    ARGS = PARSER.parse_args()

    main(
        ARGS.W, ARGS.H, ARGS.polygon, ARGS.fpath, ARGS.whirl_iterations, ARGS.whirl_step
    )
