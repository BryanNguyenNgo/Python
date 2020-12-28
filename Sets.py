student_score ={
    'John': 93,
    'Tom': 78,
    'Bob': 57
}

student_score['Marcus'] = 'NA'

for i in student_score:
    if type(student_score[i]) ==int:
        if student_score[i] >= 75:
            print(i)


