try:
    print(10 + 90)

except:
    for i in range(3):
        print(i)

finally:
    print("END CODE")
    
def error(var):
    try:
        return 10 + var
        
    except:
        print("Type Error Found!")
        print("STRING: " + str(10) + " " + var)
    
    finally:
        print("END CODE")

print(error("hello"))

def divide(x, y):
    try:
        res = x/y
        return res
    
    except ZeroDivisionError:
        print("Division by zero is forbidden!!!")
    
    except TypeError:
        print("Can't be divided or divide by a string!!!")

    finally:
        print("Executing finaly clause!!!")

print(divide("10","hello"))

while True:
    try:
        x = int (input("Enter a valid integer: "))
        break
    
    except:
        print("Invalid input!!!")

numbers = 10, 20, 30, 40
print(numbers)
chance = 0
while chance < 3:
    try:
        num = input("Enter a integer")
        if eval(num) in numbers:
            print(num, "is in numbers")
            break
        elif num == "quit":
            break
        else:
            print("Not in numbers list")
            chance += 1
    except:
        print("Try again, please!")
        chance += 1
        continue
 #   finally:
 #       print("END CODE!")

#nested try
def friends():
    animals = "bird", "cat", "dog", "cow", "lamb", "pig"
    try:
        num = int(eval(input("Please select a friend: ")))
        try:
            if animals[num] in animals:
                print(animals[num])
        except:
            print("You did not choose a friend!")
        finally:
            print("__________")
            for pet in animals:
                print(pet)
            print("____END LOOP____")
    except:
        print("You did not enter a valid index!")
friends()