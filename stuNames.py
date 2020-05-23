students = ["nAtalie", "M", "Fa ye", "Callum", "Tara"]
names = []
for i in students:
	if len(i) > 1:
		s = i.upper().replace(" ", "")
		names.append(s)
print(tuple(names))