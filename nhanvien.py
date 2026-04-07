class NhanVien:
    'Lớp mô tả cho mỗi nhân viên'
    dem = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        NhanVien.dem += 1

    def hien_thi_so_luong(self):
        print("Tổng số nhân viên được tạo: %d" % NhanVien.dem)

    def hien_thi_nhan_vien(self):
        print("Tên: ", self.__name, ", Lương: ", self.__salary)

    def cap_nhat(self, name=None, salary=None):
        self.__name = name
        self.__salary = salary


nhan_vien_dev = NhanVien('Nguyen Van A', 1000)
nhan_vien_test = NhanVien('Nguyen Van B', 1200)

nhan_vien_dev.hien_thi_nhan_vien()
nhan_vien_test.hien_thi_nhan_vien()

print(nhan_vien_dev.dem)

print(nhan_vien_dev.name)   # dòng này sẽ lỗi
print(nhan_vien_test.name)