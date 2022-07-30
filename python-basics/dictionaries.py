# Dictionaries

programming_dictionary = {
    "Bug": "a program error",
    "Function": "a piece of code",
}

# Retrieve an item from the dictionary

programming_dictionary["Bug"] # Provide the Key to retrieve the Value

# Adding new items to a dictionary

programming_dictionary["Loop"] = "the action of doing something over and over again"

# Loop through a dictionary

for thing in programming_dictionary:
    print(thing) # Will return the keys



# Exercise 1:
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the
# names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values. The final version of the
# student_grades dictionary will be checked.

# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Don't change the code above

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Don't change the code below
print(student_grades)



# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]



# Exercise 2:
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Italy to the travel_log.

# add_new_country("Italy", 2, ["Rome", "Venice"])

# You've visited Italy 2 times.
# You've been to Rome and Venice.

# DO NOT modify the travel_log directly. You need to create a function that modifies it.

# Hint
# Look at the function call above to see what the name of the function should be.


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log.

def add_new_country(country, visits, cities):
    log = {
        "country": country,
        "visits": visits,
        "cities": cities,
    }
    travel_log.append(log)



# Do not change the code below
add_new_country("Italy", 2, ["Rome", "Venice"])
print(travel_log)
