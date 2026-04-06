
ten_file = 'demo_file2.txt'
noi_dung_mau = 'Dem so luong tu xuat hien abc abc abc 12 12 it it dnu eaut'
with open(ten_file, 'w', encoding='utf-8') as file:
    file.write(noi_dung_mau)
dict_dem_tu = {} # Tạo một Dictionary rỗng để lưu kết quả đếm

with open(ten_file, 'r', encoding='utf-8') as file:
    noi_dung = file.read()
    
    danh_sach_tu = noi_dung.split()
    
    # Duyệt qua từng từ trong danh sách
    for tu in danh_sach_tu:
        if tu in dict_dem_tu:
            dict_dem_tu[tu] += 1
        else:
            dict_dem_tu[tu] = 1  

print("Kết quả trả về:")
print(dict_dem_tu)
