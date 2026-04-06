
# 1. Nhập thông tin từ bàn phím
print("--- NHẬP THÔNG TIN CÁ NHÂN ---")
ten = input("Nhập tên: ")
tuoi = input("Nhập tuổi: ")
email = input("Nhập email: ")
skype = input("Nhập Skype: ")
dia_chi = input("Nhập địa chỉ: ")
noi_lam_viec = input("Nhập nơi làm việc: ")

ten_file = 'setInfo.txt'

# a) Lưu các thông tin trên vào file 'setInfo.txt'
with open(ten_file, 'w', encoding='utf-8') as file:
    # Ghi từng dòng thông tin vào file
    file.write(f"Tên: {ten}\n")
    file.write(f"Tuổi: {tuoi}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Skype: {skype}\n")
    file.write(f"Địa chỉ: {dia_chi}\n")
    file.write(f"Nơi làm việc: {noi_lam_viec}\n")

print(f"\n=> Đã lưu thành công thông tin vào file '{ten_file}'!")

# b) Đọc thông tin từ file 'setInfo.txt' và hiển thị kết quả ra màn hình
print("\n--- KẾT QUẢ ĐỌC TỪ FILE ---")
with open(ten_file, 'r', encoding='utf-8') as file:
    noi_dung = file.read()
    print(noi_dung)
