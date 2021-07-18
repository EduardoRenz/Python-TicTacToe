from collections import Counter
from tictactoe import flatten
import random
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
        # trim empty spaces on arr
        arr = [x.strip() for x in arr]
        try:
            return arr.index('')
        except ValueError:
            return None

    #Check rows for almost winning
    def checkForRowWinning(self,grid,player,spot_count=1):
        for i,val in enumerate(grid):
            n_count = self.__countPlayerOnArray(grid[i],player)
            empty_spot_count = self.__countPlayerOnArray(grid[i], ' ')
            if n_count == spot_count and empty_spot_count > 0:
                empty_indx = self.__getEmptySpot(grid[i])
                print(f"Player {player} have {n_count} places marked,  place at {i,empty_indx}")
                return i, empty_indx
        return None

    def checkForColWinning(self,grid,player,spot_count=1):
        for i,val in enumerate(grid):
            flatten_grid = flatten(grid)
            n_count = self.__countPlayerOnArray(flatten_grid[i::3], player)
            empty_spot_count = self.__countPlayerOnArray(flatten_grid[i::3], ' ')
            if n_count == spot_count and empty_spot_count > 0:
                empty_indx = self.__getEmptySpot(flatten_grid[i::3])
                print(f"Player {player} have {n_count} places marked,  place at {empty_indx,i}")
                return empty_indx, i
        return None

    def checkForDiagWinning(self,grid,player,spot_count=1):
        def getDiagValues(grid):
            flatten_grid = flatten(grid)
            indexes = list(range(0, len(flatten_grid)))
            diag_indexes = list(filter(lambda x: x % 4 == 0, indexes))
            diag_values = [flatten_grid[i] for i in diag_indexes]
            return diag_indexes,diag_values

        diag_indexes, diag_values = getDiagValues(grid)
        n_count = self.__countPlayerOnArray(diag_values,self.player)
        empty_spot_count = self.__countPlayerOnArray(diag_values, ' ')
        if n_count == spot_count and empty_spot_count > 0:
            empty_col = self.__getEmptySpot(diag_values)
            empty_row = empty_col

            for i,val in enumerate(grid):
                if i not in diag_indexes:
                    continue

                if  grid[i][empty_col] == ' ':
                    empty_row = i

            print(f"Player {player} have {n_count} places marked,  place at {empty_row,empty_col}")
            return empty_row,empty_col

    def playRandomSpot(self,grid):
        rand_row = random.randrange(0,3)
        rand_col = random.randrange(0,3)
        
        if grid[rand_row][rand_col].strip() == '':
            print(grid[rand_row][rand_col].strip())
            return rand_row, rand_col
        else:
            return self.playRandomSpot(grid)

    # check if already have a player in this row or column
    def checkForWinning(self,grid,player):
        #Check rows for almost winning
        is_row_wining =  self.checkForRowWinning(grid,player,2)
        if is_row_wining:
            print(player," is almost wining a row",is_row_wining)
            return is_row_wining

        # Check for col almost wining
        is_col_wining = self.checkForColWinning(grid,player,2)
        if is_col_wining:
            return is_col_wining

        # Check for diags winning
        is_diag_winning = self.checkForDiagWinning(grid,player,2)
        if is_diag_winning:
            print(player," is almost wining a diag",is_diag_winning)
            return is_diag_winning
        
        return None


    def play(self, grid):
        #Check if opponent is winning
        opponent_winning_spot = self.checkForWinning(grid,self.opponent)
        if opponent_winning_spot:
            print("oponent winning spot",opponent_winning_spot)
            # Find empty spot on this row
            return opponent_winning_spot

        # Check if we are winning
        player_winning_spot = self.checkForWinning(grid,self.player)
        if player_winning_spot:
            print(self.player,"is almos winning at",player_winning_spot)
            return player_winning_spot


        # If none of the above, play the spot
        empty_spot = self.playRandomSpot(grid)
        print("IA is playing a random spot",empty_spot)
        return empty_spot

