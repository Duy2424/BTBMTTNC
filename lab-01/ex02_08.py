# Cau 08: Kiem tra cac so nhi phan 4 chu so co chia het cho 5 hay khong
chuoi_nhap = input("Nhap cac so nhi phan 4 chu so, cach nhau boi dau phay: ")
danh_sach = chuoi_nhap.split(",")

ket_qua = []
for so_nhi_phan in danh_sach:
    so_nhi_phan = so_nhi_phan.strip()
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        ket_qua.append(so_nhi_phan)

print(",".join(ket_qua))
