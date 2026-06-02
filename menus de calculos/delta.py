from math import sqrt

a = float(input("digite a A: "))
b = float(input("digite a B: "))
d = float(input("digite a D: "))

delta= b* b -4* a* d

x1 = (-b- sqrt (delta))/2*a
x2 = (-b- sqrt (delta))/2*a

print("x1=",x1,"e x2=",x2)