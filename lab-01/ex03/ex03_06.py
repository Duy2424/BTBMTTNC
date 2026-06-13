# Cau 06: Xoa mot phan tu tu Dictionary theo key da cho
sinh_vien = {"ten": "Nguyen Van A", "tuoi": 20, "nganh": "CNTT"}
print(f"Dictionary ban dau: {sinh_vien}")
key = input("Nhap key can xoa: ")
if key in sinh_vien:
    del sinh_vien[key]
    print(f"Dictionary sau khi xoa: {sinh_vien}")
else:
    print(f"Khong tim thay key '{key}' trong Dictionary")
