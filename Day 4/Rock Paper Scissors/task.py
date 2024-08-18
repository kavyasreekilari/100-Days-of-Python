import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

options = [[0,rock], [1,paper], [2,scissors]]

print(options[your_choice][1])
print(f"Computer chose:\n {options[computer_choice][1]}")
# if your_choice == options[your_choice][0]:
if your_choice == computer_choice:
    print("Its a draw!")
elif your_choice == 0 and computer_choice == 2:
    print("You won!")
elif your_choice == 2 and computer_choice == 0:
    print("Computer won!")
elif your_choice > computer_choice:
    print("You won!")
else:
    print("Computer won.")

