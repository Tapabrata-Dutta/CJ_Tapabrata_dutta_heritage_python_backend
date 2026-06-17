mobile_numbers = [9876543210, 9123456789, 9988776655, 9871234567]

search_mobile = int(input("Enter Mobile Number: "))

for i in range(len(mobile_numbers)):
    if mobile_numbers[i] == search_mobile:
        print("Mobile Number Found")
        print("Position:", i)
        break
else:
    print("Mobile Number Not Found")