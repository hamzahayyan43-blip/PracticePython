#Otherwise, print "You need more money". If they have less than 100 rupees, print "You don't have enough money"
Child = int(input("Give me  Cash."))
if Child >= 100:
    if Child >= 150:
        print("You can buy toys.")
    else:
        print("You need more money.")
else:
    print("You dont have enough money.")
