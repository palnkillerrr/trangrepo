import math

so = int(input("Nhap so: "))

if so % 2 == 0:
    print("so chan")
else:
    print("so chan")


for i in range(2, round(math.sqrt(so))):
    if so % i == 0:
        print("la hop so")
        break
else:
    print("so nguyen to")