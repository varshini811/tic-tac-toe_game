#Sneha's Code
#Adding Graphics
#Importing images from files

import pygame
from PIL import Image

#This graphic will be displayed if player 1 wins. SI
winning_faceX = pygame.image.load("IMG_happy1.jpg") 
screen_for_pics = pygame.display.set_mode((600,600))
screen_for_pics.fill((255, 0, 128))

#This graphic will be displayed if player 2 wins. SI
winning_faceO = pygame.image.load("IMG_happy2.jpg") 
screen_for_pics2 = pygame.display.set_mode((600,600))
screen_for_pics2.fill((255, 0, 128))

#This graphic will be displayed if player 1 loses. SI
losing_faceX = pygame.image.load("IMG_sad1.jpg")
screen_for_pics3 = pygame.display.set_mode((600,600))
screen_for_pics3.fill((255, 0, 128))

#This graphic will be displayed if player 2 loses. SI
losing_faceO = pygame.image.load("IMG_sad2.jpg")
screen_for_pics4 = pygame.display.set_mode((600,600))
screen_for_pics4.fill((255, 0, 128))

#This graphic will be displayed when player 1 is thinking about their next move. SI
thinking_faceX = pygame.image.load("IMG_thinking1.jpg")
screen_for_pics5 = pygame.display.set_mode((600,600))
screen_for_pics5.fill((255, 0, 128))

#This graphic will be displayed when player 1 is thinking about their next move. SI
thinking_faceO = pygame.image.load("IMG_thinking2.jpg")
screen_for_pics6 = pygame.display.set_mode((600,600))
screen_for_pics6.fill((255, 0, 128))
