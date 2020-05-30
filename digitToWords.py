def words(digit):
    for i in digit:
        num = int(i)
        if num == 1:
            print("One")
        if num == 2:
            print("Two")           
        if num == 3:
            print("Three")
        if num == 4:
            print("Four")
        if num == 5:
            print("Five")
        if num == 6:
            print("Six")
        if num == 7:
            print("Seven")
        if num == 8:
            print("Eight")
        if num == 9:
            print("Nine")
        if num == 0:
            print("Zero")
while True:
    try:
        digit = input("Enter a digit: ")
        words(digit)
        break
    except ValueError:
        print("Please enter a digit!!!")
        