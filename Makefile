.PHONY: help
help:
	@echo "help       Display this message."
	@echo "tile-15    Create a pentagonal-15 tiling of plane."
	@echo "tile-14    Create a pentagonal-14 tiling of plane."

.PHONY: tile-15
tile-15:
	python main.py 3 9 15 images/whirl-15.png 40 0.1

.PHONY: tile-14
tile-14:
	python main.py 8 8 14 images/whirl-14.png 60 0.04
