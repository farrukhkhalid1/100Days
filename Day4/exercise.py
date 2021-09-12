import random


heads_tails = random.randint(0,1)

answer = input("Heads or Tails\n")
if answer.lower() == "heads" and heads_tails == 1:
    print("Heads. You win")
elif answer.lower() == "tails" and heads_tails == 0:
    print("Tails. You win")
else:
    print("You lose")

