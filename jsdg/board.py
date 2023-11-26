#VR
#Riya Bharadia = RB
import pygame

from Values import *
from Board_Dimensions import Dimensions

class Board:

    def __init__(self, dims=None, linewidth=15, ultimate=False, max=False):
        self.squares = [ [0, 0, 0] for row in range(DIM)]
        self.dims = dims

        if not dims: 
            self.dims = Dimensions(WIDTH, 0, 0)

        self.linewidth = linewidth
        self.offset = self.dims.sqsize * 0.2
        self.radius = (self.dims.sqsize // 2) * 0.7
        self.max = max

        if ultimate: 
            self.create_ultimate()

        self.active = True

    def __str__(self):
        s = ''
        for row in range(DIM):
            for col in range(DIM):
                sqr = self.squares[row][col]
                s += str(sqr)
        return s

    def create_ultimate(self):
        for row in range(DIM):
            for col in range(DIM):

                size = self.dims.sqsize
                xcor, ycor = self.dims.xcor + (col * self.dims.sqsize), self.dims.ycor + (row * self.dims.sqsize)
                dims = Dimensions(size=size, xcor=xcor, ycor=ycor)
                linewidth = self.linewidth - 7
                ultimate = self.max

                self.squares[row][col] = Board(dims=dims, linewidth=linewidth, ultimate=ultimate, max=False)
    
    def render(self, surface):
        for row in range(DIM):
            for col in range(DIM):
                sqr = self.squares[row][col]

                if isinstance(sqr, Board): sqr.render(surface)
        
        # vertical lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.sqsize, self.dims.ycor),                  (self.dims.xcor + self.dims.sqsize, self.dims.ycor + self.dims.size), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor), (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor + self.dims.size), self.linewidth)
        
        # horizontal lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.sqsize),                  (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.sqsize), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.size - self.dims.sqsize), (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.size - self.dims.sqsize), self.linewidth)

    def valid_sqr(self, xclick, yclick):

        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM
        if col > 2: col %= DIM

        sqr = self.squares[row][col]

        # base 
        if not isinstance(sqr, Board):
            return sqr == 0 and self.active

        # recursive step
        return sqr.valid_sqr(xclick, yclick)

    def mark_sqr(self, xclick, yclick, player):
        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM
        if col > 2: col %= DIM

        sqr = self.squares[row][col]

        print('marking -> (', row, col, ')')

        # base 
        if not isinstance(sqr, Board):
            self.squares[row][col] = player
            return

        # recursive step
        sqr.mark_sqr(xclick, yclick, player)

    def draw_fig(self, surface, xclick, yclick):
        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM
        if col > 2: col %= DIM

        sqr = self.squares[row][col]

        # base 
        if not isinstance(sqr, Board):

            # cross line
            if sqr == 1:
                # descending line
                ipos = (self.dims.xcor + (col * self.dims.sqsize) + self.offset, 
                        self.dims.ycor + (row * self.dims.sqsize) + self.offset)
                fpos = (self.dims.xcor + self.dims.sqsize * (1 + col) - self.offset, 
                        self.dims.ycor + self.dims.sqsize * (1 + row) - self.offset)
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth)

                # ascending line
                ipos = (self.dims.xcor + (col * self.dims.sqsize) + self.offset, 
                        self.dims.ycor + self.dims.sqsize * (1 + row) - self.offset)
                fpos = (self.dims.xcor + self.dims.sqsize * (1 + col) - self.offset, 
                        self.dims.ycor + (row * self.dims.sqsize) + self.offset)
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth)
            
            # circle (o)
            elif sqr == 2:
                center = (self.dims.xcor + self.dims.sqsize * (0.5 + col),
                          self.dims.ycor + self.dims.sqsize * (0.5 + row))

                pygame.draw.circle(surface, CIRCLE_COLOR, center, self.radius, self.linewidth)

            return

        # recursive step
        sqr.draw_fig(surface, xclick, yclick)


#Riya's code
    def manage_win(self, surface, winner, onmain=False): #Setting up the conditions required to win
        ''' transparent screen, acting ontop of the actual game but not altering it to be able to determine who the winner is
        this is used to keep the actual content of the game still visible but then be able to draw the X or O on top of the
        current game to show who won the mini game RB
        '''
        transparent = pygame.Surface( (self.dims.size, self.dims.size) )
        transparent.set_alpha( ALPHA )
        transparent.fill( FADE )
        if onmain: 
            surface.blit(transparent, (self.dims.xcor, self.dims.ycor))
            surface.blit(transparent, (self.dims.xcor, self.dims.ycor))
        surface.blit(transparent, (self.dims.xcor, self.dims.ycor))
        
        # so if it is not on the main board (the larger board) but on the mini boards... RB
        if not onmain:
            #drawing the big X on the duplicate board if the player who is X is the winner of that mini board RB
            if winner == 1: #if the winner was X, winner is equal to 1, so this is the drawing of the X RB
                #Since to draw the X, you need two lines intersecting, this is drawing the line that descends RB
                ipos = (self.dims.xcor + self.offset, #setting the coordinates to where the line starts RB
                        self.dims.ycor + self.offset)
                fpos = (self.dims.xcor + self.dims.size - self.offset, #setting the coordinates to where the line stops RB
                        self.dims.ycor + self.dims.size - self.offset)
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth + 7) #setting the size, color and position of that descending line RB

                #Now to complete the X the ascending line needs to be drawn RB
                ipos = (self.dims.xcor + self.offset, #setting the coordinates to where the line starts RB
                        self.dims.ycor + self.dims.size - self.offset)
                fpos = (self.dims.xcor + self.dims.size - self.offset, #setting the coordinates to where the line stops RB
                        self.dims.ycor + self.offset)
                pygame.draw.line(surface, CROSS_COLOR, ipos, fpos, self.linewidth + 7) #setting the size, color and position of the ascending line. RB

            #Repeating the same process as above except in this case instead of drawing an X, the winner is circle RB
            if winner == 2:
                center = (self.dims.xcor + self.dims.size * 0.5, #setting the center of the circle RB
                        self.dims.ycor + self.dims.size * 0.5)
                pygame.draw.circle(surface, CIRCLE_COLOR, center, self.dims.size * 0.4, self.linewidth + 7) #since pygame has a built in circle, using the center location and then setting the radius and color RB
                
        #Since the board is not "activated" or touchable to the players, setting it as false to prevent changes to the board RB
        self.active = False


    def check_draw_win(self, surface,): #defining the function that checks for the win conditions, both on the inner game and the overall game RB
        isfull = True
        ''' Creating a for loop to continously look for the wins, this starts with running the loop for each row in the range which is 3 (0 1 2)
            this way it checks through each row. And then does the same for each column. RB'''
        for row in range(DIM): 
            for col in range(DIM):
                sqr = self.squares[row][col] #defining the variable sqr as the position of the each "mini game", for example [0][0] would be the top left corner of the game RB

                if isinstance(sqr,Board) and sqr.active: #making sure the mini game is within the board and then checking to see if there is a win on it RB

                    winner = sqr.check_draw_win(surface) #setting the winner to be the square chceked through the function above RB
                    if winner:
                        self.squares[row][col] = winner
                        sqr.manage_win(surface,winner) #fulling defining the winner RB

                #checking the main large board for wins RB
                #checking for vertical wins RB
                for c in range(DIM):
                    if self.squares[0][c] == self.squares[1][c] == self.squares[2][c] != 0: #checking if the column are the same and the rows are different which would be a vertical win RB
                        color = CROSS_COLOR if self.squares[0][c] ==1 else CIRCLE_COLOR #if the one of the mini squares is an X defining the color for X otherwise the color is O RB
                        '''Now since it has been determinded if the winner is X or O, drawing the line connecting the X or O in the case of a win RB'''
                        ipos = (self.dims.xcor + self.dims.sqsize * (0.5 + c), #setting the position where the line starts for the winner RB
                                self.dims.ycor + self.offset)
                        fpos = (self.dims.xcor + self.dims.sqsize * (0.5 + c), #setting the position where the line stops RB
                                self.dims.ycor + self.dims.size - self.offset)
                        pygame.draw.line(surface, color, ipos, fpos, self.linewidth) #drawing the line with the color set depending on who the winner is RB

                        return self.squares[0][c] #returning the winner (either 1 for X or 2 for O) RB
                    
                #checking for horizontal wins using the same method above RB
                for r in range(DIM):
                    if self.squares[r][0] == self.squares[r][1] == self.squares[r][2] != 0: #this time, seeing if the columns are different while the rows stay the same RB
                        color = CROSS_COLOR if self.squares[r][0] == 1 else CIRCLE_COLOR #setting the color for the line depending if the mini game winner is X or O (1 for X and 2 for O) RB
                        '''Now since it has been determinded if the winner is X or O, drawing the line connecting the X or O in the case of a win RB'''
                        ipos = (self.dims.xcor + self.offset,
                                 self.dims.ycor + self.dims.sqsize * (r + 0.5)) #setting the position where the line starts for the winner RB
                        fpos = (self.dims.xcor + self.dims.size - self.offset,
                                 self.dims.ycor + self.dims.sqsize * (r + 0.5)) #setting the position where the line stops RB
                        pygame.draw.line(surface, color, ipos, fpos, self.linewidth) #drawing the line with the color set depending on who the winner is RB

                        return self.squares[r][0] #returning the winner (either 1 for X or 2 for O) RB
                
                #Now checking for diagonal wins which is either two cases, checking for the starting at the top left corner RB
                if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0: #checking to see if all of them have the same winner RB
                    color = CROSS_COLOR if self.squares[1][1] == 1 else CIRCLE_COLOR  #setting the color for the line depending if the mini game winner is X or O (1 for X and 2 for O) RB
                    ipos = (self.dims.xcor + self.offset, 
                            self.dims.ycor + self.offset) #setting the position where the line starts for the winner RB
                    fpos = (self.dims.xcor + self.dims.size - self.offset, 
                            self.dims.ycor + self.dims.size - self.offset) #setting the position where the line stops RB
                    pygame.draw.line(surface, color, ipos, fpos, self.linewidth) #drawing the line with the color set depending on who the winner is RB

                    return self.squares[1][1] #returning the winner (either 1 for X or 2 for O) RB

                #Now checking for diagonal wins which is either two cases, checking for the starting at the top right corner RB
                if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0: #checking to see if all of them have the same winner RB
                    color = CROSS_COLOR if self.squares[1][1] == 1 else CIRCLE_COLOR #setting the color for the line depending if the mini game winner is X or O (1 for X and 2 for O) RB
                    ipos = (self.dims.xcor + self.offset, 
                            self.dims.ycor + self.dims.size - self.offset) #setting the position where the line starts for the winner RB
                    fpos = (self.dims.xcor + self.dims.size - self.offset, 
                            self.dims.ycor + self.offset) #setting the position where the line stops RB
                    pygame.draw.line(surface, color, ipos, fpos, self.linewidth) #drawing the line with the color set depending on who the winner is RB

                    return self.squares[1][1] #returning the winner (either 1 for X or 2 for O) RB
                    

