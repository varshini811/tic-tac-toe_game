#VR
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
        

    def ultimate_winner(self, surface, winner):
        print('ULTIMATE WINNER! ->', winner)

        if winner == 1:
            color = CROSS_COLOR

            iDesc = (WIDTH // 2 - 110, HEIGHT // 2 - 110)
            fDesc = (WIDTH // 2 + 110, HEIGHT // 2 + 110)

            iAsc = (WIDTH // 2 - 110, HEIGHT // 2 + 110)
            fAsc = (WIDTH // 2 + 110, HEIGHT // 2 - 110)

            pygame.draw.line(surface, color, iDesc, fDesc, 22)
            pygame.draw.line(surface, color, iAsc, fAsc, 22)

        elif winner == 2:
            color = CIRCLE_COLOR

            center = (WIDTH // 2, HEIGHT // 2)
            pygame.draw.circle(surface, color, center, WIDTH // 4, 22)
        
        else:
            Game.restart()

        font = pygame.font.SysFont('monospace', 64)
        lbl = font.render('ULTIMATE WINNER!', 1, color)
        surface.blit(lbl, (WIDTH // 2 - lbl.get_rect().width // 2, HEIGHT // 2 + 220))

        self.playing = False