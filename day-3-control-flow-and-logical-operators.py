# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is you age?"))
#     if age <= 12:
#         print("Please pay 5 dollars.")
#     elif 12 <= age <= 18:
#         print("Please pay 7 dollars.")
#     elif age > 18:
#         print("Please pay 12 dollars.")
# else:
#     print("Sorry, you have to grow taller before you can ride the rollercoaster.")

# print("Type in any number and I will tell you if it is even or odd.")
# input_number = int(input("Enter a number: \n"))
# if input_number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# print("BMI Interpreter")
# weight = input("Please enter your weight in kg: \n")	
# height = input("Please enter your height in m: \n")	
# bmi = float(weight) / float(height) ** 2
# print(f"Your BMI is {bmi}.")
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 25:
#     print("You are normal weight.")
# elif 25 <= bmi < 30:
#     print("You are slightly overweight.")
# elif 30 <= bmi < 35:
#     print("You are obese.")
# elif bmi >= 35:
#     print("You are clinicly obese.")

# year = int(input("Enter a year: \n"))
# leap = False	
# if year % 4 == 0:
#     leap = True
#     if year % 100 == 0:
#         leap = False
#         if year % 400 == 0:
#             leap = True
#         else:
#             leap = False
#     else: 
#         leap = True
# else: 
#     leap = False

# if leap == True:
#     print("Leap year.")	
# else:	
#     print("Not a leap year.")	

        
# pizza_size = input("In which size do you want your pizza (S/M/L)?\n")
# pizza_price = 0
# if pizza_size == "S":
#     pizza_price += 15
#     print(f"Your current prize is {pizza_price} dollars.")
# if pizza_size == "M":
#     pizza_price += 20
#     print(f"Your current prize is {pizza_price} dollars.")
# if pizza_size == "L":
#     pizza_price += 25
#     print(f"Your current prize is {pizza_price} dollars.")
# choice_pepperoni = input("Do you want pepperoni (Y/N)?\n")
# if choice_pepperoni == "Y":
#     if pizza_size == "S":
#         pizza_price += 2
#         print(f"Your current prize is {pizza_price} dollars.")
#     else:
#         pizza_price += 3
#         print(f"Your current prize is {pizza_price} dollars.")
# else:
#     pizza_price += 0   
# choice_cheese = input("Do you want extra cheese (Y/N)?\n")
# if choice_cheese == "Y":
#     pizza_price += 1
#     print(f"Your current prize is {pizza_price} dollars.")

# print(f"Your total prize is: {pizza_price} dollars.")

#Lovescore
# first_name = input("Please enter the name of the first person.\n")
# second_name = input("Please enter the name of the second person.\n")
# combined_names = first_name + second_name
# lowered_combined_names = combined_names.lower()
# t = lowered_combined_names.count("t")
# r = lowered_combined_names.count("r")
# u = lowered_combined_names.count("u")	
# e = lowered_combined_names.count("e")
# first_digit = t + r + u + e
# l = lowered_combined_names.count("l")
# o = lowered_combined_names.count("o")	
# v = lowered_combined_names.count("v")
# e = lowered_combined_names.count("e")
# second_digit = l + o + v + e
# whole_digit = int(str(first_digit) + str(second_digit))
# if (whole_digit < 10) or (whole_digit > 90):
#     print(f"Your love score is {whole_digit}, you go toghether like coke and mentos.")
# elif (whole_digit > 40) and (whole_digit < 50):
#     print(f"Your love score is {whole_digit}, you are alright together.")
# else:
#     print(f"Your love score is {whole_digit}.")