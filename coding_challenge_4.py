def bmi_calc(a, b):
    bmi = a/b
    return bmi


a = float(input("Enter weight in kg: "))
b = float(input("Enter height in metres: "))
print(bmi_calc(a, b))