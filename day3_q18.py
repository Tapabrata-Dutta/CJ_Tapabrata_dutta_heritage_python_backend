# 6. Check whether a student passed

math_marks = int(input("Enter Math marks: "))
science_marks = int(input("Enter Science marks: "))

if math_marks >= 40 and science_marks >= 40:
    print("Student Passed")
else:
    print("Student Failed")