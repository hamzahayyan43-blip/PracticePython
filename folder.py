distance = int(input("enter how much distace ?"))
name = input("pleasse enter ur name ?")
if distance >=10:
     fee = 10000
elif distance >= 5:
        fee = 500
else:
    fee= 200
print(name,distance,fee)