from tictactoe import DummyIAPlay, checkWinner, isDraw, makeGrid
from IA import IA

grid = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]


playing = 'x'
ia = IA('o')

while True:
    n_grid = makeGrid(grid)
    print(n_grid)

    row = int(input("Choose the row: "))
    col = int(input("Choose the column: "))

    #player turn
    if grid[row][col] != ' ':
        print("Please, choose another place!")
        continue

    grid[row][col] = playing

    #check draw
    if isDraw(grid):
        print("Draw!")
        break


    #Ia Turn
    #ia_row,ia_col = DummyIAPlay(grid)
    ia_row,ia_col = ia.play(grid)
    grid[ia_row][ia_col] = 'o'

    #check winner
    winner = checkWinner(grid)
    if winner:
        print(f"Game Over, player {winner} Wins!")
        break


n_grid = makeGrid(grid)
print(n_grid)

