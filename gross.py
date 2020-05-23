groceries = ["apples", "chips", "bread", "icecream"]
prices= [2, 3, 1.2, 4.25]

for food in range(4):
	print(groceries[food], "=", prices[food])
zip_shop = (zip(groceries,prices))
for g,p in zip_shop:
    print(g, "=", p)