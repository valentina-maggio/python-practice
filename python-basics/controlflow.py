# if/else statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Exercise 1:
# Write a program that works out whether if a given number is an odd or even number.

# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

# Write your code below this line

if number % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")


# Nested if/else and if/elif/else statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("please pay £5.")
    elif age <= 18:
        print("Please pay £7.")
    else:
        print("Please pay £12")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Exercise 2:
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Write your code below this line

bmi =round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Exercise 3:
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

# Write your code below this line

if year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
elif year % 4 == 0 and year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")


# Alternative solution

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


# Multiple if

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("please pay £5.")
    elif age <= 18:
        bill = 7
        print("Please pay £7.")
    else:
        bill = 12
        print("Please pay £12")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is £{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


# Exercise 4:
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

# Write your code below this line
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")


# Exercise 5:
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line

true_letters = list("true")
love_letters = list("love")

true_count = 0
love_count = 0

combined_names = name1 + name2

for letter in true_letters:
    true_count += combined_names.lower().count(letter)

for letter in love_letters:
    love_count += combined_names.lower().count(letter)

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")






