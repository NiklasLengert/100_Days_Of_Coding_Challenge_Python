# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# student_heights = [156, 178, 165, 171, 187, 199]
# height_sum = 0
# for height in student_heights:
#     height_sum = height_sum + height
# height_avg = round(height_sum / len(student_heights), 2)
# print(f"The average height of the provided students is: {height_avg}cm.")

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 120]
# current_highest = 0
# current_score = 0
# for scores in student_scores:
#     current_score = scores
#     if(current_score > current_highest):
#         current_highest = current_score
# print(f"The highest score is {current_highest}.")

# total = 0
# for number in range(1, 101):
#     total += number
# print(f"{total}")

# range_indicator = int(input("Adding all the even numbers from 1 to X.\nPlease enter a number for X.\n"))
# total = 0
# for num in range(2, range_indicator + 1, 2):
#     total += num
# print(total)

# for num in range(1, 101):
#     if(num % 3 == 0 and num % 5 == 0):
#         print("FizzBuzz")
#     elif(num % 3 == 0 and num % 5 != 0):
#         print("Fizz")
#     elif(num % 3 != 0 and num % 5 == 0):
#         print("Buzz")
#     else:
#         print(num)

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_letters_counter = nr_letters
# nr_numbers = int(input("How many numbers would you like?\n"))
# nr_numbers_counter = nr_numbers
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_symbols_counter = nr_symbols
# password_length = nr_letters + nr_numbers + nr_symbols
# password = ""
# for character in range(1, password_length + 1):
#     #Random Number Manipulation
#     if(nr_letters_counter != 0 and nr_numbers_counter != 0 and nr_symbols_counter != 0):
#         random_decider_for_let_num_sym = random.randint(1, 3)
#     if(nr_letters_counter == 0 and nr_numbers_counter != 0 and nr_symbols_counter != 0):
#         random_decider_for_let_num_sym = random.randint(2, 3)
#     if(nr_letters_counter != 0 and nr_numbers_counter != 0 and nr_symbols_counter == 0):
#         random_decider_for_let_num_sym = random.randint(1, 2)
#     if(nr_letters_counter != 0 and nr_numbers_counter == 0 and nr_symbols_counter != 0):
#         random_decider_for_let_num_sym = random.randint(1, 2)
#         if(random_decider_for_let_num_sym == 1):
#             random_decider_for_let_num_sym = 1
#         else:
#             random_decider_for_let_num_sym = 3
#     #Last Character
#     if((nr_letters_counter == 0 and nr_numbers_counter == 0 and nr_symbols_counter != 0) or (nr_letters_counter == 0 and nr_numbers_counter != 0 and nr_symbols_counter == 0) or (nr_letters_counter != 0 and nr_numbers_counter == 0 and nr_symbols_counter == 0)):
#         if(nr_letters_counter != 0):
#             random_decider_for_let_num_sym = 1
#         elif(nr_numbers_counter != 0):
#             random_decider_for_let_num_sym = 2
#         else:
#             random_decider_for_let_num_sym = 3
#     #Choice of Character
#     if(random_decider_for_let_num_sym == 1 and nr_letters_counter != 0):
#         random_num_lett = random.randint(0, len(letters) - 1)
#         password += letters[random_num_lett]
#         nr_letters_counter -= 1
#     elif(random_decider_for_let_num_sym == 2 and nr_numbers_counter != 0):
#         random_num_num = random.randint(0, len(numbers) - 1)
#         password += numbers[random_num_num]
#         nr_numbers_counter -= 1
#     elif(random_decider_for_let_num_sym == 3 and nr_symbols_counter != 0):
#         random_num_sym = random.randint(0, len(symbols) - 1)
#         password += symbols[random_num_sym]
#         nr_symbols_counter -= 1
# print(password)

#EZ Solution
# for num_lett in range(0, nr_letters):
#     random_num_lett = random.randint(0, len(letters) - 1)
#     password += letters[random_num_lett]
# for num_num in range(0, nr_numbers):
#     random_num_num = random.randint(0, len(numbers) - 1)
#     password += numbers[random_num_num]
# for num_sym in range(0, nr_symbols):
#     random_num_sym = random.randint(0, len(symbols) - 1)
#     password += symbols[random_num_sym]
# print(password)

#Hard Solution

