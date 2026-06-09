print("India", "USA", "UK")            # India USA UK


# Custom separator — CSV-style output
print("Alice", 25, "Engineer", sep=",") # Alice,25,Engineer


# Pipe separator — table-style
print("Name", "Age", "City", sep=" | ") # Name | Age | City


# No newline at end — print on same line
print("Loading", end="")
print("...", end="")
print(" Done!")                          # Loading... Done!


# Custom end
for i in [1,2,3]:
    print(i, end=" → ")  # 1 → 2 → 3 →

# f-Strings (Formatted String Literals) — Python 3.6+
# f-Strings are the most modern and readable way to embed variables directly inside strings. They're faster than  .format()  and far cleaner than  +  concatenation.
name  = "Riya"
score = 94.5


# Old way — ugly concatenation
print("Student: " + name + " scored " + str(score))


# .format() way — better but verbose
print("Student: {} scored {}".format(name, score))


# f-String — cleanest!
print(f"Student: {name} scored {score}")
