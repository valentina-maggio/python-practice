import random

random_integer = random.randint(1, 10) # Generates a random integer between 1 and 10 included
print(random_integer)

# You can create a new module by creating a new file, eg my_module.py and add whatever you need

random_float = random.random() # Generates a random float between 0 and 1 excluded
print(random_float)

# Exercise 1:
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's
# only for our testing code to check your work.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random
# number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails

import random

# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Don't change the code above. It's only for testing your code.

# Write the rest of your code below this line

random_num = random.randint(0, 1)
if random_num == 0:
    print("Tails")
else:
    print("Heads")


# Lists

fruits = [item1, item2]


# Exercise 2:
# You are going to write a program that will select a random name from a list of names. The person selected will have
# to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work,
# you must enter all the names as names followed by comma then space. e.g. name, name, name
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for
# our testing code to check your work.

import random

# Don't change the code below
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above

#Write your code below this line

names_length = len(names)

random_name = random.randint(0, names_length - 1)

print(f"{names[random_name]} is going to buy the meal today!")


# Exercise 3:
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
#
# This is to try and simulate the coordinates on a real map.
# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".

# Don't change the code below
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above

#Write your code below this row

row = int(position[0]) - 1
column = int(position[1]) -1

map[column][row] = "X"

#Write your code above this row

# Don't change the code below
print(f"{row1}\n{row2}\n{row3}")
