def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a/b
    else:
        print("Error. Not dividable by Zero.")
calc = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}
def calculator():
    endcalulator = False
    nr_1 = int(input("Give the first number?\n"))
    while not endcalulator:
        for key,value in calc.items():
            print(key)
        while True:
            operation = input("Pick a Operation: ")
            if operation in ('+','-','*','/'):
                break
            print("Invalid Input")
        nr_2 = int(input("What is the next number?\n"))

        function = calc[operation]
        ans=function(nr_1,nr_2)
        print(f"{nr_1} {operation} {nr_2} = {ans}")

        answer = input("If you want more calculation, press y or press n to start a new one. Press any other key to quit.")

        if 'y' in answer:
                nr_1 = ans
        elif 'n' in answer:
            endcalulator= False
            calculator()
        else:
            print("Goodbye")
            endcalulator = False
            break

calculator()



