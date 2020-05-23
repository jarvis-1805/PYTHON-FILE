dividend_int=int(input("Enter an integer to divide: "))
divisor_int=int(input("Enter an integer to divide it by: "))
if divisor_int == 0:
	print("Divisor is: ", divisor_int)
	print("Can't divide by 0")
	print("Run the program again and enter a non zero no.")
if divisor_int != 0:
	print("The result of", dividend_int, "/", divisor_int, "is:", dividend_int/divisor_int)
print("THANK YOU")
