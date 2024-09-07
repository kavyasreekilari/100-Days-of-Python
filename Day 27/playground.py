
# *args
def add(*args):
    print(type(args))   # takes args as a tuple
    print(args[1])
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,6,1,4))

# kwargs
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)