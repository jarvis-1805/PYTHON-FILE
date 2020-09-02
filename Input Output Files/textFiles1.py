gear = ["Blade Wolf", "Raiden", "Sam"]
path = "C:/Users/HP/Desktop/PYTHON Files/FILE_{}/second.txt"
for i in range(len(gear)):
    with open(path.format(i), "w") as f3:
        f3.write(gear[i])
       # f3.write("\n" + gear[1])
        
        f3.write("\n{} is cooler than {}".format(gear[0], gear[1]))


simpsons = [["Bart in detention", "Lists at MIT"], ["Dougnuts...Mmm", "Homer: 'Nom, nom, nom!'"]]
transformers = [["HotRod opens matrix", "Optimus returns!"], ["Unicorn explodes", "Megtron jumps"]]
def File(text):
    path1 = "C:/Users/HP/Desktop/PYTHON Files/"
    
    for i in range(len(text)):
        with open(path1 + "cartoon_{}.txt".format(i), "w") as f:
            f.write(text[i][0])
            f.write("\n" + text[i][1])

File(transformers)


dc = open("skynet.txt", "w")
dc.write("""Terminator is \nhunting John connor \nand Sarah is protecting him""")
dc.close()

d = open("skynet.txt", "r+")
d.write("\n hasta la vista baby!")
end = d.readlines()
d.close()
film = "".join(end)
print("Carl" in film.replace("\n", " ").split())