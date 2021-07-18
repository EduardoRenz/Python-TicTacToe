import random
from collections import Counter
def flatten(matrix): return [item for row in matrix for item in row]

def makeGrid(grid):
    new_grid = ''
    for i,x in enumerate(grid):
        new_grid += "-------------\n"
        col = ''
        for y in grid[i]:
            col += f'| {y} '
        #print(col + '|')
        new_grid += col + '|\n'
        col = ''
        #new_grid += '|'
    new_grid += "-------------"
    return new_grid

#Check if we have a sequential of 3 times a player
def checkAllIsPlayer(flatten_grid, player):
    if all(map(lambda val: val == player, flatten_grid)):
        return player
    return False

#Check if match 3 times in a row of grid
def matchRow(grid):
    flatten_grid = flatten(grid)
    i = 0
    while i < len(flatten_grid):
        if checkAllIsPlayer(flatten_grid[i:i+3], 'x'):
            return 'x'
        if checkAllIsPlayer(flatten_grid[i:i+3], 'o'):
            return 'o'
        i += 3
    return False

#Check if match 3 times in a column of grid
def matchCol(grid):
    flatten_grid = flatten(grid)
    i = 0
    values = []

    while i < 3:
        if checkAllIsPlayer(flatten_grid[i::3], 'x'):
            return 'x'
        if checkAllIsPlayer(flatten_grid[i::3], 'o'):
            return 'o'
        i += 1
        values = []
    return values

#Check if match 3 times in diagonal of a grid
def matchDiag(grid):
    def getDiagValues(grid):
        flatten_grid = flatten(grid)
        indexes = list(range(0, len(flatten_grid)))
        diag_indexes = list(filter(lambda x: x % 4 == 0, indexes))
        diag_values = [flatten_grid[i] for i in diag_indexes]
        return diag_values

    if checkAllIsPlayer(getDiagValues(grid), 'x') or checkAllIsPlayer(getDiagValues(grid[::-1]), 'x'):
        return 'x'
    if checkAllIsPlayer(getDiagValues(grid), 'o') or checkAllIsPlayer(getDiagValues(grid[::-1]), 'o'):
        return 'o'
    return False


# Check if game is drawn
def isDraw(grid):
    # Count number of empty spaces, if there is no empty space return False
    if not any(map(lambda val: val.strip() == '', flatten(grid))):
        return True
    return False
    

# Check if we have one winner
def checkWinner(grid):
    match_row = matchRow(grid)
    if match_row:
        return match_row

    match_col = matchCol(grid)
    if match_col:
        return match_col

    match_diag = matchDiag(grid)
    if match_diag:
        return match_diag


def DummyIAPlay(grid,player='o'):
    rand_row = random.randrange(0,3)
    rand_col = random.randrange(0,3)
    
    if grid[rand_row][rand_col].strip() == '':
        print(grid[rand_row][rand_col].strip())
        print(rand_col,rand_col)
        return rand_row, rand_col
    
    else:
        return DummyIAPlay(grid,player)


