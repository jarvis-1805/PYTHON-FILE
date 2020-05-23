tup1=(33,49,55)
mylist=[10,20,30]
z=list(zip(tup1, mylist))
print(z)
for t, m in z:
    print(t+m)
for i in range(3):
    print(tup1[i]+mylist[i])
    
