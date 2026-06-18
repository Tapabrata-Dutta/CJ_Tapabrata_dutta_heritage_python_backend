marks = [78, 85, 92, 67, 88, 90, 32]

topper = marks[0]

for i in marks:
    if i > topper:
        topper = i

print("Topper Marks:", topper)