#Take a number as input from the user. First check if the number is positive or negative. If it is positive, check whether it is even or odd.
number = int(input("Enter a number please."))
if number >0:
    if number %2 ==0:
        print("The number is positive and its even")
    else:
        print("its odd")
else:
    print("Its Negative")