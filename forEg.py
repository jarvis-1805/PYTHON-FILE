rep = ["Joe", "Mike", "Joi", "Luv", "Deckard", "Wallace", "Rachel"]
for i in rep:
	if len(i) == 3 or len(i) == 6:
		print(i, "is a replicant")
	else:
		print(i, "is not a replicant")