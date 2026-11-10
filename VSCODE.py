#Take the student's age and running time.If the student is 10 years or older, check their running time.If the time is less than 15 seconds, print "You qualified for the final".Otherwise, print "Try again next time".If the student is younger than 10, print "You are too young for this competition".
age = int(input("What is your age ?"))
Time = int(input("Give a time ?"))
if age >=10:
    if Time < 15:
        print("You are qualified for the final")
    else:
        print("Try again for next time.")
else:
    print("You are too young for the compitition.")
