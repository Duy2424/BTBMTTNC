danh_sach = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
dem = {}
for phan_tu in danh_sach:
    if phan_tu in dem:
        dem[phan_tu] += 1
    else:
        dem[phan_tu] = 1
print(f"Danh sach: {danh_sach}")
print(f"So lan xuat hien: {dem}")
