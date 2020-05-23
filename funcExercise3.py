def greet(name = "Michael"):
    print("Hello there, " + name, "!")

def repeat(n):
    for i in range(n):
        name = input("Student name: ")
        greet(name)

repeat(3)