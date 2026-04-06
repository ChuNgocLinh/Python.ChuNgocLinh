while True:
    print("\n===== MENU =====")
    print("1. Tính tổng 2 số")
    print("2. Tính tổng danh sách số")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tìm số nguyên tố trong [a,b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm số hoàn hảo trong [a,b]")
    print("0. Thoát")

    chon = int(input("Nhập lựa chọn: "))

    if chon == 1:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Tổng =", tong_2_so(a, b))

    elif chon == 2:
        n = int(input("Nhập số lượng phần tử: "))
        ds = [] 
        for i in range(n):
            x = int(input("Nhập phần tử: "))
            ds.append(x)
        print("Tổng =", tong_danh_sach(ds))

    elif chon == 3:
        n = int(input("Nhập n: "))
        if la_so_nguyen_to(n):
            print("Đây là số nguyên tố")
        else:
            print("Không phải số nguyên tố")

    elif chon == 4:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Các số nguyên tố là:")
        tim_so_nguyen_to(a, b)

    elif chon == 5:
        n = int(input("Nhập n: "))
        if la_so_hoan_hao(n):
            print("Là số hoàn hảo")
        else:
            print("Không phải số hoàn hảo")

    elif chon == 6:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Các số hoàn hảo là:")
        tim_so_hoan_hao(a, b)

    elif chon == 0:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")