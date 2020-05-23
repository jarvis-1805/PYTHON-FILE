def survivor(name = "Michael"):
    zomb1 = input("How many zombies are there? ")
    zombie = eval(zomb1)
    
    if zombie >= 1 and zombie < 20:
        print("{} is fighting {} zombies!!!".format(name, zombie))
        
    elif zombie >= 20 and zombie < 100:
        print("{} is shooting {} zombies!!!".format(name, zombie))
    
    elif zombie >= 100 and zombie < 200:
        print("{} is running from {} zombies!!!".format(name, zombie))
    
    else:
        print("{} is eaten by {} zombies!!!!!!!!".format(name, zombie))

survivor("Daryl")