grades = (85, 92, 78, 95, 88)
total = 0


for grade in grades:
    total += grade
    print(f'Grade: {grade}')


print(f'Average: {total / len(grades):.1f}')
