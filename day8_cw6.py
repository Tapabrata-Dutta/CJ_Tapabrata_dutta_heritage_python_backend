students  = ['Alice', 'Bob', 'Carol', 'Dave']
scores    = [88, 74, 95, 62]


for student, score in zip(students, scores):
    status = 'Pass' if score >= 70 else 'Fail'
    print(f'{student}: {score} → {status}')
