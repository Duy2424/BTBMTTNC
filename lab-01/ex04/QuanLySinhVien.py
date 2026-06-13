from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self):
        ten = input("Nhap ten sinh vien: ")
        gioi_tinh = input("Nhap gioi tinh: ")
        nganh = input("Nhap chuyen nganh: ")
        diem_tb = float(input("Nhap diem trung binh (he 10): "))
        sinh_vien = SinhVien(ten, gioi_tinh, nganh, diem_tb)
        self.danh_sach_sinh_vien.append(sinh_vien)
        print("Them sinh vien thanh cong!")

    def cap_nhat_sinh_vien(self):
        sv_id = int(input("Nhap ID sinh vien can cap nhat: "))
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.id == sv_id:
                sinh_vien.ten = input("Nhap ten moi: ")
                sinh_vien.gioi_tinh = input("Nhap gioi tinh moi: ")
                sinh_vien.nganh = input("Nhap chuyen nganh moi: ")
                sinh_vien.diem_tb = float(input("Nhap diem trung binh moi: "))
                print("Cap nhat thong tin sinh vien thanh cong!")
                return
        print(f"Khong tim thay sinh vien co ID = {sv_id}")

    def xoa_sinh_vien(self):
        sv_id = int(input("Nhap ID sinh vien can xoa: "))
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.id == sv_id:
                self.danh_sach_sinh_vien.remove(sinh_vien)
                print("Xoa sinh vien thanh cong!")
                return
        print(f"Khong tim thay sinh vien co ID = {sv_id}")

    def tim_kiem_theo_ten(self):
        ten = input("Nhap ten sinh vien can tim: ")
        ket_qua = []
        for sinh_vien in self.danh_sach_sinh_vien:
            if ten.lower() in sinh_vien.ten.lower():
                ket_qua.append(sinh_vien)
        if len(ket_qua) > 0:
            print("Ket qua tim kiem:")
            for sinh_vien in ket_qua:
                sinh_vien.hien_thi()
        else:
            print(f"Khong tim thay sinh vien co ten '{ten}'")

    def sap_xep_theo_diem_tb(self):
        self.danh_sach_sinh_vien.sort(key=lambda sv: sv.diem_tb)
        print("Da sap xep danh sach sinh vien theo diem trung binh!")

    def sap_xep_theo_nganh(self):
        self.danh_sach_sinh_vien.sort(key=lambda sv: sv.nganh)
        print("Da sap xep danh sach sinh vien theo ten chuyen nganh!")

    def hien_thi_danh_sach(self):
        if len(self.danh_sach_sinh_vien) == 0:
            print("Danh sach sinh vien rong!")
        else:
            print("Danh sach sinh vien:")
            for sinh_vien in self.danh_sach_sinh_vien:
                sinh_vien.hien_thi()
