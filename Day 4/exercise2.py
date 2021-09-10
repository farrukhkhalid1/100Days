row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal =int(position[0]) #2
vertical = int(position[1]) #3

row = map[vertical-1] #row3
row[horizontal-1] = "X" #Element 2

print(f"{row1}\n{row2}\n{row3}")