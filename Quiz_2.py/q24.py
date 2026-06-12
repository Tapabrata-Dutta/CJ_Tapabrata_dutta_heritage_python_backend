password = "bikram"
count=1
while(count<6):
    check = input("Enter your password: ")
    if(check != password):
        print("Password is incorrect")
        count +=1
    else: 
        print("Nice job")
        break
print("System locked")