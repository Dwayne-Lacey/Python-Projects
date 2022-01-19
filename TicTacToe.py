from random import randint

class Game_Grid:
    def __init__(self):
        pass
        

#Initializa variables here
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
    print(start_game)
    print(start_game != "y")
    print(start_game != "n")