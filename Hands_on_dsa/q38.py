product_codes = ["P101", "P102", "P103", "P104"]

search_code = input("Enter Product Code: ")

for i in range(len(product_codes)):
    if product_codes[i] == search_code:
        print("Product Found at Position", i)
        break
else:
    print("Product Not Found")