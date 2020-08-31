'''
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
    1> The elements of the first array are all factors of the integer being considered
    2> The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. This program determines how many such numbers exist and those numbers as well.'''

n1 = int(input('Enter the no. of elements in array 1 : '))
n2 = int(input('Enter the no. of elements in array 2 : '))

print("\nEnter array 1 :")
L1 = list()
for a in range(n1):
    x = int(input('Enter the element : '))
    L1.append(x)
L1.sort()

print("\nEnter array 2 :")
L2 = list()
for a in range(n2):
    x = int(input('Enter the element : '))
    L2.append(x)
L2.sort()

a = L1[len(L1)-1]
b = L2[0]

N = list()
flag = False
for i in range(a, b+1):
    for j in L1:
        if i%j == 0:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        N.append(i)

BN = list()
c = 0
for i in N:
    for j in L2:
        if j%i == 0:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        BN.append(i)
        c = c+1

print('\nNo. of elements are : {}, those are {}'.format(c, BN))