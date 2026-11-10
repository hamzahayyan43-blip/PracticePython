#A child can buy ice cream if they have 100 rupees or more AND their parents allow them.
custmer = int(input("Do you have money ? "))
parentallow =input("Does your parents allow yoou to eat icecream ? ")
if custmer >= 100 and parentallow == "yes":
    print("Here is your icecream enjoy")
else:
    print("Sorry,but you can not eat icecream")