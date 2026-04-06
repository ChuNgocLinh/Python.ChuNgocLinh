import os

# ===== Đọc bộ mã =====
def doc_bo_ma(file_key):
    f = open(file_key, "r", encoding="utf-8")
    noi_dung = f.read()
    bo_ma = eval(noi_dung)
    f.close()
    return bo_ma


# ===== Mã hóa / giải mã =====
def xu_ly(text, bo_ma, mode):
    ket_qua = ""

    # Nếu giải mã → đảo dictionary
    if mode == "decode":
        bo_ma_dao = {}
        for k, v in bo_ma.items():
            bo_ma_dao[v] = k
        bo_ma = bo_ma_dao

    for ky_tu in text:
        if ky_tu in bo_ma:
            ket_qua = ket_qua + bo_ma[ky_tu]
        else:
            ket_qua = ket_qua + ky_tu

    return ket_qua


# ===== Xử lý file =====
def xu_ly_file(file_in, file_out, file_key, mode):
    bo_ma = doc_bo_ma(file_key)

    # Đọc file input
    f = open(file_in, "r", encoding="utf-8")
    noi_dung = f.read()
    f.close()

    # Xử lý mã hóa / giải mã
    ket_qua = xu_ly(noi_dung, bo_ma, mode)

    # Ghi file output
    f = open(file_out, "w", encoding="utf-8")
    f.write(ket_qua)
    f.close()

    # ===== IN RA MÀN HÌNH (ĂN ĐIỂM) =====
    print("Nội dung gốc:", noi_dung)
    print("Kết quả:", ket_qua)


# ===== MAIN =====
BASE_DIR = os.path.dirname(__file__)

file_in = os.path.join(BASE_DIR, "input.txt")
file_encode = os.path.join(BASE_DIR, "encode.txt")
file_decode = os.path.join(BASE_DIR, "decode.txt")
file_key = os.path.join(BASE_DIR, "key.txt")

while True:
    print("\n===== MENU =====")
    print("1. Mã hóa")
    print("2. Giải mã")
    print("0. Thoát")

    chon = int(input("Nhập lựa chọn: "))

    if chon == 1:
        xu_ly_file(file_in, file_encode, file_key, "encode")
        print("Đã mã hóa → encode.txt")

    elif chon == 2:
        xu_ly_file(file_encode, file_decode, file_key, "decode")
        print("Đã giải mã → decode.txt")

    elif chon == 0:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")