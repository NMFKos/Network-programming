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
        query = ("""
            SELECT m.ID_trận, 
                   CASE 
                     WHEN m.ID_user1 = %s THEN m.ID_user2 
                     ELSE m.ID_user1 
                   END AS ID_đối_thủ,
                   CASE 
                     WHEN m.ID_user1 = %s THEN u2.Tên_người_dùng 
                     ELSE u1.Tên_người_dùng 
                   END AS Tên_đối_thủ,
                   CASE 
                     WHEN m.ID_user1 = %s THEN m.Điểm_user1 
                     ELSE m.Điểm_user2 
                   END AS Điểm_của_bạn,
                   CASE 
                     WHEN m.ID_user1 = %s THEN m.Điểm_user2 
                     ELSE m.Điểm_user1 
                   END AS Điểm_đối_thủ,
                   m.Thời_gian
            FROM matches m
            JOIN users u1 ON m.ID_user1 = u1.ID_user
            JOIN users u2 ON m.ID_user2 = u2.ID_user
            WHERE m.ID_user1 = %s OR m.ID_user2 = %s
        """)
        cursor.execute(query, (user_id, user_id, user_id, user_id, user_id, user_id))
        
        for (ID_trận, ID_đối_thủ, Tên_đối_thủ, Điểm_của_bạn, Điểm_đối_thủ, Thời_gian) in cursor:
            result = "Thắng" if Điểm_của_bạn > Điểm_đối_thủ else "Thua" if Điểm_của_bạn < Điểm_đối_thủ else "Hòa"
            matches.append((ID_đối_thủ, Tên_đối_thủ, result, Thời_gian))
        
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

tree = ttk.Treeview(root, columns=("Tên đối thủ", "Kết quả", "Ngày"))
tree.heading("#0", text="ID đối thủ")
tree.heading("Tên đối thủ", text="Tên đối thủ")
tree.heading("Kết quả", text="Kết quả")
tree.heading("Ngày", text="Thời gian")

# Lấy ID user hiện tại
current_user_id = 1  # Thay thế bằng ID thực của user hiện tại

# Lấy dữ liệu từ cơ sở dữ liệu và điền vào Treeview
matches = fetch_matches(current_user_id)
populate_tree(tree, matches)

tree.pack(expand=True, fill=tk.BOTH)

root.mainloop()
