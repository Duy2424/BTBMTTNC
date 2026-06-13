class SinhVien:
    sinh_vien_id = 0  # Bien dem tu dong tang cho ma sinh vien

    def __init__(self, ten, gioi_tinh, nganh, diem_tb):
        SinhVien.sinh_vien_id += 1
        self.id = SinhVien.sinh_vien_id
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.nganh = nganh
        self.diem_tb = diem_tb

    def xep_loai_hoc_luc(self):
        if self.diem_tb >= 8:
            return "Gioi"
        elif self.diem_tb >= 6.5:
            return "Kha"
        elif self.diem_tb >= 5:
            return "Trung binh"
        else:
            return "Yeu"

    def hien_thi(self):
        print(f"ID: {self.id} | Ten: {self.ten} | Gioi tinh: {self.gioi_tinh}"
              f" | Nganh: {self.nganh} | Diem TB: {self.diem_tb}"
              f" | Hoc luc: {self.xep_loai_hoc_luc()}")
