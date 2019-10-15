# /usr/bin/env python
"""
A code port of the 15th pentagonal tiling

http://jsfiddle.net/jolumij/1qh7zav9/
"""
import itertools
import numpy as np

import src.whirl
import src.tiles


def main():
    """
    Main function to interface with CLI.
    """
    mesh = list(itertools.product(range(2), range(6)))
    translations = np.dot(mesh, src.tiles.TRANS_15)

    supercell = src.tiles.tile_15()

    polygons = np.vstack([trans + supercell for trans in translations])

    src.whirl.whirl_plot(polygons, 40, c="black", linewidth=0.1)


if __name__ == "__main__":
    main()
