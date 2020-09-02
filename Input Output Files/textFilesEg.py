d = open("rain.txt", "w")
d.write("Hi")
d.write("\nFood is hot"*2)
d.write("\nsunny day"*4)
d.close()

e = open("cloud.txt", "w")
e.write("Hi")
e.write("\nFood is cold"*2)
e.write("\nsunny day"*4)
e.close()

a = open("rain.txt", "r")
b = open("cloud.txt", "r")
day = a.readlines()
night = b.readlines()
for i in range(6):
    if day[i] == night[i]:
        print(True)
    else:
        print(False)

a.close()
b.close()

x, y = open("rain.txt", "r"),  open("cloud.txt", "r")
day, night = x.readlines(), y.readlines()
for i in [True if day[i] == night[i] else False for i in range(6)]:
    print(i)
x.close() ; y.close()

files = ["morning", "evening", "night"]
for i in range (len(files)):
    d = open(files[i] + ".txt", "w")
    d.write("game")
    d.close()
    text = input("add text: ")
    
    d = open(files[i] + ".txt", "a")
    d.write("\n" + text)
    d.close()


w = open("count.txt", "w")
w.write("""computer\n
python\n
udemy\n
intelligence\n
universal\n
jupyter\n
java\n
javascript""")
w.close()

with open("count.txt", "r+") as comp:
    g = "".join(comp.readlines())

g2 = g.replace("\n\n", " ").split()

print([i for i in g2 if len(i) >= 5 and len(i) <= 7])