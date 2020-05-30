n = 0
print("You have three chances")
while n < 3:
    try:
        num = eval(input("Enter a number: "))
        if num > 0:
            print("Absolute value of ", num, " is: ", num)
        if num == 0:
            print("Absolute value of ", num, " is: ", 0)
        if num < 0:
            print("Absolute value of ", num, " is: ", (-num))
        n += 1
    except:
        print("The entered value is not a number!!! Try again!!!")
        n += 1
        continue