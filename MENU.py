import random as rd
menu = ["NOOdles", "cashew with tofu", "coconut rice"]
print(rd.choice(menu))
probabilities = [0.9, 0.01, 0.01, 0.08]
students = ["Gracie", "Callum", "Blaise", "Tony"]
print(rd.choices(students, probabilities, k = 10))

print(rd.sample(range(10, 40), k = 10))