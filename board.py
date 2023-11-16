# Tic Tac Toe
# Riya Bharadia = RB
#Varshini Rajakuamarn = VR

import random #importing the class random, so that it can be used later on in the program RB

def drawBoard(board):
    # This function prints out the board that it was passed.
    '''
    Makes the tictactoe board with a number associated with each square so that when the game is being played each square has an 
    # accoiated number to call upon RB
    '''
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9]) #Printing and Assigning the top row of the board positions 7, 8, 9 RB
    print('-+-+-') # Making the lines between the row RB
    print(board[4] + '|' + board[5] + '|' + board[6]) #Printing and Assigning the top row of the board positions 4, 5, 6 RB
    print('-+-+-') #Making the lines between the row RB
    print(board[1] + '|' + board[2] + '|' + board[3]) #Printing and Assigning the top row of the board positions 1, 2, 3 RB

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    '''
    Part of the set up before running the game, where the player chooses if they want to be X or O, allows the player to input what 
    they want to be, and then checks to see if the input is actually X or O by converting the input to all upper case and then using
    an if statement to confrim the choice of the player and the computer. This returns the string of X or O in the order list of
    which one is the player's vs the computer's (the player's is first and the computer's is second) RB
    '''
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = '' #Assigning an empty string to letter RB
    while not (letter == 'X' or letter == 'O'): #Using while to make sure the input from the player is X or O and then the code continues RB
        print('Do you want to be X or O?') #Printing the question that is asked to the player RB
        letter = input().upper() #Requesting an input from the player and assigning the input to letter, and converting it to upper case to compare with the while statement RB

    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X': #Checcking to see what the player picked and then assigning the player and the computer their corresponding letters RB
        return ['X', 'O'] #if the player picked X RB
    else:
        return ['O', 'X'] #otherwise the computer gets X RB

def whoGoesFirst():
    # Randomly choose the player who goes first.
    '''
    Still part of the set up of the game to determine who gets to go first, this is is a random choice, that has no determining factors
    the ranint is called from the random class, and is used between 0 and 1, where is 0 is randomally picked then the computer starts,
    whereas if 1 is randomally picked then the player starts, and this is done via if statement as well. This returns the string of the 
    name of the person (player or computer) who will get to start. RB
    '''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    '''
    This function runs through all the possible win cases and returns True is one of them has occured signifying that there is a winner
    in this case the player. The function uses 'and' and 'or' to be able to make different cases (separated by 'or') and have each case
    have three specific criteria for it to be True (each one outlined and then separated by 'and'). RB
    '''
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    # Check if 'move' falls under the range of 1-9 or if the space correlating with 'move' is free for it to be a valid input.
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        # If the entered 'move' does not meet the conditions, the loop will prompt the user to input a new move. The loop will continue till a valid move is entered to proceed to the next part of the code.
        print('What is your next move? (1-9)')
        move = input()
        # After a valid move has been entered, the program will return the value of the move in its integer form.
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Initializes 'possibleMoves', an empty list to store the valid inputs for move.
    possibleMoves = []
    # 'i' is iterated through each element in movesList, which is a list of potential moves.
    for i in movesList:
        # Check if 'i' is a free space on the gameboard.
        if isSpaceFree(board, i):
            # If i meets the condition, then it will be added to the possibleMoves list.
            possibleMoves.append(i)
    # Check if there are any valid moves altogether in possibleMoves.
    if len(possibleMoves) != 0:
        # If there are valid moves, a random move is selected from possibleMoves and is returned.
        return random.choice(possibleMoves)
    # If there are no valid moves, the function returns None.
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    # Checks which letter the computer and user are playing as. If the computer is using 'X', then the user is playing as 'O'. 
    if computerLetter == 'X':
        playerLetter = 'O'
        # If not, then the game assumes that the computer is playing as 'O', and the user is playing as 'X'.
    else:
        playerLetter = 'X'

    # The code below outlines the algorithm that AI uses to make moves, and checks if the computer won
    # First, check if we can win in the next move by reinforcing the available moves positions (1 to 9) on the board
    for i in range(1, 10):
        # A copy of the existing gameboard is made.
        boardCopy = getBoardCopy(board)
        # Computer's letter is replicated using 'makeMove'. 
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            # Checks if the computer wins from the boardCopy, by setting conditions of winning to isWinner. 
            # If computer can win the next round, the game returns 'i', leading to victory
            if isWinner(boardCopy, computerLetter):
                return i

    # Checks if the player could win on his next move, and block them by putting down the computer's letter (X or O) in that position.
    # Checking the available positions on the board range(1, 10).

    for i in range(1, 10):
        # Refers back to the copy of the existing board game
        boardCopy = getBoardCopy(board)
        # Checks if the user can win on the next move.
        # Checking if i is free
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            # If the user is going to win, the computer returns 'i' in that position.
            if isWinner(boardCopy, playerLetter):
                return i

    # If neither the computer nor the user is winning, the computer tries to take one of the corners, if they are free.
    # Checking if the corners [positions 1,3,7,0] are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    # If any of the corner positions are free, the computer outputs its move there.
    if move != None:
        return move

    # If the corner positions are not free, the computer tries to occupy the center [position 5], if it is free.
    if isSpaceFree(board, 5):
        return 5

    # If neither the corners nor the centre is free, the computer places its move on one of the sides [positions 2, 4, 6, or 8].
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False. VR
   
    #This for loop iterates through the numbers from 1 to 9. This range represents the spaces on the game board. VR
    for i in range(1, 10):
       
        #This loop checks is a specific space is free ir not. It will return True of the space is unoccupied and False if the space is occupied VR
        if isSpaceFree(board, i):
            #This will return false if any space on the board is found to be free (when isSpaceFree returns True). This means that the birad is not yet full and has at least one unoccpied space. VR
            return False
        #This will complete the loop and return true indicating that all spaces have been occupied. VR

    return True

#This will print Welcome to Tic Tac Toe! and will be displayed to the user/player of the game VR
print('Welcome to Tic Tac Toe!')

#This line starts an infinite game loop. VR
while True:
    '''
    This will first reset the board.
    Initializing the game board as a list of 10 elements.
    The board is represented as a list where each element corresponds to a space on the board.
    The spaces are initially empty (' '). VR
    '''
    theBoard = [' '] * 10
   
    ''''
    This line calls a function (inputPlayerLetter()), to determine the player's
    role in the game, (X or O)  and the computer's letter. These letters will be used to
    represent each player's moves on the game board. VR
    '''
   
    playerLetter, computerLetter = inputPlayerLetter()
   
    #This line calls a function  whoGoesFirst(), to determine which player goes first. VR
    turn = whoGoesFirst()
   
    #This line displays a message to inform the player about the starting player. VR
    print('The ' + turn + ' will go first.')
   
    ''''
    This line sets the gameIsPlaying variable to True. As long as gameIsPlaying
    remains True, the game loop will continue running. VR
    '''
    gameIsPlaying = True

    while gameIsPlaying: ''''
                        loop continues to execute as long as the gameIsPlaying variable is True.
                        Game keeps running until a win, a tie, or some other condition
                        is met that sets gameIsPlaying to False. VR
                        '''
    if turn == 'player': # Player's turn. VR
            drawBoard(theBoard)  # Display the current game board. VR
            move = getPlayerMove(theBoard) # Get the player's move. VR
            makeMove(theBoard, playerLetter, move) # Update the game board with the player's move. VR

            if isWinner(theBoard, playerLetter): #Checks if the player has won the game VR
                drawBoard(theBoard) #display the current state of the game board VR
                print('Hooray! You have won the game!') # If the player has won, this line prints a congratulatory message to the player VR
                gameIsPlaying = False # The game ends because the player has won. VR
            else: #If the player has not won, the code proceeds to the else part of the conditional. VR
                if isBoardFull(theBoard): #checks if the game board is full, checks if no more moves can be made VR
                    drawBoard(theBoard) #display the final state of the game board. VR
                    print('The game is a tie!') #This line prints a message indicating that the game has ended in a tie because there's no winner and no more available moves. VR
                    break # The game is a tie, so exit the loop. VR
                else:
                    turn = 'computer' # Switch to the computer's turn. VR

    else: #This indicates that it is now the computers turn VR
            move = getComputerMove(theBoard, computerLetter) # Get and returns the the computer's move. VR
            makeMove(theBoard, computerLetter, move) # Update the game board with the computer's move. VR

            if isWinner(theBoard, computerLetter): #Checks if the computer has won the game. VR
                drawBoard(theBoard) #display the current state of the game board VR
                print('The computer has beaten you! You lose.') #prints a message to inform the player that the computer has won the game. VR
                gameIsPlaying = False # The game loop ends because the computer has won. VR
            else: #Indicate when it's neither the player's turn nor the computer's turn, indicating that the game is still in progress. VR
                if isBoardFull(theBoard): #Checks if the game board is full, meaning there are no more empty spaces for moves. VR
                    drawBoard(theBoard) # Update the game board VR
                    print('The game is a tie!') # line prints a message to inform the players that the game has ended in a tie VR
                    break # The game is a tie, so exit the loop. VR
                else:
                    turn = 'player' # Switch back to the player's turn. VR

    print('Do you want to play again? (yes or no)') #line prints a message to the player, asking if they would like to start a new game. VR
    if not input().lower().startswith('y'): '''
                                            This line reads the player's input, which is expected to be either "yes" or "no", this is case senstive
                                            input() is a function that waits for the player to type something and press Enter.
                                            .lower() is used to convert the input to lowercase.
                                            This is done to make the comparison case-insensitive, so the player's response
                                            can be in any combination of uppercase and lowercase letters.
                                            startswith('y') checks if the input begins with the letter 'y'.
                                            VR '''
'''
              if the player's input does not start with 'y' (meaning they did not enter "yes"), the break statement is executed.
              This causes the program to exit the game loop and, might end the game completely
              VR '''