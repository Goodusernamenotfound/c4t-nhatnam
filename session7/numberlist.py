numbers = [5, 1, 8, 92, -1, 30]
# number = int(input("Enter a number: "))
# if number in numbers:
#     print("Position:", numbers.index(number))
# else:
#     print("Number is not in list")

print(sum(numbers))
summ = 0 
for n in numbers:
    summ += n
    print(summ)