import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from register_ui import Ui_MainWindow
from user_list import ListWindow   # ✅ SỬA Ở ĐÂY


# 🔥 TẠO DATABASE
def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ho TEXT,
        ten TEXT,
        email TEXT,
        password TEXT,
        gender TEXT
    )
    """)

    conn.commit()
    conn.close()


# 🔥 LƯU USER
def insert_user(ho, ten, email, password, gender):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (ho, ten, email, password, gender)
    VALUES (?, ?, ?, ?, ?)
    """, (ho, ten, email, password, gender))

    conn.commit()
    conn.close()


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 👉 tạo DB khi chạy
        create_db()

        # 👉 nút đăng ký
        self.ui.pushButton.clicked.connect(self.register)

    def register(self):
        ho = self.ui.lineEdit.text()
        ten = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()

        # 👉 giới tính
        if self.ui.radioButton.isChecked():
            gender = "Nam"
        elif self.ui.radioButton_2.isChecked():
            gender = "Nữ"
        else:
            gender = ""

        agree = self.ui.checkBox.isChecked()

        # 👉 validate
        if not ho or not ten or not email or not password or not gender:
            QMessageBox.warning(self, "Lỗi", "Nhập đầy đủ thông tin")
            return

        if not agree:
            QMessageBox.warning(self, "Lỗi", "Bạn phải đồng ý điều khoản")
            return

        # 👉 LƯU DATABASE
        insert_user(ho, ten, email, password, gender)

        QMessageBox.information(self, "OK", "Đăng ký thành công!")

        # 🔥 CHUYỂN MÀN
        self.open_list()

    # 👉 mở màn danh sách
    def open_list(self):
        self.list_window = ListWindow()
        self.list_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())