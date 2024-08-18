bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) # removes decimals
print(round(bmi)) # rounds up or down
print(round(bmi, 2)) # rounds to 2 places of floating point number

print(round(3.4)) # rounds down to whole number
print(round(3.5)) # rounds up to next number


# Assignment operators
score = 0
print(score)
score += 1
print(score)
score *= 4
print(score)
score -= 2
print(score)
score /= 2
print(score)


# f-string
score = 100
height = 5.3
winning = True
print(f"My score is {score}, height is {height} and I am {winning} to win.")
