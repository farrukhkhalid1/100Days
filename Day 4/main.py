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
computer = random.randint(1,3)
player_1 = int(input("What do you want to choose? Rock = 1, Paper = 2, Scissors =3\n"))

if player_1 == 1:
    print(rock)
elif player_1 == 2:
    print(paper)
elif player_1 == 3:
    print(scissors)
print("Computer chose :")
if computer == 1:
    print(rock)
elif computer == 2:
    print(paper)
elif computer == 3:
    print(scissors)
if player_1 == computer:
    print("You draw")
elif player_1 == 1 and computer == 3:
    print("You win")
elif player_1 == 2 and computer == 1:
    print("You win")
elif player_1 == 3 and computer == 2:
    print("You win")
else:
    print("You lose")


