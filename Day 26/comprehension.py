import random

# list comprehension
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

name = "kavya"
letters_list = [letter for letter in name]
new_range = [n * 2 for n in range(1,5)]

names = ["Alex", "Beth", "Craoline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
student_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in student_scores.items() if score > 50}
