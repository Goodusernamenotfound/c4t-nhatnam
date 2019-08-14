name = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
population = [150300, 247100, 333300, 266800, 420900, 31800]
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
for i in range(len(population)):
    density.append(round(population[i]/area[i]))
print("Mean:", round(sum(density)/6))