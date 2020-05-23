num1 = [100, 2, 90, 10]; num2 = [12, 7, 90, 50]
zip_num = zip(num1, num2)

for i, j in zip_num:
	if i>j:
		print(i)
	elif i<j:
		print(j)
	else:
		print(i,j)