#Varshini's Code

#Importing pygame, importing constants from the Values module and importing Board from the board module - VR

import pygame
from Values import *
from board import Board
#This class represnts the behavior and stae of the game - VR
class Game:
    def __init__(self, ultimate=False, max=False):

        #This part initializing the game with specified modes - VR
        self.ultimate = ultimate
        self.max = max
        
        #This creates the board game based on the specified modes - VR
        self.board = Board(ultimate=ultimate, max=max)

        #This indicates the current player of the game (player 1 or 2) - VR
        self.player = 1

        #This part indicates that the game is currently in progress - VR
        self.playing = True

        #This initializing the font module from pygame - VR
        pygame.font.init()

    #This renders the state of the game board on the specifed surface - VR
    def render_board(self, surface):
        self.board.render(surface)

    #This part switches the players turn, gives the turn to the next player of the game - VR
    def next_turn(self):
        self.player = 2 if self.player == 1 else 1
        
    #This part of the code is responsible for hadeling the displaya nd action when there is an "ultimate" winner for the game - VR
    def ultimate_winner(self, surface, winner):
        print('ULTIMATE WINNER! ->', winner)

        #This part of tehe code draws an "X" if player 1 wins and draws a "O" if player 2 wins - VR
        if winner == 1:
            color = CROSS_COLOR

            #Theses are the coordinates for drawing the X - VR
            iDesc = (WIDTH // 2 - 110, HEIGHT // 2 - 110)
            fDesc = (WIDTH // 2 + 110, HEIGHT // 2 + 110)

            iAsc = (WIDTH // 2 - 110, HEIGHT // 2 + 110)
            fAsc = (WIDTH // 2 + 110, HEIGHT // 2 - 110)

            #This is the code to draw the X - VR
            pygame.draw.line(surface, color, iDesc, fDesc, 22)
            pygame.draw.line(surface, color, iAsc, fAsc, 22)

        else:
            color = CIRCLE_COLOR

            #Theses are the coordinates for drawing the O - VR
            center = (WIDTH // 2, HEIGHT // 2)

            #This is the code to draw the O - VR
            pygame.draw.circle(surface, color, center, WIDTH // 4, 22)

        #This will display a message for the ultimate winner message - VR
        font = pygame.font.SysFont('monospace', 64)
        lbl = font.render('ULTIMATE WINNER!', 1, color)
        surface.blit(lbl, (WIDTH // 2 - lbl.get_rect().width // 2, HEIGHT // 2 + 220))

        #Indicates that it is the end of the game - VR
        self.playing = False

    #Thsi resstes the game to the intial game board - VR
    def restart(self):
        self.__init__(self.ultimate, self.max)
