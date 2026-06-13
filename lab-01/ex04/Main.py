from QuanLySinhVien import QuanLySinhVien


def hien_thi_menu():
    print("\n========== QUAN LY SINH VIEN ==========")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep danh sach sinh vien theo diem trung binh")
    print("6. Sap xep danh sach sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    print("========================================")


if __name__ == "__main__":
    quan_ly = QuanLySinhVien()
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ")
        if lua_chon == "1":
            quan_ly.them_sinh_vien()
        elif lua_chon == "2":
            quan_ly.cap_nhat_sinh_vien()
        elif lua_chon == "3":
            quan_ly.xoa_sinh_vien()
        elif lua_chon == "4":
            quan_ly.tim_kiem_theo_ten()
        elif lua_chon == "5":
            quan_ly.sap_xep_theo_diem_tb()
        elif lua_chon == "6":
            quan_ly.sap_xep_theo_nganh()
        elif lua_chon == "7":
            quan_ly.hien_thi_danh_sach()
        elif lua_chon == "0":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long nhap lai!")
