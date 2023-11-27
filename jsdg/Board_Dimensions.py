#Varshini's Code

#Importing constants from the Values module - VR
from Values import *
#This represents the size and coordinates of the game board - VR
class Dimensions:

    def __init__(self, size, xcor, ycor):
        #This initalizes the dimensions with the provided size and coordinates of the board - VR

        self.size = size
        #This calculates the size of each square within the component based on the global DIM value - VR

        self.sqsize = size // DIM
        
        #This sets the the x and y coordinates of the component - VR
        self.xcor = xcor
        self.ycor = ycor