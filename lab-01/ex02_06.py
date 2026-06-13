x = int(input("Nhap so X: "))
y = int(input("Nhap so Y: "))

mang = []
for i in range(x):
    hang = []
    for j in range(y):
        hang.append(i * j)
    mang.append(hang)

print(mang)
