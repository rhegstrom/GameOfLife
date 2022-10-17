# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 07:40:09 2022

@author: Roger Hegstrom (rhegstrom@avc.edu)

Conway's Game of Life
---------------------
    RULES:
        If cell is DEAD and has 3 ALIVE neighbors --> becomes ALIVE
            
        If cell is ALIVE and has 2 or 3 ALIVE neighbors --> stays ALIVE
           otherwise --> cell DIES
"""
import numpy as np
import os
import time


ROWS    = os.get_terminal_size().lines - 1
COLUMNS = os.get_terminal_size().columns
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
board = np.random.choice([0, 1], p=[0.9, 0.1], size=(ROWS, COLUMNS))            
printBoard()
time.sleep(1)

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
   
    board = tempBoard.copy()
    printBoard()
    time.sleep(0.1)