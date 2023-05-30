from interpreter import draw
from chessPictures import *

base = square.join(square.negative())
negativeBase = base.negative()

figure = negativeBase.horizontalRepeat(4)

draw(figure)