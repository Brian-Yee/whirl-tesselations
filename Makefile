.PHONY: help
help:
	@echo "help       Display this message."
	@echo "tile-15    Create a pentagonal-15 tiling of plane."
	@echo "tile-14    Create a pentagonal-14 tiling of plane."

.PHONY: pentagon-15
pentagon-15:
	python main.py 3 9 pentagon-15 images/whirl-15.png 40 0.1

.PHONY: pentagon-14
pentagon-14:
	python main.py 8 8 pentagon-14 images/whirl-14.png 60 0.04

.PHONY: square
square:
	python main.py 5 3 square images/square.png 200 0.005

.PHONY: hexagon
hexagon:
	time python main.py 5 5 hexagon images/hexagon.png 80 0.02

.PHONY: triangle
triangle:
	time python main.py 6 6 triangle images/triangle.png 50 0.03
