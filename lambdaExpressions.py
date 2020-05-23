g = lambda x, y, z : x + y + z
print(g(10, 20, 100))

h = lambda x = 10, y = 40, z = 50 : x + y + z
print(h())

i = lambda x = 10, y = 40, z = 50 : x + y + z
print(i(200, 400, 12))

j = lambda x = 10, y = 40, z = 50 : x + y + z
print(j(200, 400))

g2 = lambda num: num %2 == 0 or num > 8
print(g2(3))

compare = lambda x, y: x if x > 10 else y
print(compare(4,2))

size = lambda x: "BIG" if x > 100 else "small"
print(size(101))

print(type(size))