import random 


exit_game = False
coin_guess = ""
play_again = ""
correct_guess = 0
total_guess = 0
game_type = ""
dice_guess = 0
while game_type != "coin flip" and game_type != "dice roll":
    game_type = input("Would you like to play coin flip or dice roll? ").lower()
while exit_game == False:
    if game_type == "coin flip":
        print("Welcome to our coin flipping game! Will the coin land on heads or tails?")
        while coin_guess != "heads" and coin_guess != "tails":
            coin_guess = input("Please enter either heads or tails. ").lower()
        i = random.randint(1,2)
        if i == 1:
            coin = "heads"
        elif i == 2:
            coin = "tails"
        else:
            print("Error")
            exit_game = True
            break
        print("The coin landed on:", coin)
        if coin == coin_guess:
            print("Your guess:", coin_guess + ",", "was correct!")
            correct_guess += 1
            total_guess += 1
        elif coin != coin_guess:
            print("Your guess:", coin_guess + ",", "was incorrect.")
            total_guess += 1
        else:
            print("Error")
            exit_game = True
            break
        print("You've guessed correctly", str(correct_guess) + "/" + str(total_guess), "times.")
        while play_again != "yes" and play_again != "no":
            play_again = input("Would you like to play again? ").lower()
        if play_again == "no":
            game_switch = input("Would you like to switch games? ").lower()
            if game_switch == "yes":
                game_type = "dice roll"
                coin_guess = ""
                play_again = ""
            else:
                exit_game = True
        elif play_again == "yes":
            coin_guess = ""
            play_again = ""

    # different game
    if game_type == "dice roll":
        print("Welcome to our dice rolling game! What number will the dice roll?")
        while dice_guess < 1 or dice_guess > 6:
            dice_guess = int(input("Please enter a number between 1 and 6. "))
        i = random.randint(1,6)
        print("The dice landed on:", i)
        if i == dice_guess:
            print("Your guess:", str(dice_guess) + ",", "was correct!")
            correct_guess += 1
            total_guess += 1
        elif i != dice_guess:
            print("Your guess:", str(dice_guess) + ",", "was incorrect.")
            total_guess += 1
        else:
            print("Error")
            exit_game = True
            break
        print("You've guessed correctly", str(correct_guess) + "/" + str(total_guess), "times.")
        while play_again != "yes" and play_again != "no":
            play_again = input("Would you like to play again? ").lower()
        if play_again == "no":
            game_switch = input("Would you like to switch games? ").lower()
            if game_switch == "yes":
                game_type = "coin flip"
                dice_guess = 0
                play_again = ""
            else:
                exit_game = True
        elif play_again == "yes":
            dice_guess = 0
            play_again = ""