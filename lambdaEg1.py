mul = lambda num1 = 5, num2 = 20, num3 = 100: num1 + num2 + num3
print(mul())

bowl = ["cherries", "orange", "apple", "melon", "figs"] 
salad = lambda x: x if x in bowl else "not in bowl"
print(salad("mango"))

inside = lambda num: num**2 if num in range(10) else "outside"
print(inside(4))

def error():
    while True:
        try:
            val = int(eval(input("Enter an integer: ")))
            
            g = lambda x: x*3 if x > 10 else "too low"
            
            if g(val) > 20:
                print("Lambda is", g(val))
                print("Input value is", val)
                break
            else:
                print("No output")
        except:
            print("Try again, please")
            continue
        finally:
            print("END CODE")
error()

g = lambda x: x**2 if x > 5 in range(10) else 0

for i in range(10):
    print(i+100, i+g(9))

critics = ["Mustafa", "Michael", "Callum", "George"]
films = ["Akira", "Blade Runner 2049", "Mr Robot", "The Ten Cokmdskm"]
opinion = []
for i in range(4):
    fave = critics[i] + "'s favourite film is " + films[i]
    opinion.append(fave)

print(opinion)

print([critics[i] + "'s favourite film is " + films[i] for i in range(4)])