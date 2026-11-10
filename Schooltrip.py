#A student can go on a school trip if they are 10 years old and have parent permission. Write a Python program that asks for the student's age and whether they have permission.
age = int(input("What is your age"))
permission = input("Do you have permision of your parents" )
if age >= 10 and permission == "YESBRO":
    print("You can go on trip")
else:
    print("You can not go on trip")