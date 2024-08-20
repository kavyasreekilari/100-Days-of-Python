import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    should_accumulate = True
    n1 = float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation:")
        n2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start with a new calculation:")
        if continue_calculation == 'y':
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 10)
            calculator()


calculator()




# def perform_calculations(n1, n2, operation):
#     if operation == "+":
#         return add(n1, n2)
#     elif operation == "-":
#         return subtract(n1, n2)
#     elif operation == "*":
#         return multiply(n1, n2)
#     elif operation == "/":
#         return divide(n1, n2)
#     else:
#         return "Please enter a valid operation from the options + - * / "

# stop_calculating = False
# result = 0
#
# print(art.logo)
# n1 = int(input("What's the first number?: "))
#
# def new_calculation(n1):
#
#
# while not stop_calculating:
#
#     print("+")
#     print("-")
#     print("*")
#     print("/")
#     operation = input("Pick an operation:")
#     n2 = int(input("What's the next number?: "))
#
#     result = perform_calculations(n1, n2, operation)
#     print(result)
#
#     continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start with a new calculation:")
#     if continue_calculation == 'y':
#         n1 = result
#




