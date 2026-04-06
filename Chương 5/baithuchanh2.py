
ten_file = "bai2_output.txt"
van_ban = input("Nhập đoạn văn bản cần ghi vào file: ")

# Mở file chế độ 'w' (write) để ghi
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(van_ban)
print(f"=> Đã ghi thành công vào file '{ten_file}'.\n")

# Mở file chế độ 'r' (read) để đọc và hiển thị
print("Nội dung của file vừa ghi là:")
with open(ten_file, 'r', encoding='utf-8') as file:
    noi_dung = file.read()
    print(noi_dung)
