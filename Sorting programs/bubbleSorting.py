length = int(input('Enter the array length: '))
array = []
outer = inner = swap = 0

for i in range(0, length):
    array.append(int(input('Enter the array element: ')))

for i in range(0, length):
    print('\n---- Iteration {} of outer loop ----'.format(i+1))
    
    for j in range(0, length-i-1):
    
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
        #print('Sorted array: ', array)
    
    print('Sorted array: ', array)