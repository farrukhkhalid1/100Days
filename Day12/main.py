import random

def dlevel (level):

    if level == "easy":
        number_of_attempts = 10
    elif level == "hard":
        number_of_attempts = 5
    else:
        print("Invalid Input")
        exit()
    return number_of_attempts

def compare(chosen_number, guess_number):
    if guess_number == chosen_number:
        return True
    elif guess_number > chosen_number:
        return "Too High"
    else:
        return "Too Low"

print("Welcome to Number guessing game!")
print("I am thinking of a number between 1 and 100.")
difficulty = dlevel(input("Chose a difficulty. Type 'easy' or 'hard': "))

number = random.randint(1,100)
endgame= False

while not endgame:
    print(f"You have {difficulty} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    print(compare(number,guess))

    difficulty -=1

    if compare(number,guess) == True:
        print(f"You won. The number was {number}")
        endgame = True
    elif difficulty == 0:
        print("You have run out of guesses, you lose.")
        endgame = True