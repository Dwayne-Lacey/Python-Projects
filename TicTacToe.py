from random import randint
import string

#This class creates an instance of the Tic-Tac-Toe game 
class Game_Grid:
    def __init__(self, players, grid_size):
        self.turn = 0
        self.players = players
        self.game_complete = ""
        self.game_grid = {}
        self.player_shape_types = ["X", "O"]
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

    def place_marker(self, row, column, player_shape):
        marker_placed = False
        while marker_placed == False:
            if self.game_grid[row][column] == " ":
                self.game_grid[row][column] = player_shape
                marker_placed = True
                return True
            else:
                print("There is already a mark placed here, try another spot.")
                return False
    
    def computer_place_marker(self):
        available_spaces = []
        for key, value in self.game_grid.items():
            if key != 0:
                for val in range(0, len(value)):
                    if value[val] == " ":
                        available_spaces.append(str(key) + str(val + 1))
        return available_spaces[randint(0, len(available_spaces) - 1)]
        

    def check_marker_valid(self, marker, player_shape):
        if marker[0] in self.game_grid.keys() and marker[-1].isdigit():
            if int(marker[-1]) > 0 and int(marker[-1]) <= self.grid_size:
                row = marker[0]
                column = int(marker[-1]) - 1
                marker_placed = self.place_marker(row, column, player_shape)
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

    def coin_flip(self):
        coin_guess = ""
        while coin_guess != "HEADS" and coin_guess != "TAILS":
            coin_guess = input("Order for turns will be determined by a coin toss! Heads or tails? ").upper()
        coin_result = randint(1,2)
        if coin_result == 1:
            coin = "HEADS"
        else:
            coin = "TAILS"
        if coin_guess == coin:
            print("{} won the coin toss, they will go first.".format(player1.player_name))
            return True
        else:
            print("{} won the coin toss, they will go first.".format(player2.player_name))
            return False



class Player:
    def __init__(self, player_name, player_shape):
        self.player_name = player_name
        self.player_shape = player_shape


#Initialize variables here
start_game = ""
marker_placed = False
player_shape = ""
number_players = ""
size_grid = 0

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






#Setup players
while number_players != "1" and number_players != "2":
    number_players = input("Will there be 1 or 2 players? ")


while size_grid < 3 or size_grid > 10:
    size_grid = input("Please choose a grid size between 3 and 10 ")
    if size_grid.isdigit() == False:
        size_grid = 0
    else:
        size_grid = int(size_grid)

new_game = Game_Grid(number_players, size_grid)

if new_game.players == "1":
    player1_name = input("Please enter your name. ")
    while player_shape != new_game.player_shape_types[0] and player_shape != new_game.player_shape_types[1]:
        player_shape = input("What shape would you like to use? {} or {}? ".format(new_game.player_shape_types[0], new_game.player_shape_types[1])).upper()
    if player_shape == new_game.player_shape_types[0]:
        other_shape = new_game.player_shape_types[1]
    else:
        other_shape = new_game.player_shape_types[0]
    player1 = Player(player1_name, player_shape)
    player2 = Player("CPU", other_shape)
else:
    player1_name = input("Player 1 - Please enter your name. ")
    player2_name = input("Player 2 - Please enter your name. ")
    while player_shape != new_game.player_shape_types[0] and player_shape != new_game.player_shape_types[1]:
        player_shape = input("What shape would you like to use? {} or {}? ".format(new_game.player_shape_types[0], new_game.player_shape_types[1])).upper()
    if player_shape == new_game.player_shape_types[0]:
        other_shape = new_game.player_shape_types[1]
    else:
        other_shape = new_game.player_shape_types[0]
    player1 = Player(player1_name, player_shape)
    player2 = Player(player2_name, other_shape)    





player1_turn = new_game.coin_flip()

new_game.build_grid()
new_game.print_grid()

#Game flow    
while start_game == "y":
    

    
    if player1_turn == True:
        while marker_placed == False:
            print("It's {}'s turn.".format(player1.player_name))
            marker = input("{} where would you like to place your marker? ".format(player1.player_name))
            marker_placed = new_game.check_marker_valid(marker, player1.player_shape)
            new_game.print_grid()
        player1_turn = False
    else:
        while marker_placed == False:
            print("It's {}'s turn.".format(player2.player_name))
            if player2.player_name == "CPU":
                marker = new_game.computer_place_marker()
            else:
                marker = input("{} where would you like to place your marker? ".format(player2.player_name))
            marker_placed = new_game.check_marker_valid(marker, player2.player_shape)
            new_game.print_grid()
        player1_turn = True            
    
    marker_placed = False