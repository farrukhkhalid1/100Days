
import random

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):

    if sum(cards) ==21 and len(cards) ==2 :
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):

    if user > 21 and computer > 21:
        return "You went over. You lose."

    if user == computer:
        return "Draw"
    elif user > 21:
       return "You went over. You lose."
    elif computer > 21:
        return "Computer went over. You won"
    elif user == 0 :
        return "You won Blackjack"
    elif computer == 0:
        return "Computer won Blackjack"
    elif user > computer:
        return "You won."
    elif computer > user:
        return "You lose."

def playgame():

    game_over = False
    user_cards = []
    computer_cards =[]

    for i in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            game_over = True
        else:
            while True:
                next_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if next_card in ('y','n'):
                    break
                print("Invalid Input")
            if next_card == 'y':
                user_cards.append(deal())
            else:
                game_over = True

    while computer_score < 17:
        computer_cards.append(deal())
        computer_score= calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

    playgame1 = False
    while not playgame1:
        while True:
            answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if answer in ('y','n'):
                break
            print("Invalid Input")
        if answer == 'y':
            playgame()
        else:
            print("Goodbye")
            playgame1= True


playgame()