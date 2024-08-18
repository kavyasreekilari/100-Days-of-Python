# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# greet_with_name("Jack Bauer")

def calculate_weeks_left(age):
    years_remaining = 90 - age
    num_of_weeks_left = years_remaining * 52
    print(f"You have {num_of_weeks_left} weeks left")

# calculate_weeks_left(27)

# PAUSE 2
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

greet_with("Kavya","Chicago!")

# PAUSE 3
def greet_with_keywords(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}!")

greet_with_keywords(location="Pittsburgh", name="Kavya")