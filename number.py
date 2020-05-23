numbers = list(range(10, 70, 10))
print(numbers)
values = [2, 5]
import itertools
from itertools import cycle as cy
val1 = [2] ; val2 = [5]

zip_val = list(zip(numbers, cy(val1), cy(val2)))
calc = []

for n, v, z in zip_val:
	s = n*v
	t = n*z
	calc.append(s)
	calc.append(t)
print(calc)
print(zip_val)