marks = []
sum = 0
for i in range(0, 3):
    mark = eval(input("Enter marks in subject {}: ".format(i+1)))
    marks.append(mark)
    sum += mark

avg = sum/3
print(int(avg))
if avg >= 80:
    print("Level 4, above agency-noramlized standards")
elif avg >=70:
    print("Level 3, at agency-noramlized standards")
elif avg >=60:
    print("Level 2, below, but approaching agency-noramlized standards")
elif avg >=50:
    print("Level 1, well below agency-noramlized standards")
elif avg >=40:
    print("Level 1-, too below agency-noramlized standards")
elif avg >=0:
    print("Remedial standards")