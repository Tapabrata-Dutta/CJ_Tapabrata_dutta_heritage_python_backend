phonebook = {
    "Rahul": "9876543210",
    "Priya": "9123456780",
    "Amit": "9988776655"
}

name = input("Enter name: ")

if name in phonebook:
    print("Phone Number:", phonebook[name])
else:
    print("Contact not found")