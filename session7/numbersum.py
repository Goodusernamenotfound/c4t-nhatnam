numbers = input("Enter numbers, seperated by a space: ")
split = numbers.split(" ")
summ = 0
for n in split:
    summ = summ + int(n)
print(summ)