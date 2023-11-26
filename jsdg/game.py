#VR
#Riya Bharadia = RB
import pygame
from Values import *
from board import Board
class Game:
    def restart(self):
        self.__init__(self.ultimate, self.max)

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
        

    def ultimate_winner(self, surface, winner): #setting the winning screen RB
        print('ULTIMATE WINNER! ->', winner) #winner message RB

        if winner == 1: #drawing the big X if the winner if X RB
            color = CROSS_COLOR #seting the color RB

            '''drawing the big X by splitting it into 2 lines, here are the coordinates of where each line starts and stops RB''' 
            iDesc = (WIDTH // 2 - 110, HEIGHT // 2 - 110)
            fDesc = (WIDTH // 2 + 110, HEIGHT // 2 + 110)

            iAsc = (WIDTH // 2 - 110, HEIGHT // 2 + 110)
            fAsc = (WIDTH // 2 + 110, HEIGHT // 2 - 110)

            pygame.draw.line(surface, color, iDesc, fDesc, 22) #drawing each line using the coordinates set for the start and stop RB
            pygame.draw.line(surface, color, iAsc, fAsc, 22)

        elif winner == 2: #drawing a circle if the winner is O RB
            color = CIRCLE_COLOR #setting the color RB

            center = (WIDTH // 2, HEIGHT // 2) #setting the position of the center of the circle RB
            pygame.draw.circle(surface, color, center, WIDTH // 4, 22) #drawing the circle using the pygame builtin circle while setting radius and color
        
        else:
            Game.restart()

        font = pygame.font.SysFont('monospace', 64)
        lbl = font.render('ULTIMATE WINNER!', 1, color)
        surface.blit(lbl, (WIDTH // 2 - lbl.get_rect().width // 2, HEIGHT // 2 + 220))

        self.playing = False