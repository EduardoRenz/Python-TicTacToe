from collections import Counter
from tictactoe import flatten
class IA() :
    player = None
    opponent = None
    def __init__(self, player='o'):
        self.player = player
        self.opponent = 'x' if self.player == 'o' else 'o'


    def __countPlayerOnArray(self, arr, player):
        count = Counter(arr)
        return count[player]

    def __getEmptySpot(self,arr):
        return arr.index('')

    #Check rows for almost winning
    def checkForRowWinning(self,grid,player):
        for i,val in enumerate(grid):
            n_count = self.__countPlayerOnArray(grid[i],self.player)
            if n_count >=2:
                empty_indx = self.__getEmptySpot(grid[i])
                print(f"Player {player} have {n_count} on row {i} on place at {i,empty_indx}")
                return i, empty_indx
        return None

    def checkForColWinning(self,grid,player):
        for i,val in enumerate(grid):
            flatten_grid = flatten(grid)
            n_count = self.__countPlayerOnArray(flatten_grid[i::3],self.player)
            if n_count >=2:
                empty_indx = self.__getEmptySpot(flatten_grid[i::3])
                print(f"Player {player} have {n_count} ,  place at {empty_indx,i}")
                return empty_indx, i
        
        return None


    def play(self, grid):
        #Check rows for almost winning
        is_row_wining =  self.checkForRowWinning(grid,self.player)
        if is_row_wining:
            return is_row_wining

        # Check for col almost wining
        is_col_wining = self.checkForColWinning(grid,self.player)
        if is_col_wining:
            return is_col_wining



