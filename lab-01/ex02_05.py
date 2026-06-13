so_gio = float(input("Nhap so gio lam viec trong tuan: "))
luong_gio = float(input("Nhap muc luong theo gio: "))

if so_gio <= 44:
    tien_luong = so_gio * luong_gio
else:
    gio_lam_them = so_gio - 44
    tien_luong = 44 * luong_gio + gio_lam_them * luong_gio * 1.5

print(f"So tien thuc nhan cua nhan vien la: {tien_luong}")
