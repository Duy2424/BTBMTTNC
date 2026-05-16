print("nhap va ban(done de ket huc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nsau khi chuyen thanh chu in hoa")
for line in lines:
    print(line.upper())