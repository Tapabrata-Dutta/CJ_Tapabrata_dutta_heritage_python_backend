inventory = {}

while True:

    print("\n1.Add Product")
    print("2.Update Stock")
    print("3.Search Product")
    print("4.Low Stock Report")
    print("5.Inventory Value")
    print("6.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        product = input("Product Name: ")
        stock = int(input("Stock: "))
        price = float(input("Price: "))

        inventory[product] = [stock, price]

    elif choice == 2:
        product = input("Product Name: ")

        if product in inventory:
            inventory[product][0] = int(input("New Stock: "))
        else:
            print("Product Not Found")

    elif choice == 3:
        product = input("Product Name: ")

        if product in inventory:
            print(inventory[product])
        else:
            print("Product Not Found")

    elif choice == 4:
        print("Low Stock Products:")

        for product in inventory:
            if inventory[product][0] < 10:
                print(product)

    elif choice == 5:
        total = 0

        for product in inventory:
            total += inventory[product][0] * inventory[product][1]

        print("Total Inventory Value:", total)

    elif choice == 6:
        break