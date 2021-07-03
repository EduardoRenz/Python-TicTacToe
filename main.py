from tictactoe import checkWinner, makeGrid,DummyIAPlay

grid = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]


playing = 'x'

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

    #Ia Turn
    ia_row,ia_col = DummyIAPlay(grid)
    grid[ia_row][ia_col] = 'o'

    #playing = 'x' if playing == 'o' else 'o'

    winner = checkWinner(grid)
    if winner:
        print(f"Game Over, player {winner} Wins!")
        break

n_grid = makeGrid(grid)
print(n_grid)

