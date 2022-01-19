from random import randint

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
        pass
        

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


while start_game != "y" and start_game != "n":
    start_game = input("Welcome to Tic-Tac-Toe! Would you like to start a new game? y/n ").lower()
