_list = ['abc', 'xyz', 'hello', 'python', 'hi']

n = int(input("Nhập n: "))

ket_qua = []

for i in _list:
    if len(i) > n:
        ket_qua.append(i)

print("Các từ có độ dài lớn hơn", n, "là:", ket_qua)