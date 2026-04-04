# Sinh viên: Phạm Gia Khánh - MSSV: 20230797 - Lớp: DCCNTT14.2

ten_file = "du_lieu.txt"
n = int(input("Nhập số dòng n cần đọc: "))

try:
    with open(ten_file, 'r', encoding='utf-8') as file:
        print(f"\n--- {n} dòng đầu tiên của file ---")
        for i in range(n):
            dong = file.readline()
            if not dong:
                break
            print(dong, end="") 
except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{ten_file}' trong thư mục!")