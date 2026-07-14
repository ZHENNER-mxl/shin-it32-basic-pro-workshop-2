name = str(input("Enter name:"))
age = int(input("Enter age :"))
heigh = float(input("Enter heigh :"))
power = int(input("Enter power :"))
money = float(input("Enter money :"))

if age > 40:
    if heigh <= 180:
        if power > 8:
            if money > 2000:
                print("You pass!")
            elif money <=2000:
                print("Find more money!")
else :
    print("You didn't pass !")               
