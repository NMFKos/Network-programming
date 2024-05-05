import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Lịch sử đấu của trò chơi")

# Tạo nút "Quay lại" ở phía trên cùng
back_button = ttk.Button(root, text="Quay lại")
back_button.pack(side=tk.TOP, pady=10)  # Đặt nút ở phía trên cùng và thêm khoảng cách dưới nút

tree = ttk.Treeview(root, columns=("Kết quả", "Ngày"))
tree.heading("#0", text="ID đối thủ")
tree.heading("Kết quả", text="Kết quả")
tree.heading("Ngày", text="Ngày diễn ra")

matches = [
    ("001", "Thắng", "30-4-2024"),
    ("002", "Thua", "1-5-2024"),
    ("003", "Hòa", "2-5-2024")
]
for match in matches:
    tree.insert("", "end", text=match[0], values=match[1:])

tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()
