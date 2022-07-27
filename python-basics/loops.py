# for loop

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)


# Exercise 1:
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality
# using what you have learnt about for loops.

# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above

# Write your code below this row

total_heights = 0
total_students = 0

for height in student_heights:
    total_heights += height
    total_students += 1

average_student_height = round(total_heights/total_students)
print(average_student_height)


# Exercise 2:
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

# Don't change the code below
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

# Write your code below this row

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")


# Range

for number in range(1, 10): # The max number in the range is excluded
    print(number)

# Loop with step

for number in range(1, 11, 3): # 3 is the incremental step
    print(number)

# Gauss numbers

total = 0
for number in range(1, 101):
    total += number
print(total)


# Exercise 3:
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even
# number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not
# every step of the calculation.
# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

even_sum = 0
for number in range (2, 101, 2):
    even_sum += number

print(even_sum)


# Exercise 4:
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz".

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)