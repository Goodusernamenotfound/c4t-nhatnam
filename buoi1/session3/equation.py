import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = (b**2) - (4*a*c)
if a==0:
    print("Lỗi: a phải khác 0")
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x=(-b)/(2*a)
    print('Phương trình có 1 ngiệm là', x)
else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print("Phương trình có 2 nghiệm là", x1, "và", x2)