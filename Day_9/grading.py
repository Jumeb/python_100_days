student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

for key in student_scores:
    if student_scores[key] >= 91:
        student_scores[key] = 'Outstanding'
    elif student_scores[key] >= 81:
        student_scores[key] = 'Exceeds Expectations'
    elif  student_scores[key] >= 71:
        student_scores[key] = 'Acceptable'
    else: 
        student_scores[key] = 'Fail'

print(student_scores)
