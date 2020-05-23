print([u for u in "universe"])
print(list("universe"))
print([x**2 for x in range(0, 11)])

pets = ["cat", "dog", "rabbit", "duck", "mouse", "piglet"]
print([pets[i] + " is hungry!!!" for i in range(len(pets))])

print([numbers**3 for numbers in range(0,11) if numbers >=8])

print([numbers**3 for numbers in range(0,11) if numbers >=3 and numbers % 2 == 1])
print([g for g in range(0, 20) if g%2==0 and g>2])