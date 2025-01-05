student_heights = input("Input a list of student heights ").split()


for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

lenght = 0
total_height = 0

for height in student_heights:
    lenght += 1
    total_height += height

print(f'Average height rounded to the nearest whole number = {round(total_height/lenght)}')