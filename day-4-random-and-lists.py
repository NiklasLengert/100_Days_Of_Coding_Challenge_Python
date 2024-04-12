import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_float_one_to_five = random_float * 5
# print(random_float_one_to_five)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}.")

# print("Virtual Coin Toss")
# guess = input("Do you think the coin toss will show 'Heads' or 'Tails'?\n")
# coin_toss = random.randint(0, 1)
# if(coin_toss == 0):
#     coin_toss_result = "Heads"
#     print(f"The coin toss was {coin_toss_result}.")
#     if(guess.lower == "heads"):
#         print("You have won!")
#     else: 
#         print("You have lost.")
# if(coin_toss == 1):
#     coin_toss_result = "Tails"
#     print(f"The coin toss was {coin_toss_result}.")
#     if(guess.lower == "tails"):
#         print("You have won!")
#     else:
#         print("You have lost.")

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
# print(states_of_america[1])
# states_of_america[1] = "Pencilvania"
# print(states_of_america)
# states_of_america.append("Niki Lando")
# print(states_of_america)

# print("Who pays the bill?")
# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# random_number = random.randint(0, len(names) - 1)
# print(f"The choosen one is: {names[random_number]}.")

# print("Treasure Map")
# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
# print(f"{line1}\n{line2}\n{line3}")

# print("This is a rock paper scissors game.\n")
# player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if(player_choice == 0):
#     player_choice_string = "Rock"
#     print(f"You choose {player_choice_string}.")
# if(player_choice == 1):
#     player_choice_string = "Paper"
#     print(f"You choose {player_choice_string}.")
# if(player_choice == 2):
#     player_choice_string = "Scissors"
#     print(f"You choose {player_choice_string}.")
# computer_choice = random.randint(0, 2)
# if(computer_choice == 0):
#     print("Computer choose Rock")
#     if(player_choice == computer_choice):
#         print("TIE")
#     elif(player_choice == 1):
#         print("WIN")
#     else:
#         print("LOOSE")
# if(computer_choice == 1):
#     print("Computer choose Paper")
#     if(player_choice == computer_choice):
#         print("TIE")
#     elif(player_choice == 0):
#         print("LOOSE")
#     else:
#         print("WIN")
# if(computer_choice == 2):
#     print("Computer choose Scissors")
#     if(player_choice == computer_choice):
#         print("TIE")
#     elif(player_choice == 0):
#         print("WIN")
#     else:
#         print("LOOSE")