import tkinter as tk
from tkinter import scrolledtext, filedialog
import re

# ================= AI THÔNG MINH =================
def smart_ai(prompt):
    p = prompt.lower()

    # Tổng
    if any(x in p for x in ["tổng", "sum"]):
        return '''# Tính tổng từ 1 đến n
n = int(input("Nhập n: "))
print("Tổng:", sum(range(1, n+1)))'''

    # Nguyên tố
    elif any(x in p for x in ["nguyên tố", "prime"]):
        return '''# In số nguyên tố từ 1 đến n
n = int(input("Nhập n: "))
for i in range(2, n+1):
    if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
        print(i)'''

    # Fibonacci
    elif any(x in p for x in ["fibonacci", "fib"]):
        return '''# Dãy Fibonacci
n = int(input("Nhập n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b'''

    # Giai thừa
    elif any(x in p for x in ["giai thừa", "factorial"]):
        return '''# Tính giai thừa
n = int(input("Nhập n: "))
f = 1
for i in range(1, n+1):
    f *= i
print("Giai thừa:", f)'''

    # Sắp xếp
    elif any(x in p for x in ["sắp xếp", "sort"]):
        return '''# Sắp xếp danh sách
arr = list(map(int, input("Nhập dãy số: ").split()))
arr.sort()
print("Sau khi sắp xếp:", arr)'''

    # Tìm max
    elif any(x in p for x in ["lớn nhất", "max"]):
        return '''# Tìm số lớn nhất
arr = list(map(int, input("Nhập dãy số: ").split()))
print("Max:", max(arr))'''

    # Regex nhận dạng số n
    match = re.search(r'\d+', p)
    if match:
        return f"# Bạn nhập số {match.group()} - xử lý tùy bài toán"

    return "❌ Không hiểu yêu cầu!\n👉 Gợi ý: 'tổng', 'nguyên tố', 'fibonacci', 'giai thừa', 'sắp xếp'..."

# ================= CHỨC NĂNG =================
def generate_code():
    user_input = input_box.get("1.0", tk.END).strip()
    result = smart_ai(user_input)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def copy_code():
    code = output_box.get("1.0", tk.END)
    window.clipboard_clear()
    window.clipboard_append(code)

def save_file():
    code = output_box.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".py")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

# ================= UI XỊN =================
window = tk.Tk()
window.title("🔥 AI Code Generator PRO")
window.geometry("900x600")
window.configure(bg="#1e1e1e")

# Title
tk.Label(window, text="AI Code Generator", fg="white", bg="#1e1e1e",
         font=("Segoe UI", 20, "bold")).pack(pady=10)

# Input
tk.Label(window, text="Nhập yêu cầu:", fg="white", bg="#1e1e1e").pack()

input_box = scrolledtext.ScrolledText(window, height=5,
                                      bg="#2d2d2d", fg="white",
                                      insertbackground="white",
                                      font=("Consolas", 11))
input_box.pack(fill="both", padx=10, pady=5)

# Buttons
btn_frame = tk.Frame(window, bg="#1e1e1e")
btn_frame.pack()

tk.Button(btn_frame, text="🚀 Tạo Code", bg="#007acc", fg="white",
          font=("Segoe UI", 11), command=generate_code).pack(side="left", padx=5)

tk.Button(btn_frame, text="📋 Copy", bg="#28a745", fg="white",
          command=copy_code).pack(side="left", padx=5)

tk.Button(btn_frame, text="💾 Lưu file", bg="#ffc107",
          command=save_file).pack(side="left", padx=5)

# Output
tk.Label(window, text="Kết quả:", fg="white", bg="#1e1e1e").pack()

output_box = scrolledtext.ScrolledText(window, height=18,
                                       bg="#2d2d2d", fg="#00ffcc",
                                       insertbackground="white",
                                       font=("Consolas", 11))
output_box.pack(fill="both", padx=10, pady=5)

window.mainloop()