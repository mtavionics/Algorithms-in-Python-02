# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:08:05 2021
Project 2
@author: Mikhail Terentev

"""

# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')    
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])    
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def inputPlayerLetter():
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    return ['X', 'O']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[6] == le and bo[7] == le and bo[8] == le) or # across the bottom
    (bo[0] == le and bo[3] == le and bo[6] == le) or # down the left side
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the middle
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the right side
    (bo[0] == le and bo[4] == le and bo[8] == le) or # diagonal
    (bo[2] == le and bo[4] == le and bo[6] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
    
def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    move = input('Please enter your move (0-8): ')
    while move not in '0 1 2 3 4 5 6 7 8'.split() or not isSpaceFree(board, int(move)):
        print('Sorry, that position has already been taken!')
        move = input('Please enter your move (0-8): ')
    return int(move)


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 4):
        return 4

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [1, 3, 5, 7])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True


print('Tic-Tac-Toe!')
print(' 0 | 1 | 2')
print('----------')
print(' 3 | 4 | 5')
print('----------')
print(' 6 | 7 | 8')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The player use ‘X’ mark and the computer use ‘O’ mark.')
    print('The ' + turn + ' will go first.')
    
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':
            # Player's turn.    
            print('Your turn:')
            
            move = getPlayerMove(theBoard)
            
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):

                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
            
            
        else:
            # Computer's turn.
            print('Computer move:')
            
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):

                print('Sorry! The winner is Computer!!! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
            
        drawBoard(theBoard)
        
    if not playAgain():
        break
    
    
'''
Output:
    

Tic-Tac-Toe!
 0 | 1 | 2
----------
 3 | 4 | 5
----------
 6 | 7 | 8
The player use ‘X’ mark and the computer use ‘O’ mark.
The player will go first.
Your turn:

Please enter your move (0-8): 4
   |   |  
-----------
   | X |  
-----------
   |   |  
Computer move:
   |   |  
-----------
   | X |  
-----------
 O |   |  
Your turn:

Please enter your move (0-8): 0
 X |   |  
-----------
   | X |  
-----------
 O |   |  
Computer move:
 X |   |  
-----------
   | X |  
-----------
 O |   | O
Your turn:

Please enter your move (0-8): 7
 X |   |  
-----------
   | X |  
-----------
 O | X | O
Computer move:
 X | O |  
-----------
   | X |  
-----------
 O | X | O
Your turn:

Please enter your move (0-8): 3
 X | O |  
-----------
 X | X |  
-----------
 O | X | O
Computer move:
 X | O |  
-----------
 X | X | O
-----------
 O | X | O
Your turn:

Please enter your move (0-8): 2
 X | O | X
-----------
 X | X | O
-----------
 O | X | O
The game is a tie!
Do you want to play again? (yes or no)

yes
The player use ‘X’ mark and the computer use ‘O’ mark.
The computer will go first.
Computer move:
 O |   |  
-----------
   |   |  
-----------
   |   |  
Your turn:

Please enter your move (0-8): 4
 O |   |  
-----------
   | X |  
-----------
   |   |  
Computer move:
 O |   |  
-----------
   | X |  
-----------
   |   | O
Your turn:

Please enter your move (0-8): 6
 O |   |  
-----------
   | X |  
-----------
 X |   | O
Computer move:
 O |   | O
-----------
   | X |  
-----------
 X |   | O
Your turn:

Please enter your move (0-8): 5
 O |   | O
-----------
   | X | X
-----------
 X |   | O
Computer move:
Sorry! The winner is Computer!!! You lose.
 O | O | O
-----------
   | X | X
-----------
 X |   | O
Do you want to play again? (yes or no)

yes
The player use ‘X’ mark and the computer use ‘O’ mark.
The player will go first.
Your turn:

Please enter your move (0-8): 4
   |   |  
-----------
   | X |  
-----------
   |   |  
Computer move:
   |   |  
-----------
   | X |  
-----------
   |   | O
Your turn:

Please enter your move (0-8): 2
   |   | X
-----------
   | X |  
-----------
   |   | O
Computer move:
   |   | X
-----------
   | X |  
-----------
 O |   | O
Your turn:

Please enter your move (0-8): 7
   |   | X
-----------
   | X |  
-----------
 O | X | O
Computer move:
   | O | X
-----------
   | X |  
-----------
 O | X | O
Your turn:

Please enter your move (0-8): 3
   | O | X
-----------
 X | X |  
-----------
 O | X | O
Computer move:
   | O | X
-----------
 X | X | O
-----------
 O | X | O
Your turn:

Please enter your move (0-8): 0
 X | O | X
-----------
 X | X | O
-----------
 O | X | O
The game is a tie!
Do you want to play again? (yes or no)

yes
The player use ‘X’ mark and the computer use ‘O’ mark.
The player will go first.
Your turn:

Please enter your move (0-8): 0
 X |   |  
-----------
   |   |  
-----------
   |   |  
Computer move:
 X |   |  
-----------
   |   |  
-----------
 O |   |  
Your turn:

Please enter your move (0-8): 4
 X |   |  
-----------
   | X |  
-----------
 O |   |  
Computer move:
 X |   |  
-----------
   | X |  
-----------
 O |   | O
Your turn:

Please enter your move (0-8): 7
 X |   |  
-----------
   | X |  
-----------
 O | X | O
Computer move:
 X | O |  
-----------
   | X |  
-----------
 O | X | O
Your turn:

Please enter your move (0-8): 6
Sorry, that position has already been taken!

Please enter your move (0-8): 5
 X | O |  
-----------
   | X | X
-----------
 O | X | O
Computer move:
 X | O |  
-----------
 O | X | X
-----------
 O | X | O
Your turn:

Please enter your move (0-8): 2
 X | O | X
-----------
 O | X | X
-----------
 O | X | O
The game is a tie!
Do you want to play again? (yes or no)

yes
The player use ‘X’ mark and the computer use ‘O’ mark.
The computer will go first.
Computer move:
 O |   |  
-----------
   |   |  
-----------
   |   |  
Your turn:

Please enter your move (0-8): 2
 O |   | X
-----------
   |   |  
-----------
   |   |  
Computer move:
 O |   | X
-----------
   |   |  
-----------
   |   | O
Your turn:

Please enter your move (0-8): 4
 O |   | X
-----------
   | X |  
-----------
   |   | O
Computer move:
 O |   | X
-----------
   | X |  
-----------
 O |   | O
Your turn:

Please enter your move (0-8): 7
 O |   | X
-----------
   | X |  
-----------
 O | X | O
Computer move:
Sorry! The winner is Computer!!! You lose.
 O |   | X
-----------
 O | X |  
-----------
 O | X | O
Do you want to play again? (yes or no)

yes
The player use ‘X’ mark and the computer use ‘O’ mark.
The player will go first.
Your turn:

Please enter your move (0-8): 4
   |   |  
-----------
   | X |  
-----------
   |   |  
Computer move:
 O |   |  
-----------
   | X |  
-----------
   |   |  
Your turn:

Please enter your move (0-8): 2
 O |   | X
-----------
   | X |  
-----------
   |   |  
Computer move:
 O |   | X
-----------
   | X |  
-----------
 O |   |  
Your turn:

Please enter your move (0-8): 3
 O |   | X
-----------
 X | X |  
-----------
 O |   |  
Computer move:
 O |   | X
-----------
 X | X | O
-----------
 O |   |  
Your turn:

Please enter your move (0-8): 7
 O |   | X
-----------
 X | X | O
-----------
 O | X |  
Computer move:
 O | O | X
-----------
 X | X | O
-----------
 O | X |  
Your turn:

Please enter your move (0-8): 8
 O | O | X
-----------
 X | X | O
-----------
 O | X | X
The game is a tie!
Do you want to play again? (yes or no)

yes
The player use ‘X’ mark and the computer use ‘O’ mark.
The player will go first.
Your turn:

Please enter your move (0-8): 8
   |   |  
-----------
   |   |  
-----------
   |   | X
Computer move:
 O |   |  
-----------
   |   |  
-----------
   |   | X
Your turn:

Please enter your move (0-8): 2
 O |   | X
-----------
   |   |  
-----------
   |   | X
Computer move:
 O |   | X
-----------
   |   | O
-----------
   |   | X
Your turn:

Please enter your move (0-8): 6
 O |   | X
-----------
   |   | O
-----------
 X |   | X
Computer move:
 O |   | X
-----------
   | O | O
-----------
 X |   | X
Your turn:

Please enter your move (0-8): 7
Hooray! You have won the game!
 O |   | X
-----------
   | O | O
-----------
 X | X | X
Do you want to play again? (yes or no)

no



'''