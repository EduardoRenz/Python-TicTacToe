from tictactoe import makeGrid,checkWinner,IAPlay
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
print(IAPlay(grid))