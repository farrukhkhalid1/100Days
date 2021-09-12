import random
import art
import words

print(art.logo)

endgame = False
word = random.choice(words.word_list)
word = list(word)
guess = []
lives = 6
already_guessed=[]

for i in range(len(word)):
    guess+="_"
print(f"{''.join(guess)}")

while not endgame:
    char = input("Give a letter\n").lower()
    if len(already_guessed) > 0 and char in word:
        print(f"you have already guessed the letter {char}")

    for i in range(len(word)):
        if char == word[i]:
            guess[i] = char
            if char not in already_guessed:
                already_guessed.append(char)

    if char not in word:
        lives-=1
        print(f"You have guessed the letter {char}. It is not in the word. You lose a life.")

    print(f"{''.join(guess)}")

    if "_" not in guess:
        endgame=True
        print("You won")
    else:
        if lives==0:
            endgame=True
            print(f"You Lose. The letter was {''.join(word)}")

    print(art.stages[lives])



