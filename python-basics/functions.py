# Defining and calling a function

def my_function():
    print("Hello")
    print("Bye")

my_function()


# Function with parameter

def greet_with_name(name):
    print(f"Good morning {name}")
    print(f"How are you doing {name}?")
    print("Isn't the weather nice today?")

greet_with_name("Valentina")


# Function with multiple (positional) parameters

def greet_with(name, location):
    print(f"Good morning {name}")
    print("How are you doing?")
    print(f"Isn't the weather nice in {location} today?")

greet_with("Valentina", "London")


# Keyword arguments

def greet_with(name, location):
    print(f"Good morning {name}")
    print("How are you doing?")
    print(f"Isn't the weather nice in {location} today?")

greet_with(location="London", name="Valentina") # The right order will be kept


# Exercise 1:
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 ✖️ 4) ÷ 5 = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

import math

def paint_calc(height, width, cover):
    total_cans = math.ceil(height *  width / cover)
    print(f"You'll need {total_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Exercise 2:
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

def prime_checker(number):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


# Functions with outputs

def my_function():
    result = 3 * 2
    return result

output = my_function()


def format_name(f_name, l_name):
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

formatted_string = format_name("vAlentiNa", "mAy")
print(formatted_string)


# Multiple return values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You din't provide valid inputs."
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))


# Exercise 3:
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap()
# so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return
# False if it is not a leap year.
#
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
#
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
#
# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year
# has 29 days in February.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
           return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# Docstrings

def format_name(f_name, l_name):
    """ Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You din't provide valid inputs."
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

format_name("valentina", "mAy")

