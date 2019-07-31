n =int(input("Nhập tháng (số): "))
if 1<=n<=3:
    print ("Tháng này là mùa xuân")
elif 4<=n<=6:
    print ("Tháng này là mùa hè")
elif 7<=n<=9:
    print ("Tháng này là mùa thu")
elif 10<=n<=12:
    print ("Tháng này là mùa đông")
else:
    print("Invalid!")