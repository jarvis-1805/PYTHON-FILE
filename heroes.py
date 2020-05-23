import random as rd
heroes = ["Batman", "Spiderman", "Ironman", "Captain America"]
villains = ["Joker", "Venom", "Thanos", "Red Skull"]
numbers = list(range(len(heroes)))
rd.shuffle(heroes) ; rd.shuffle(villains)
for i in numbers:
    print(heroes[i], "VS", villains[i])