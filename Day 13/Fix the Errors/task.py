age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")