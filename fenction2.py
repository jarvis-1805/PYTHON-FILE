def squared(num):
	return num**2
	
def cubed(num):
	return num**3
	
def quad(num):
	return num**4
	
v = 4
print(squared(v))
print(cubed(v))
print(quad(v))
total = squared(v) + cubed(v) + quad(v)
print(total)

def greet():
	time = eval(input("Enter the time: "))
	
	if time >= 6 and time < 12:
		print("GOOD MORNING!!!")
        return time**2
	elif time >= 12 and time < 10:
		print("AFTERNOON!!!")
        return time**3
	elif time >= 10 and time < 21:
		print("GOOD EVENING!!!")
        return time**4
	else:
		print("GOOD NIGHT!!!")
        return time
greet()