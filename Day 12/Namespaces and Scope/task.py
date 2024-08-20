enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)

my_function()