def squared(num):
	return num**2
	
def cubed(num):
	return num**3
	
def quad(num):
	return num**4
    
def greet():
    time=eval(input("Enter the time: "))
    
    if time >= 6 and time < 12:
        print("GOOD MORNING")
        return squared(time)
        
    elif time >= 12 and time < 10:
        print("AFTERNOON")
        return cubed(time)
        
    elif time >= 10 and time < 21:
        print("GOOD EVENING")
        return quad(time)
        
    else:
        print("GOOD NIGHT")
        return time

p=greet()
print(p)