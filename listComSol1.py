print([(i+30) for i in range(10)])

print(["The number is " + str(i) for i in range(10) if i%2 == 0])

print([d**3 for d in range(20) if d%2 == 0 and d > 10])

d2 = {"k1": [g+ 20 *g for g in range(10) if g < 5], 
"k2": [e*e for e in range(20) if e < 10]}
print(d2)

d3 = {"k3": [sum(d2["k1"]) + sum(d2["k2"])]}
print(d3)