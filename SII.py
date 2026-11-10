for i in range(1, 6):
    units = int(input("Enter electricity units for house"))
    if units <= 100:
        bill = units * 10
        print("Low Usage")
    elif units <= 300:
        bill = units * 15
        print("Medium Usage")
    else:
        bill = units * 20
        print("High Usage")