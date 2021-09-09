print("Welcome to Tip Calculator")
total_amount = int(input("Give the amount of the total bill.\n$ "))
tip= int(input("What percentage tip would you like to give?\n"))
people = int(input("how many people are there?\n"))
total_amount_pP = (total_amount+(total_amount*tip/100))/people
print("Each person should pay : $ %.2f" % total_amount_pP)

