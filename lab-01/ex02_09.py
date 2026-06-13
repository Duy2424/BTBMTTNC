# Cau 09: Kiem tra so nguyen to
def kiem_tra_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            return False
    return True

so = int(input("Nhap mot so: "))
if kiem_tra_nguyen_to(so):
    print(f"{so} la so nguyen to")
else:
    print(f"{so} khong phai la so nguyen to")
