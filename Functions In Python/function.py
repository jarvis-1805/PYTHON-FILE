def square(arg1, arg2):
	return arg1 + arg2
num = square(10, 20)
print(num)

def square(arg1=20, arg2=30):
	return arg1 + arg2
val = square(100, 100)
print(val)

print(type(square))