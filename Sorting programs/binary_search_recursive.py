def binarySearch(arr, first, last, key):
    if(last >= first):
        mid = (first+last)//2
        if(arr[mid] == key):
        	return mid
        if(arr[mid] > key):
        	return binarySearch(arr, first, mid-1, key)
        return binarySearch(arr, mid+1, last, key)
    return -1

n = 7
arr = [1, 3, 7, 9, 11, 12, 45]
key = 3
print(binarySearch(arr, 0, n-1, key))