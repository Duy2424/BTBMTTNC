# Cau 01: Tinh tong cac so chan trong mot List
danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tong = 0
for so in danh_sach:
    if so % 2 == 0:
        tong += so
print(f"Danh sach: {danh_sach}")
print(f"Tong cac so chan trong List la: {tong}")
