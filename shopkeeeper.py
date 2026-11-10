shop_open = input("Is the shop open?")
money = input("Do you have money?")
if shop_open == "True":
    if money == "True":  
        print("Choose a flavour and enjoy your icecream.")
    else:
        print("Go back home.")
else:
    print("Home")