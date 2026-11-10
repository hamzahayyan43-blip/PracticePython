for i in  range(1,11):
    age = int(input("Please enter a vlaue ? "))
    if age >= 18:
        print("RS.500 for the ticket")
    elif age >= 10:
        print("Charge RS.300")
    else:
        print("RS.150")