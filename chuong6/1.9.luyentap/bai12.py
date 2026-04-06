_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

n = int(input("Nhập độ dài n: "))

dem = 0

for i in _list:
    if len(i) >= n and i[0] == i[len(i) - 1]:
        dem = dem + 1

print("Số chuỗi thỏa điều kiện là:", dem)