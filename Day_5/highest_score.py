student_scores = input("Input a scores of students ").split()


for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# print(student_heights)

max = 0
min = 100

for score in student_scores:
    if score > max:
        max = score
    if score < min:
        min = score

print(f'The highest score in the class is: {max}')
print(f'The lowest score in the class is: {min}')