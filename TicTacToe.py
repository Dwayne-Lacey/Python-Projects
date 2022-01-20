from random import randint
import string

#This class creates an instance of the Tic-Tac-Toe game 
class Game_Grid:
    def __init__(self, players, player_shape, grid_size):
        self.turn = 0
        self.players = players
        self.game_complete = ""
        self.game_grid = {}
        self.player_shape = player_shape
        self.grid_size = grid_size

    def build_grid(self):
        n = 0
        for item in range(0, self.grid_size + 1):
            if n == 0:
                self.game_grid[n] = []
            else:
                self.game_grid[string.ascii_uppercase[n-1]] = []
            for val in range(1, self.grid_size + 1):
                if n == 0:
                    self.game_grid[n].append(str(val))
                else:
                    self.game_grid[string.ascii_uppercase[n-1]].append(" ")
            n += 1
    
    def print_grid(self):
        for key, val in self.game_grid.items():
            print(key, "-", val)
        

#Initialize variables here
start_game = ""

#Code to add game title at top of terminal
print("------------------------------------------ ")
print("### #  ###  ###  ##   ###  ###  ##  ####")
print(" #  # #      #  #  # #      #  #  # #")
print(" #  # #      #  #### #      #  #  # ###")
print(" #  # #      #  #  # #      #  #  # #")
print(" #  #  ###   #  #  #  ###   #   ##  ####")
print("------------------------------------------ ")


new_game = Game_Grid(1, "X", 3)
new_game.build_grid()
new_game.print_grid()



while start_game != "y" and start_game != "n":
     start_game = input("Welcome to Tic-Tac-Toe! Would you like to start a new game? y/n ").lower()

