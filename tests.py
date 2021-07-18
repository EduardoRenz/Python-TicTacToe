from tictactoe import makeGrid,checkWinner,matchRow


from IA import IA

iaPLay = IA('o')

grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
test_grid_row = [[' ', ' ', ' '],  [' ', ' ', ' '], ['x', 'x', 'x']]
test_grid_col = [['x', ' ', 'o'], ['x', ' ', 'o'], ['x', ' ', 'o']]
test_grid_col2 = [[' ', ' ', 'o'], ['x', ' ', 'o'], ['x', ' ', 'o']]
test_grid_no_match = [[' ', 'o', ' '], [' ', 'x', 'x'], ['o', 'o', ' ']]
test_grid_diag = [['x', ' ', ' '],[' ', 'x', ' '], [' ', ' ', 'x']]

test_grid_almost_winning_x = [
    ['x', ' ', 'x'],
    [' ', 'o', ' '],
    ['o', ' ', ' ']
]

test_grid_almost_winning_o_row = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    ['o', 'o', ' ']
]

test_grid_almost_winning_o_row2 = [
    [' ', ' ', ' '],
    ['o', ' ', 'o'],
    [' ', ' ', ' ']
]

test_grid_almost_winning_o_col = [
    [' ', ' ', ' '],
    [' ', 'o', ' '],
    [' ', 'o', ' ']
]

test_grid_almost_winning_o_col2 = [
    [' ', ' ', 'o'],
    [' ', ' ', ' '],
    [' ', ' ', 'o']
]

test_grid_almost_winning_o_diag = [
    ['o', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', 'o']
]

test_grid_almost_winning_o_diag2 = [
    [' ', ' ', ' '],
    [' ', 'o', ' '],
    ['o', ' ', ' ']
]

test_grid_almost_winning_o_diag3 = [
    [' ', ' ', 'o'],
    [' ', 'o', ' '],
    [' ', ' ', ' ']
]

test_grid_almost_winning_x_diag = [
    [' ', ' ', 'x'],
    [' ', 'x', ' '],
    [' ', ' ', ' ']
]

test_grid_diag2 = [
    [' ', ' ', 'o'],
    [' ', 'o', ' '],
    ['o', ' ', ' ']
]

test_grid = """-------------
|   |   | o |
-------------
|   | o |   |
-------------
| o |   |   |
-------------"""

false_test_grid = """-------------
|   |   | x |
-------------
|   | o |   |
-------------
| o |   |   |
-------------"""



# Test if the grid is drawing correctly.
true_draw_grid_diag = makeGrid(test_grid_diag2)
print(true_draw_grid_diag)
print(test_grid)
print("Grids match and be true: ", true_draw_grid_diag == test_grid)
print("Grids not match must be false: ", false_test_grid ==test_grid)

# Test if winner will be found
print("Match winner in a row is x: ", checkWinner(test_grid_row))
print("Not Match winner in a row  : ", checkWinner(grid))
print("Match Winner in Diag is o :", checkWinner(test_grid_diag2))
print("Match Winner in Diag is x :", checkWinner(test_grid_diag))
print("Match winner in a col is x :", checkWinner(test_grid_col))
print("Match winner in a col is o :", checkWinner(test_grid_col2))

# Check for suggestions for IA
# case 1 - IA is winning in a row 2
print("Suggestion of place should be (2,2) : ", iaPLay.play(test_grid_almost_winning_o_row))
# case 2 - IA is winning in a row 1
print("Suggestion of place should be (1,1) : ", iaPLay.play(test_grid_almost_winning_o_row2))
# case 3 - IA is winning in a col
print("Suggestion of place should be (0,1) : ", iaPLay.play(test_grid_almost_winning_o_col))
# case 4 - IA is winning in a col 2
print("Suggestion of place should be (1,2) : ", iaPLay.play(test_grid_almost_winning_o_col2))
# case 5 - IA is winning in a diag
print("Suggestion of place should be (1,1) : ", iaPLay.play(test_grid_almost_winning_o_diag))
# case  no win
print("Suggestion of place should be a random spot : ", iaPLay.play(test_grid_diag))
# case check if player is winning on diag
print(makeGrid(test_grid_almost_winning_x_diag))
print("Suggestion of place diag x winning should be (2,0) : ", iaPLay.play(test_grid_almost_winning_x_diag))

# # Check if ia can win in cols
# print(makeGrid(test_grid_almost_winning_o_col))
# print(iaPLay.play(test_grid_almost_winning_o_col))

# print(makeGrid(test_grid_almost_winning_o_col2))
# print(iaPLay.play(test_grid_almost_winning_o_col2))

# # Check if ia can win in diag
# print(makeGrid(test_grid_almost_winning_o_diag2))
# print(iaPLay.play(test_grid_almost_winning_o_diag2))

# print(makeGrid(test_grid_almost_winning_o_diag))
# print(iaPLay.play(test_grid_almost_winning_o_diag))

# print(makeGrid(test_grid_almost_winning_o_diag3))
# print(iaPLay.play(test_grid_almost_winning_o_diag3))
