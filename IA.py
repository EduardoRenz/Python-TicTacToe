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
        
        def get_diag(grid):
            return [grid[i][i] for i in range(3)]

        def get_inverse_diag(grid):
            return [grid[i][2-i] for i in range(3)]


        diag_values = get_diag(grid)
        n_count = self.__countPlayerOnArray(diag_values, player)

        if n_count == spot_count and self.__countPlayerOnArray(diag_values, ' ') > 0:
            for i in range(3):
                player_on_row_count = self.__countPlayerOnArray(grid[i],player)
                if player_on_row_count > 0:
                    continue
                empty_spot = self.__getEmptySpot(diag_values[i])

                return i, empty_spot

        inverse_diag_values = get_inverse_diag(grid)
        n_count_inverse = self.__countPlayerOnArray(get_inverse_diag(grid), player)
        print(n_count_inverse)
        if n_count_inverse == spot_count and self.__countPlayerOnArray(inverse_diag_values, ' ') > 0:
            for i in range(3):
                player_on_row_count = self.__countPlayerOnArray(grid[i],player)
                if player_on_row_count > 0:
                    continue
                empty_spot = self.__getEmptySpot(inverse_diag_values[i])
                return i, empty_spot



        return None

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
            return is_row_wining

        # Check for col almost wining
        is_col_wining = self.checkForColWinning(grid,player,2)
        if is_col_wining:
            return is_col_wining

        # Check for diags winning
        is_diag_winning = self.checkForDiagWinning(grid,player,2)
        if is_diag_winning:
            print(player," is almost wining a diag", is_diag_winning)
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

