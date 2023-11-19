#VR
from Values import *

class Dimensions:

    def __init__(self, size, xcor, ycor):
        self.size = size
        self.sqsize = size // DIM
        self.xcor = xcor
        self.ycor = ycor