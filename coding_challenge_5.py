def divide(a, b):
try:
c = a/b
return c
except:
print("Sorry something gone wrong!")

x = int(input("Enter numerator: "))
y = int(input("Enter denominator: "))
print(divide(x, y))