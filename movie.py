prices = {"popcorn": 5, "soda": 2, "veggie burger": 7}
total = []

val = 0
while val < 2:
	num1 = input("Would you like popcorn with the film?")
	if num1 == "no":
		None
	elif num1 == "quit":
		print("Enjoy the film")
		break
	else:
		total.append(prices["popcorn"])
		
	num2 = input("Would you like a soda?")
	if num2 == "no":
		None
	elif num2 == "quit":
		print("Enjoy the film")
		break
	else:
		total.append(prices["soda"])
	
	num3 = input("Would you like a veggie burger?")
	if num3 == "no":
		None
	elif num3 == "quit":
		print("Enjoy the film")
		break
	else:
		total.append(prices["veggie burger"])
		
	val += 1
	print("That will be $" + str(sum(total)))
	print("Enjoy the film!!!!")
	break