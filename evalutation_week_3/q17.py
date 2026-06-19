books = {}

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter Choice (in number): "))

    if choice == 1:
        book = input("Enter Book Name: ")
        books[book] = "Available"
        print("Book Added Successfully")

    elif choice == 2:
        book = input("Enter Book Name: ")

        if book in books:
            if books[book] == "Available":
                books[book] = "Issued"
                print("Book Issued")
            else:
                print("Book Already Issued")
        else:
            print("Book Not Found")

    elif choice == 3:
        book = input("Enter Book Name: ")

        if book in books:
            books[book] = "Available"
            print("Book Returned")
        else:
            print("Book Not Found")

    elif choice == 4:
        book = input("Enter Book Name: ")

        if book in books:
            print("Status:", books[book])
        else:
            print("Book Not Found")

    elif choice == 5:
        print("\nBooks Available in Library")

        if len(books) == 0:
            print("No Books Available")
        else:
            for book, status in books.items():
                print(book, "-", status)

    elif choice == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")