import random as rd
rd.seed(10)

numbers = rd.sample(range(10, 100), k = 10)
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(round(9.12845, 3))
print(abs(-10))
print(eval("2.5"))
print(pow(2, 3))

new_numbers = sorted(numbers)
print(new_numbers)

print([pow(x, 2) for x in new_numbers])

print([i > 40 for i in new_numbers])
print(any([i > 40 for i in new_numbers]))
print(all([i > 40 for i in new_numbers]))
print(([i > 40 for i in new_numbers][3:]))
print(all([i > 40 for i in new_numbers][3:]))
print(sum([i > 40 for i in new_numbers]))
print(sum([i < 40 for i in new_numbers]))

data = ["10", 8.12345, 100, -30, -200]
print(data)

new_data = eval(data[0]) + int(data[1]) + data[2] + abs(data[3]) + abs(data[4])
print(new_data)

clean_data = [abs(k) for k in [int(i) for i in data]]
print(clean_data)
clean_data = sorted(clean_data[2:])[3::-1]
print(clean_data)
#print(sorted(clean_data[2:]))
#print(sorted(clean_data[2:])[3::-1])

print("The top three values {0}, {1} and {2}. My favourite number is {1}".format(*clean_data))