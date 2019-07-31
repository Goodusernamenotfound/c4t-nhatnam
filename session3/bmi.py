weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
bmi = weight/(height**2)
if 0<bmi<15:
    print("Chỉ số BMI của bạn là", bmi, ". Bạn rất nhẹ cân")
elif 15<=bmi<18.5:
    print("Chỉ số BMI của bạn là", bmi, ". Bạn nhẹ cân")
elif 18.5<=bmi<25:
    print("Chỉ số BMI của bạn là", bmi, ". Bạn khỏe mạnh")
else:
    print("Chỉ số BMI của bạn là", bmi, ". Bạn thừa cân")