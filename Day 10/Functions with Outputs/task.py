def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")


print_title = format_name(first_name,last_name)
print(print_title)
