def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("nhap danh sach cac so: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("sau khi dao nguoc:", list_dao_nguoc)
