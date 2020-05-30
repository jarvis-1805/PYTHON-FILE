li = []
nsum = pesum = posum = 0
while True:
    l = (eval(input("Enter the integer: ")))
    if l == 0:
        break
    elif l < 0:
        nsum += l
    elif l > 0:
        if l%2 == 0:
            pesum += l
        elif l%2 != 0:
            posum += l
    elif l == 0:
        break
    li.append(l)

print(li)
print("Negative nos. sum: ", nsum)
print("Positive Even nos. sum: ", pesum)
print("Positive Odd nos. sum: ", posum)