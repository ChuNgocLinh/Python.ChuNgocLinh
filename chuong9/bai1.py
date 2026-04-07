class HocVien:
    'Lớp mô tả học viên'

    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) show info
    def show_info(self):
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)

    # c) change info (có giá trị mặc định)
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop


# d) Chương trình chính
hv1 = HocVien("Chu Ngọc Linh", "31/01/2005", "a@gmail.com", "0123456789", "HN", "IT02")

print("=== Thông tin ban đầu ===")
hv1.show_info()

# thay đổi thông tin
hv1.change_info()

print("\n=== Sau khi cập nhật ===")
hv1.show_info()