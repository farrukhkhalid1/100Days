print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1.lower()+name2.lower()

true = combined_name.count("t")+combined_name.count("r")+combined_name.count("u")+combined_name.count("e")
love = combined_name.count("l")+combined_name.count("o")+combined_name.count("v")+combined_name.count("e")

true_love = str(true)+str(love)
true_love = int(true_love)
if  10 > true_love or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif  true_love>= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}" )
