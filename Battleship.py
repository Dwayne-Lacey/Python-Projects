import string
import random
class Grid:
  def __init__(self,grid_height, grid_width):
    self.grid_height = grid_height
    self.grid_width = grid_width
    self.grid = {}
    self.grid_keys = []
  
  def build_grid(self):
    grid = {}
    for row in range(0, self.grid_height + 1):
      if row == 0:
        grid[row] = []
        for column in range(0, self.grid_width):
          grid[row].append(str(column + 1))
      else:
        row_letter = string.ascii_uppercase[row - 1]
        grid[row_letter] = []
        for column in range(0, self.grid_width):
          grid[row_letter].append(" ")
    self.grid = grid
    
  def print_grid(self):
    for key, value in self.grid.items():
      print(key, " - " ,value)

  def check_grid_exists(self, strike):
      if len(strike) == 2:
        if strike[1].isdigit() == True:
          if strike[0] in self.grid_keys and int(strike[1]) in list(range(1, self.grid_width + 1)):
            return True
          else:
            return False
        else:
          return False
      else:
        return False

  def __repr__(self):
    print("This class contains a {height} by {width} sized grid to play battleship".format(height = self.grid_height, width = self.grid_width))

class Battleships:
  def __init__(self, total_ships):
    self.total_ships = total_ships
    self.small_ships = []
    self.medium_ships = []
    self.large_ships = []
    self.row_chr = []
    self.all_ships = []
    self.ships_left = total_ships
  
  def ship_size_totals(self):
    #Decides how many of each ship there will be
    if self.total_ships % 2 == 1:
      large_ships = 1
      medium_ships = int((self.total_ships - 1) / 2)
      small_ships = int((self.total_ships - 1) / 2)
    else:
      large_ships = 1
      medium_ships = int((self.total_ships) / 2) - 1
      small_ships = int((self.total_ships) / 2)
    
    #Builds large ships
    for st in range(0,4):
      self.large_ships.append(" ")

    #Builds medium ships
    for ships in range(0, medium_ships):
      self.medium_ships.append([])
    for ship in self.medium_ships:
      for st in range(0,3):
        ship.append(" ")
    
    #Builds small ships
    for ships in range(0, small_ships):
      self.small_ships.append([])
    for ship in self.small_ships:
      for st in range(0,2):
        ship.append(" ")

    #Stores all ships in one list 
    self.all_ships.append(self.large_ships)
    for ship in self.medium_ships:
      self.all_ships.append(ship)
    for ship in self.small_ships:
      self.all_ships.append(ship)
    
  def place_ships(self, ships, grid):
    grid_rows = range(0, grid.grid_height)
    for row in grid_rows:
      self.row_chr.append(string.ascii_uppercase[row])
      grid.grid_keys.append(string.ascii_uppercase[row])
    for ship in self.all_ships:
      current_key = self.row_chr.pop(random.randint(1, len(self.row_chr)-1))
      if len(ship) == 4:
        st_index = random.randint(0,2)
        for x in range(st_index, st_index + 4):
          grid.grid[current_key][x] = "="
      if len(ship) == 3:
        st_index = random.randint(0,3)
        for x in range(st_index, st_index + 3):
          grid.grid[current_key][x] = "="    
      if len(ship) == 2:
        st_index = random.randint(0,4)
        for x in range(st_index, st_index + 2):
          grid.grid[current_key][x] = "="    
    
  def player_guess(self, grid, guess_grid, guess):
    guess_key = guess[0].upper()
    list_index = int(guess[1]) - 1
    if grid.grid[guess_key][list_index] == "=":
      guess_grid.grid[guess_key][list_index] = "X"
      grid.grid[guess_key][list_index] = "X"
      if (grid.grid[guess_key][0:-1]).count("=") == 0:
        self.ships_left -= 1
        print("You sunk my battleship!")
        print("There are", self.ships_left, "ships left.")
      print("{guess} Hit".format(guess = guess))
    elif guess_grid.grid[guess_key][list_index] == "X" or guess_grid.grid[guess_key][list_index] == "O":
      print("You have already attacked {guess}".format(guess = guess))
    else:
      guess_grid.grid[guess_key][list_index] = "O"
      print("{guess} Miss".format(guess = guess))
      
    guess_grid.print_grid()

  def __repr__(self):
    print("This class contains {ships} ships".format(ships = self.total_ships))

#Game flow is below
play_again = True

new_inst = Grid(10, 6)
new_inst.build_grid()

other_inst = Grid(10,6)
other_inst.build_grid()


battleship1 = Battleships(5)
battleship1.ship_size_totals()
battleship1.place_ships(battleship1.medium_ships, new_inst)

other_inst.print_grid()


print("Welcome to battleship!")
while play_again == True:
  play_again_choice = ""
  while battleship1.ships_left > 0:
    strike = input("Where would you like to strike captain? ")

    if new_inst.check_grid_exists(strike) == True:
      battleship1.player_guess(new_inst, other_inst, strike)

  while play_again_choice != "YES" and play_again_choice != "NO":
    play_again_choice = input("Would you like to play again? ").upper()
  if play_again_choice == "YES":
    play_again = True
  else:
    play_again = False

  
print("Game Over")
