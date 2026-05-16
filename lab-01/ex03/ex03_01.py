def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("nhap ds cac so: ")
numbers = list(map(int, input_list.split(',')))
print("tong so chan:", tinh_tong_so_chan(numbers))
