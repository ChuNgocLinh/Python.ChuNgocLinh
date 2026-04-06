<<<<<<< HEAD
import time

nam_sinh = int(input("Nhập năm sinh: "))

x = time.localtime()
nam_hien_tai = x[0]

tuoi = nam_hien_tai - nam_sinh

=======
import time

nam_sinh = int(input("Nhập năm sinh: "))

x = time.localtime()
nam_hien_tai = x[0]

tuoi = nam_hien_tai - nam_sinh

>>>>>>> 3dbcf1bdbc4a283596cd96fdd25861eb2f6f8b50
print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")