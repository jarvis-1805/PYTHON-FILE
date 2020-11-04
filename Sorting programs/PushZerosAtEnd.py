'''
All the zeros have been pushed towards the end of the array/list.
Another important fact is that the order of the non-zero elements
have been maintained as they appear in the input array/list.

Sample Input 1:
7
2 0 0 1 3 0 0

Sample Output 1:
2 1 3 0 0 0 0
'''

def pushZerosAtEnd(arr, n) :
    k = 0
    for i in range(0, len(arr), 1):
        if arr[i] != 0:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        i += 1
    print(arr)

n = int(input())
arr = []
for i in range(0, n, 1):
    arr.append(int(input()))
pushZerosAtEnd(arr, n)