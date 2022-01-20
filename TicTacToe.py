from random import randint
import string

#This class creates an instance of the Tic-Tac-Toe game 
class Game_Grid:
    def __init__(self, players, player_shape, other_shape, grid_size):
        self.turn = 0
        self.players = players
        self.game_complete = ""
        self.game_grid = {}
        self.player_shape = player_shape
        self.other_shape = other_shape
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

    def place_marker(self, row, column):
        marker_placed = False
        while marker_placed == False:
            if self.game_grid[row][column] == " ":
                self.game_grid[row][column] = self.player_shape
                marker_placed = True
                return True
            else:
                print("There is already a mark placed here, try another spot.")
                return False
    
    def computer_place_marker(self):
        pass

    def check_marker_valid(self, marker):
        if marker[0] in self.game_grid.keys() and marker[-1].isdigit():
            if int(marker[-1]) > 0 and int(marker[-1]) <= self.grid_size:
                row = marker[0]
                column = int(marker[-1]) - 1
                marker_placed = self.place_marker(row, column)
                if marker_placed == True:
                    return True
                else:
                    return False
            else:
                print("Marker is not valid, please choose a spot within the grid such as", str(string.ascii_uppercase[randint(0, self.grid_size - 1)]) + str(randint(1, self.grid_size)))
                return False
        else:
            print("Marker is not valid, please choose a spot within the grid such as", str(string.ascii_uppercase[randint(0, self.grid_size - 1)]) + str(randint(1, self.grid_size))) 
            return False         


#Initialize variables here
start_game = ""
marker_placed = False

#Code to add game title at top of terminal
print("------------------------------------------ ")
print("### #  ###  ###  ##   ###  ###  ##  ####")
print(" #  # #      #  #  # #      #  #  # #")
print(" #  # #      #  #### #      #  #  # ###")
print(" #  # #      #  #  # #      #  #  # #")
print(" #  #  ###   #  #  #  ###   #   ##  ####")
print("------------------------------------------ ")


new_game = Game_Grid(1, "X", "O", 3)
new_game.build_grid()
new_game.print_grid()

while start_game != "y" and start_game != "n":
      start_game = input("Welcome to Tic-Tac-Toe! Would you like to start a new game? y/n ").lower()

while start_game == "y":
    while marker_placed == False:
        marker = input("Where would you like to place your marker?")
        marker_placed = new_game.check_marker_valid(marker)
        new_game.print_grid()
    
    marker_placed = False