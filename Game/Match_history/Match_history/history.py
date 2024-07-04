import tkinter as tk
from tkinter import ttk
import mysql.connector

# MySQL settings
db_config = {
    'user': 'root',
    'password': '07042004',
    'host': 'localhost',
    'database': 'pong',
}

def fetch_matches(user_id):
    matches = []
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = ("SELECT ID_trận, ID_user1, ID_user2, Điểm_user1, Điểm_user2, Thời_gian "
                 "FROM matches "
                 "WHERE ID_user1 = %s OR ID_user2 = %s")
        cursor.execute(query, (user_id, user_id))
        
        for (ID_trận, ID_user1, ID_user2, Điểm_user1, Điểm_user2, Thời_gian) in cursor:
            if ID_user1 == user_id:
                opponent_id = ID_user2
                result = "Thắng" if Điểm_user1 > Điểm_user2 else "Thua" if Điểm_user1 < Điểm_user2 else "Hòa"
            else:
                opponent_id = ID_user1
                result = "Thắng" if Điểm_user2 > Điểm_user1 else "Thua" if Điểm_user2 < Điểm_user1 else "Hòa"
            matches.append((opponent_id, result, Thời_gian))
        
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return matches

def populate_tree(tree, matches):
    for match in matches:
        tree.insert("", "end", text=match[0], values=match[1:])

# Main application
root = tk.Tk()
root.title("Lịch sử đấu của trò chơi")

# Tạo nút "Quay lại" ở phía trên cùng
back_button = ttk.Button(root, text="Quay lại")
back_button.pack(side=tk.TOP, pady=10)  # Đặt nút ở phía trên cùng và thêm khoảng cách dưới nút

tree = ttk.Treeview(root, columns=("Kết quả", "Ngày"))
tree.heading("#0", text="ID đối thủ")
tree.heading("Kết quả", text="Kết quả")
tree.heading("Ngày", text="Thời gian")

# Lấy ID user hiện tại
current_user_id = 1  # Thay thế bằng ID thực của user hiện tại

# Lấy dữ liệu từ cơ sở dữ liệu và điền vào Treeview
matches = fetch_matches(current_user_id)
populate_tree(tree, matches)

tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()
