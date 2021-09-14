import art
import data
import random

def randomize():
    return random.choice(data.data)

def format(dictionary):
    name = dictionary["name"]
    description = dictionary["description"]
    country = dictionary["country"]
    return f"{name}, a {description}, from {country}"

score = 0
playgame = True
word1 = randomize()
while playgame :
    print(art.logo)
    word2 = randomize()
    print(f"Compare A : {format(word1)}")
    print(art.vs)
    print(f"Against B : {format(word2)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    word1_fcount = word1["follower_count"]
    word2_fcount = word2["follower_count"]

    if answer =='a':
        if word1_fcount > word2_fcount:
            score += 1
            print(f"You are right. Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            playgame = False
    elif answer == 'b':
        if word2_fcount > word1_fcount:
            score +=1
            print(f"You are right. Current score: {score}")
            word1 = word2
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            playgame = False
    else:
        print("Invalid Input")
        break