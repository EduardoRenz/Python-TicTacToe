from tictactoe import makeGrid,checkWinner,matchRow


from IA import IA

iaPLay = IA('o')

grid = [['', '', ''], ['', '', ''], ['', '', '']]
test_grid_row = [['', '', ''],  ['', '', ''], ['x', 'x', 'x']]
test_grid_col = [['x', '', 'o'], ['x', '', 'o'], ['x', '', 'o']]
test_grid_col2 = [['', '', 'o'], ['x', '', 'o'], ['x', '', 'o']]
test_grid_no_match = [['', 'o', ''], ['', 'x', 'x'], ['o', 'o', '']]
test_grid_diag = [
    ['x', '', ''],
    ['', 'x', ''],
    ['', '', 'x']
]
test_grid_diag2 = [
    ['', '', 'o'],
    ['', 'o', ''],
    ['o', '', '']
]

test_grid_almost_winning_x = [
    ['x', '', 'x'],
    ['', 'o', ''],
    ['o', '', '']
]

test_grid_almost_winning_o_row = [
    ['', '', ''],
    ['', '', ''],
    ['o', 'o', '']
]

test_grid_almost_winning_o_row2 = [
    ['', '', ''],
    ['o', 'o', ''],
    ['', '', '']
]


test_grid_almost_winning_o_col = [
    ['', '', ''],
    ['', 'o', ''],
    ['', 'o', '']
]


test_grid_almost_winning_o_col2 = [
    ['', '', 'o'],
    ['', '', ''],
    ['', '', 'o']
]


test_grid = """-------------
|  |  | o |
-------------
|  | o |  |
-------------
| o |  |  |
-------------"""

false_test_grid = """-------------
|  |  | x |
-------------
|  | o |  |
-------------
| o |  |  |
-------------"""



# Test if the grid is drawing correctly.
true_draw_grid_diag = makeGrid(test_grid_diag2)
print("Grids match and be true: ", true_draw_grid_diag ==test_grid)
print("Grids not match must be false: ", false_test_grid ==test_grid)

# Test if winner will be found
print("Match winner in a row is x: ", checkWinner(test_grid_row))
print("Not Match winner in a row  : ", checkWinner(grid))
print("Match Winner in Diag is o :", checkWinner(test_grid_diag2))
print("Match Winner in Diag is x :", checkWinner(test_grid_diag))
print("Match winner in a col is x :", checkWinner(test_grid_col))
print("Match winner in a col is o :", checkWinner(test_grid_col2))
# print("Not Match Diag x :", matchDiag(test_grid_row))

# print("No match ", matchDiag(test_grid_no_match))
# print("No match ", matchRow(test_grid_no_match))
# print("Match col x: ", matchCol(test_grid_col))

# Check if ia can win in rows
# case 1
print(makeGrid(test_grid_almost_winning_o_row))
print(iaPLay.play(test_grid_almost_winning_o_row))
# case 2
print(makeGrid(test_grid_almost_winning_o_row2))
print(iaPLay.play(test_grid_almost_winning_o_row2))

# case 3 - no win
print(makeGrid(test_grid_diag))
print(iaPLay.play(test_grid_diag))

# Check if ia can win in cols
print(makeGrid(test_grid_almost_winning_o_col))
print(iaPLay.play(test_grid_almost_winning_o_col))

# print(makeGrid(test_grid_almost_winning_o_col2))
# print(IAPlay(test_grid_almost_winning_o_col2))