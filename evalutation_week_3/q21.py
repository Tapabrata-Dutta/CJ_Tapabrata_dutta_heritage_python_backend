password = input("Enter Password: ")

count = 0
suggestions = []

if len(password) >= 8:
    count += 1
else:
    suggestions.append("Use at least 8 characters")

has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True
        break

if has_upper:
    count += 1
else:
    suggestions.append("Add at least one uppercase letter")

has_lower = False
for ch in password:
    if ch.islower():
        has_lower = True
        break

if has_lower:
    count += 1
else:
    suggestions.append("Add at least one lowercase letter")

has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if has_digit:
    count += 1
else:
    suggestions.append("Add at least one digit")

special = "@#$%^&*()!_-+=<>?/{}[]"

has_special = False
for ch in password:
    if ch in special:
        has_special = True
        break

if has_special:
    count += 1
else:
    suggestions.append("Add at least one special character")

print("\nConditions Satisfied:", count, "/ 5")

if count <= 2:
    print("Weak Password")
elif count <= 4:
    print("Medium Password")
else:
    print("Strong Password")

if count < 5:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)