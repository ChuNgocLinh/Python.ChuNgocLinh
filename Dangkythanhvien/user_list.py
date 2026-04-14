import sqlite3
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from list_ui import Ui_MainWindow

print("ĐANG LOAD FILE user_list.py")


class ListWindow(QMainWindow):   # ✅ đúng tên để import
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 👉 set tiêu đề bảng (tránh lỗi hiển thị)
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Họ", "Tên", "Email", "Password", "Giới tính"]
        )

        self.load_data()

        # 👉 kiểm tra tồn tại nút trước khi connect (tránh crash)
        if hasattr(self.ui, "btn_delete"):
            self.ui.btn_delete.clicked.connect(self.delete_user)

        if hasattr(self.ui, "btn_update"):
            self.ui.btn_update.clicked.connect(self.update_user)

    def load_data(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(rows))

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.ui.tableWidget.setItem(
                    row_idx, col_idx, QTableWidgetItem(str(col_data))
                )

        conn.close()

    # ❌ XÓA
    def delete_user(self):
        row = self.ui.tableWidget.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Chọn dòng cần xóa")
            return

        user_id = self.ui.tableWidget.item(row, 0).text()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "OK", "Đã xóa")
        self.load_data()

    # ✏️ SỬA
    def update_user(self):
        row = self.ui.tableWidget.currentRow()

        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Chọn dòng cần sửa")
            return

        user_id = self.ui.tableWidget.item(row, 0).text()
        ho = self.ui.tableWidget.item(row, 1).text()
        ten = self.ui.tableWidget.item(row, 2).text()
        email = self.ui.tableWidget.item(row, 3).text()
        gender = self.ui.tableWidget.item(row, 5).text()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE users
        SET ho=?, ten=?, email=?, gender=?
        WHERE id=?
        """, (ho, ten, email, gender, user_id))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "OK", "Đã cập nhật")
        self.load_data()