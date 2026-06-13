# Cau 07: Chuyen cac dong nhap vao thanh chu hoa
dong_nhap = []
print("Nhap cac dong (nhap dong rong de ket thuc):")
while True:
    dong = input()
    if dong == "":
        break
    dong_nhap.append(dong)

for dong in dong_nhap:
    print(dong.upper())
