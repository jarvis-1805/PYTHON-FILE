print("Human")
for i in range(2):
	k = 0
	while k < 8:
		if k % 2 == 0:
			print("Question")
		elif k > 3 and k < 7:
			print("CELL")
		elif k == 3:
			print("INTERLINKED")
		else:
			print("CELL WITHIN CELLS")
		k += 1
print("Time to finish")