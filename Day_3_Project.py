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



import random

list = [rock, paper, scissors]
computer = random.randint(0, 2)
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user >= 0 and user <= 2:
    print(list[user])
    print(f"The computer chose {list[computer]}")

if user >= 3:
    print("You typed an invalid number")
elif computer == 0 and user == 2:
    print("You lose!")
elif user == 0 and computer == 2 or user > computer:
    print("You Win!")
elif user == computer:
    print("It's a draw!")
else:
    print("You lose!")
