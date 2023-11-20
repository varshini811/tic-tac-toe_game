#VR
import pygame
from Values import *
from board import Board
class Game:
    def __init__(self, ultimate=False, max=False):
        self.ultimate = ultimate
        self.max = max
        self.board = Board(ultimate=ultimate, max=max)
        self.player = 1
        self.playing = True
        pygame.font.init()

    def render_board(self, surface):
        self.board.render(surface)

    def next_turn(self):
        self.player = 2 if self.player == 1 else 1

    #ADDING WINNING STUFF FOR CODE - I THINK


    def restart(self):
        self.__init__(self.ultimate, self.max)
