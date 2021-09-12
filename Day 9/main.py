dict ={}
bidtime = False
maxbid =0


while not bidtime:
    name = input("what is your name?\n")
    bid = int(input("What is your bid?\n"))
    dict.update({name:bid})

    while True:
        answer= input("Are there more Bidder? yes/no\n").lower()

        if answer in ('yes','no'):
            break
        print("Invalid Input")

    if answer == "yes":
        continue
    elif answer == "no":
        for w in dict:
            if dict[w] > maxbid:
                maxbid = dict[w]

        for key,value in dict.items():
            if maxbid == dict[key]:
                print(f"The highest bid is {value} from {key}")
                bidtime=True


