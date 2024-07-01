from pathlib import Path
import mysql.connector
# from tkinter import *
# Explicit imports to satisfy Flake8

from customtkinter import CTk, CTkCanvas, CTkButton, CTkImage, CTkLabel
from PIL import Image    


window = CTk()

window.geometry("850x500")
window.configure(bg = "#2B5955")
# connection = mysql.connector.connect(host="localhost", user="root", password="123456", database="pong")
# cursor = connection.cursor()
# cursor.execute("SELECT id_user, email, Tên_người_dùng FROM USERS where id_user = %s", [id,])
# rows = cursor.fetchall()
# id = [row[0] for row in rows]
# email = [row[1] for row in rows]
# name = [row[2] for row in rows]

# Create the main window
bg_img = CTkImage(dark_image=Image.open("Game/assets/image_1.png"), size=(850, 500))
bg_lab = CTkLabel(window, image=bg_img, text="")
bg_lab.grid(row=0, column=0)

# Avatar
ava_bg = CTkImage(dark_image=Image.open("Game/assets/image_3.png"), size=(185, 185))
ava_bg_lab = CTkLabel(window, image=ava_bg, text="")
ava_bg_lab.place(x=80, y=110)

ava = CTkImage(dark_image=Image.open("Game/assets/image_4.png"), size=(120, 120))
ava_lab = CTkLabel(window, image=ava, text="", bg_color='transparent')
ava_lab.place(x=112, y=143)

# Info
info_bg = CTkImage(dark_image=Image.open("Game/assets/image_2.png"), size=(400, 185))
info_bg_lab = CTkLabel(window, image=info_bg, text="ID: " + "\t0001" + "\n\nUsername: " + "Ngoc Bao" + "\n\nEmail:" + "\tngocbao@gmail.com",
                       font=("OpenSans Regular", 20), anchor='e',
                       fg_color='#FF9388', bg_color='transparent', justify='left')
info_bg_lab.place(x=350, y=110)

# Back button
back_btn = CTkButton(window, text='Quay lại', width=120, height=30,
                     fg_color='#407777', hover_color='#FF7B81',
                     bg_color='transparent', corner_radius=10)
back_btn.place(x=10, y=20)

# History button
history_btn = CTkButton(window, text='Lịch sử đấu', width=120, height=50,
                        fg_color='#407777', hover_color='#FF7B81',
                        bg_color='transparent', corner_radius=10)
history_btn.place(x=110, y=350)

# friend button
friend_btn = CTkButton(window, text='Danh sách bạn bè', width=120, height=50,
                       fg_color='#407777', hover_color='#FF7B81',
                       bg_color='transparent', corner_radius=10)
friend_btn.place(x=470, y=350)


# connection.close()


# window = CTk()





window.resizable(False, False)
window.mainloop()

