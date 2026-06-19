inventory = {}

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. View Inventory")
    print("6. Exit")

    choice = int(input("Enter Choice (in number) : "))

    if choice == 1:
        product = input("Enter Product Name: ")
        stock = int(input("Enter Stock Quantity: "))
        inventory[product] = stock
        print("Product Added")

    elif choice == 2:
        product = input("Enter Product Name: ")

        if product in inventory:
            del inventory[product]
            print("Product Removed")
        else:
            print("Product Not Found")

    elif choice == 3:
        product = input("Enter Product Name: ")

        if product in inventory:
            print("Stock =", inventory[product])
        else:
            print("Product Not Found")

    elif choice == 4:
        product = input("Enter Product Name: ")

        if product in inventory:
            stock = int(input("Enter New Stock: "))
            inventory[product] = stock
            print("Stock Updated")
        else:
            print("Product Not Found")

    elif choice == 5:
        print("\nInventory Details")
        for product, stock in inventory.items():
            print(product, ":", stock)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")