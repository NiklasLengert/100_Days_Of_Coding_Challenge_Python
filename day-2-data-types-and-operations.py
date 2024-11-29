#Data Types

#Strings
#Subscripting => print("Hello"[0]) #H
#print("123" + "345") #123345

#Integer
#print(123 + 345) #468
#print(123_456_789) #123456789

#Float
#3.14159

#Boolean
#True
#False


# num_char = len(input("What is your name?\n"))
# new_num_char = str(num_char)
# print("Your name is " + new_num_char + " characters long.")


# print("###########################\n#########################\n######################\n#####################\n")
# print("Hello this is the number addinator!")
# number = input("Enter a two digit number: \n")
# digit1 = int(number[0])
# digit2 = int(number[1])
# sum = digit1 + digit2
# print(f"The sum of the digits is: {sum}\n")
# print("#####################\n######################\n#########################\n###########################\n")


#3+5 #8
#7-4 #3
#3*2 #6
#6/3 #2
#2**3 #8

# print("Body Mass Index Calculator")
# height = input("Please enter your height in meters: \n")
# weight = input("Please enter your weight in kg: \n")
# bmi = int(weight) / float(height) ** 2
# print(f"Your BMI is: {int(bmi)}")

# print("Life in weeks calculator")
# input_age = input("What is your current age? \n")
# years_remaining = 90 - int(input_age)
# years_in_weeks = years_remaining * 52
# print(f"You have {years_in_weeks} weeks left")

# print("Tip Calculator")
# total_bill = float(input("What was the total bill? \n"))
# tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? \n"))
# amount_of_people = float(input("How many people to split the bill? \n"))
# final_total_bill_with_tip = total_bill * (tip_percentage / 100) + total_bill
# final_tip_per_person = round(final_total_bill_with_tip / amount_of_people, 2)
# print(f"Each person should pay: ${final_tip_per_person}")