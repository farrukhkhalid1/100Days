alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text,shift):
    text = list(text)
    for i in range(len(text)):
        text[i] = ord(text[i])
        if text[i] >=97 and text[i] <= 122:
            text[i] = text[i]+shift
            if text[i] > 122:
                text[i] = text[i]-26
        text[i] = chr(text[i])

    text = ''.join(text)
    print(text)

def decode(text,shift):
    text = list(text)
    for i in range(len(text)):
        text[i] = ord(text[i])
        if text[i] >=97 and text[i] <= 122:
            text[i] = text[i]-shift
            if text[i] < 97:
                text[i] = text[i]+26
        text[i] = chr(text[i])

    text = ''.join(text)
    print(text)

while True:
    while True:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction in ('encode','decode'):
            break
        print("Invalid Input")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encode(text,shift)
    elif direction == "decode":
        decode(text,shift)
    else:
        print("Please write encode or decode")

    while True:
        answer = input("Do you want to restart the program? Write yes or no\n")
        if answer in ('yes','no'):
            break
        print("invalid Input")

    if answer=="yes":
        continue
    elif answer=="no":
        print("goodbye")
        break

