#check their age again. If the age is 10 or above, print "Middle School"; otherwise, print "Primary School". If the age is below 5, print "Not old enough for school".
age = int(input("Please tell me your age ?")) 
if age >= 5:
    if age >= 10:
        print("Middle School")
    else:
        print("Primary School")
else:
    print("Not enough old to go to school")


