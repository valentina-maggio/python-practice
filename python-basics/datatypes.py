# Print specific character of string

print("Hello"[0])

# Integers
# For big numbers where you would use ',' Python allow to add '_'

123_456_789 # Equals 123,456,789

# Type check

type() # Gives the type of data

# Type conversion

num = 123
str(num)  # From integer to string

# Operations

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3 # Exponent


# Exercise 1:
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Don't change the code below
two_digit_number = input("Type a two digit number: ")
# Don't change the code above

####################################
#Write your code below this line

digits = [int(num) for num in str(two_digit_number)]
print(sum(digits))


# Exercise 2:
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both
# weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above

#Write your code below this line
height = float(height)
weight = int(weight)
print(round(weight/(height ** 2)))


# Round numbers

print(round(2.666666, 2)) # Rounds the numbers to two decimal places

# Floor numbers

print(8 // 3) # Returns 2

# Division shortcut (manipulate value based on previous value)

result = 4 / 2
result /= 2
print(result) # Returns 1.0

# f-String
# Combines different data types into a string

score = 0
isWinning = false
print(f"your score is {score}, you are winning is {isWinning}") # Returns your score is 0, you are winning is false


# Exercise 3
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# Don't change the code below
age = input("What is your current age?")
# Don't change the code above

#Write your code below this line

years = 90 - int(age)
months = years * 12
weeks = years  * 52
days = years * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left")
