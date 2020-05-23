numbers = list(range(0, 110, 10))
numbers = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
second = []
x = 0
while x < len(numbers):
	t = numbers[x] *2.5
	if t % 2 == 0:
		second.append(int(t))
	x += 1
print(second)
print(x)