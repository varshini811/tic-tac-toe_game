#Varshini Code

#Importing pygame and sys, import sys is used to manipulate different parts of the Python runtime environment - VR
import pygame
import sys

#Importing constants from the Values module and importing Game from the game module - VR
from Values import *
from game import Game

#This is the main class, in which the ultimate tic tac toe game will be run - VR
class Main:

    def __init__(self):
        #This is intializing the main pygame window for the game - VR
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        #This intializes the game in ultimate mode rather than having the maxium limit - VR
        pygame.display.set_caption('ULTIMATE TIC TAC TOE')
        self.game = Game(ultimate=True, max=False)

    def mainloop(self):
#This retrives the references to the screen and the diffrent game objects - VR
        screen = self.screen
        game = self.game

#This sets the screen with the background colour and rendering the initial baord game board - VR
        self.screen.fill(BG_COLOR)
        game.render_board(screen)

#This is the main game loop for the game - VR
        while True:

            for event in pygame.event.get():

                # This part is responsible for the diffrent mouse clicks - VR
                if event.type == pygame.MOUSEBUTTONDOWN and game.playing:
                    xclick, yclick = event.pos

                #This checks if the click by the user is within the set range of square, and if it is, it will mark it - VR
                    if game.board.valid_sqr(xclick, yclick):
                        game.board.mark_sqr(xclick, yclick, game.player)
                        game.board.draw_fig(screen, xclick, yclick)

                        #determining the overall winner of the game RB
                        winner = game.board.check_draw_win(screen)
                        if winner:
                        
                        #This part manages the diplay for the win and also updates the winner of the game --> RIYA IF YOU WANT TO ADD THIS
                            game.board.manage_win(screen, winner, onmain=True)
                            game.ultimate_winner(screen, winner)

                        #This switches to the next turn for the plays - VR
                        game.next_turn()

                #This handels the key pressing for the game, specifically (control 'r') in order to rest the board - VR
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.restart()
                        self.screen.fill(BG_COLOR)
                        game.render_board(screen)

                #This part of the code hadles if the game ends and closes the window - VR
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #This updates the board to display the current state of the game - VR
            pygame.display.update()

#This is the enry point of the program - VR
if __name__ == '__main__':
    main = Main()
    main.mainloop()
