# numbers = [12, 21, 34, 95, 77, 64"]
# print("Current list:", numbers)
# output = []
# for num in numbers:    
#     if num % 2 == 0:  
#         output.append(num) 
# print("Even numbers in list: for num in list:", output)

numbers = input("Enter numbers, seperated by a comma: ")
split = numbers.split(",")
output = []
for num in split:    
    if int(num) % 2 == 0:  
        output.append(num) 
print("Even numbers in list:", output)
