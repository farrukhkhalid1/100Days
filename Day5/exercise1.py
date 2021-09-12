student_heights = input("Input a list of student heights ").split()
summe = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    summe += student_heights[n]

average = summe/ len(student_heights)
print(round(average))