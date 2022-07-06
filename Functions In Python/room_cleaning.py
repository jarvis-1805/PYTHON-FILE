def main():
    # Welcome Message
    print('-'*20)
    print('Welcome to the Happy Sweeper project cost calculator.')
    print("-"*20)
    # Information Gathering Phase User Selections Gathered and Evaluated.
    room_qty = float(input("Please enter the total number of rooms :"))
    cleantype = str(input('Please choose cleaning intensity (light or heavy) :'))

    def cleantype_choiceprog(cleantype):  # Code to determine intensity.
        cleanchoice = 10
        if cleantype == "light" or cleantype == "l":
            print('You have chosen light cleaning. This will cover sweeping and dusting and basic sanitizing.')
            cleanchoice = 10
        elif cleantype == "heavy" or cleantype == "h":
            print('You have chosen heavy cleaning. This includes light cleaning and mopping, and heavy sanitizing.')
            cleanchoice = 20
        return cleanchoice

    def cleansize_selectionprog(room_qty):  # Code to gather room size choice from customer
        roomcost = 0
        if room_qty >= 1 or room_qty <= 7:
            roomcost = 1.0  # for homes with 1 - 7 rooms total.
            return roomcost
        elif room_qty >= 8 or room_qty <= 15:
            roomcost = .8  # for homes with 8 - 15 rooms total.
            return roomcost
        elif room_qty >= 16 or room_qty <= 25:
            roomcost = .6  # for homes with 16 - 25 rooms total
            return roomcost
        elif room_qty >= 25:
            roomcost = .4  # for homes with over 25 rooms or for friends and family.
            return roomcost
        else:
            print('Please enter a value greater than 0')
            cleansize_selectionprog(room_qty)
        return roomcost

    # Formula Execution Area

    def clean_cost():
        cc = (cleantype_choiceprog(cleantype) * cleansize_selectionprog(room_qty))
        return cc

    def total_clean_cost(room_qty):
        tcc = clean_cost() * room_qty
        return tcc

# Output Phase
    print('-' * 20)
    print('It will cost :', clean_cost(), ':per room cleaned.')
    print()
    print('The total cost of cleaning this space is: ', str(total_clean_cost(room_qty)))
    print()
    print('(---Restarting Calculator---)')
    print()


main()