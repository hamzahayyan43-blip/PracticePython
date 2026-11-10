#Write a Python program that uses a for loop to take the marks of 10 students. Use an if-else statement to check whether each student has passed or failed.
for i in range(1, 11):
    marks = int(input("Enter marks of student "))

    if marks >= 50:
        print("Student", i, "has Passed")
    else:
        print("Student", i, "has Failed")