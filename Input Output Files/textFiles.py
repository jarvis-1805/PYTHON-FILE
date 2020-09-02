desk = "C:/Users/HP/Desktop/PYTHON Files/"
f = open(desk + "first.txt", "w")
f.write("This is My First file")
f.write("\nHello World!!!")
f.close()

f1 = open(desk + "first.txt", "a")
f1.write("\nGood Night!")
f1.close()

with open(desk + "first.txt", "a") as g:
    g.write("\nCoooolll!!!")

f2 = open(desk + "first.txt", "r")
print(f2.read())
f2.close()