# Cau 04: Tim cac so trong khoang 2000 den 3200 chia het cho 7
# va khong phai la boi so cua 5
ket_qua = []
for so in range(2000, 3201):
    if so % 7 == 0 and so % 5 != 0:
        ket_qua.append(str(so))
print(",".join(ket_qua))
