"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """       
    num_of_x = 0
    num_of_o = 0
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                num_of_x += 1
            elif board[i][j] == O:
                num_of_o += 1
    
    if num_of_x > num_of_o:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()   
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.add((i, j))
              
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board
        


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
     # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None
    # for i in range(len(board)):
    #     # check all columns
    #     if board[0][i] == board[1][i] and  board[1][i] == board[2][i] and board[2][i] != EMPTY:
    #         return board[0][i]

    #     # check all rows
    #     elif  board[i][0] == board[i][1] and  board[i][1] == board[i][2] and board[i][2] != EMPTY:
    #         the_winner = board[i][0]
    #         return the_winner
        
    #     else:
    #         return None

        # # check all diagonals 
        # elif board[0][0] == board[1][1] and  board[1][1] == board[2][2] and board[2][2] != EMPTY:
        #     the_winner = board[0][0]
        #     return the_winner
 
        # elif board[0][2] == board[1][1] and  board[1][1] == board[2][0] and board[2][0] != EMPTY:
        #     the_winner = board[0][2]
        #     return the_winner
        # else:
        #     the_winner = EMPTY
        #     return the_winner



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) == X or winner(board) == O or all(col != EMPTY for row in board for col in row)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


    
def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move