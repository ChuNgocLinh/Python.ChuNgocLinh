# Sinh viên: Phạm Gia Khánh - MSSV: 20230797 - Lớp: DCCNTT14.2

ten_file = 'demo_file1.txt'
noi_dung_goc = 'Thuc \n hanh \n voi \n file\n IO\n'

# 1. Tạo file và ghi nội dung
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(noi_dung_goc)

# 2. Câu a) In ra màn hình nội dung file đó trên một dòng
print("a) In trên một dòng:")
with open(ten_file, 'r', encoding='utf-8') as file:
    noi_dung = file.read()
    # Thay thế tất cả ký tự xuống dòng '\n' bằng chuỗi rỗng ''
    noi_dung_mot_dong = noi_dung.replace('\n', '')
    print(noi_dung_mot_dong)

print("\n" + "="*30 + "\n")

# 3. Câu b) In ra màn hình nội dung file đó theo từng dòng
print("b) In theo từng dòng:")
with open(ten_file, 'r', encoding='utf-8') as file:
    # Lặp qua từng dòng trong file để in
    for dong in file:
        print(dong, end="")