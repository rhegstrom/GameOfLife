# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 07:40:09 2022

@author: Roger Hegstrom (rhegstrom@avc.edu)

NOTE:  
     - I WOULD RUN THIS ON THE COMMAND LINE AND NOT IN SPYDER ex: python main.py
     
      
Conway's Game of Life
---------------------
    RULES:
        If cell is DEAD and has 3 ALIVE neighbors --> becomes ALIVE
            
        If cell is ALIVE and has 2 or 3 ALIVE neighbors --> stays ALIVE
           otherwise --> cell DIES

    Display the 20x20 grid at each step, observe how the game progresses.        
           
Report on:
    1. what was the fewest number of steps (from a random beginning) until all cells are 'dead,'
    2. what was the smallest number of steps until a stable configuration was found.  Put these answers in comments in the code.  
    
    I ran the program 20 times:
       The smallest number of steps to reach a stable configuration was 34
       The smallest number of steps for all cells to die was 88(HAPPENED ONLY ONCE)
    
 
"""
import numpy as np
import os
import time


#ROWS    = os.get_terminal_size().lines - 1
#COLUMNS = os.get_terminal_size().columns

ROWS    = 20
COLUMNS = 20

ALIVE   = 1
DEAD    = 0


def calculateAliveNeighbors(row,col):
    """
    Returns the alive neighbors of (row, col) on the board

    Parameters
    ----------
    row : int
        row in the board array.
    col : int
        column in the board array.

    Returns
    -------
    alive_neighbors : int
        Number of alive neighbors.

    """    
    # Keep values in the proper ranges within the board matrix
    row_begin = (row-1) if (row-1) >= 0 else 0
    row_end   = (row+2) if (row+2) < ROWS else ROWS
    
    col_begin = (col-1) if (col-1) >= 0 else 0
    col_end   = (col+2) if (col+2) < COLUMNS else COLUMNS

    alive_neighbors = (np.sum(board[row_begin:row_end, col_begin:col_end])
                       - board[row, col])
    
    return alive_neighbors


def printBoard():
    """
    Prints the current board to screen

    Returns
    -------
    None.

    """
    os.system('cls')
    for row in range(ROWS):
        for col in range(COLUMNS):
            print('#' if board[row, col] == ALIVE else ' ', end='')
        print('')
            



# Populate initial board with random values and print board
board = np.random.choice([0, 1], p=[0.6, 0.4], size=(ROWS, COLUMNS))    

previousBoard = np.zeros((20,20))
        
printBoard()
time.sleep(1)

steps = 0
# Main Program Loop
while True:
    tempBoard = np.zeros((ROWS, COLUMNS), dtype=int) # next iteration board
    for row in range(ROWS):
        for col in range(COLUMNS):
            alive_neighbors = calculateAliveNeighbors(row, col)
            if ((board[row, col] == ALIVE and alive_neighbors in (2, 3)) 
            or (board[row, col] == DEAD and alive_neighbors == 3)):
                tempBoard[row, col] = ALIVE
            else:
                tempBoard[row, col] = DEAD            
                
    steps = steps + 1
    if ( (previousBoard == board).all() or (previousBoard == tempBoard).all()):
        print(f"(steps={steps}) A stable state has been achieved...")
        exit(0)
                
    previousBoard = board.copy()
    board = tempBoard.copy()
    printBoard()
    
    if (np.sum(board) == 0 ):
        print(f"(steps={steps}) A stable state has been reached(all cells died)...")
#    time.sleep(0.1)