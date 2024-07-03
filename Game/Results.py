from pathlib import Path
import mysql.connector
from customtkinter import CTk, CTkCanvas, CTkButton, CTkImage, CTkLabel, CTkToplevel
from PIL import Image    

import os

from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values(".env")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
DATABASE = os.getenv("DATABASE")
PASSWORD = os.getenv("PASSWORD")
def go_back(window, main_app):
    window.withdraw()
    main_app.deiconify()

def add_fr(id1, id2):
    connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    cursor = connection.cursor()
    print(type(id1), type(id2))
    for i in id2:
        print(i)
    print(id1)
    try:
        cursor.execute("INSERT INTO FRIENDS (id_user1, id_user2) VALUES (%s, %s)", [id1, id2[0]])
        print("Successfully added friend")
    except:
        print("Failed to add friend")
    
def Result(rows, main_app, id1):
    
    
    id2 = [row[0] for row in rows]
    username = [row[1] for row in rows]
    email = [row[3] for row in rows]

    window = CTkToplevel(main_app)

    window.geometry("850x500")
    window.configure(bg = "#2B5955")
    main_app.withdraw()
    # Create the main window
    bg_img = CTkImage(dark_image=Image.open("./assets/image_1.png"), size=(850, 500))
    bg_lab = CTkLabel(window, image=bg_img, text="")
    bg_lab.grid(row=0, column=0)

    # Avatar
    ava_bg = CTkImage(dark_image=Image.open("./assets/image_3.png"), size=(185, 185))
    ava_bg_lab = CTkLabel(window, image=ava_bg, text="")
    ava_bg_lab.place(x=80, y=110)

    ava = CTkImage(dark_image=Image.open("./assets/image_4.png"), size=(120, 120))
    ava_lab = CTkLabel(window, image=ava, text="", bg_color='transparent')
    ava_lab.place(x=112, y=143)

    # Info
    info_bg = CTkImage(dark_image=Image.open("./assets/image_2.png"), size=(400, 185))
    info_bg_lab = CTkLabel(window, image=info_bg, text="ID: " + "\t" + str(id2[0]) + "\n\nUsername: " + str(username[0]) + "\n\nEmail:" + "\t" + str(email[0]),
                        font=("OpenSans Regular", 20), anchor='e',
                        fg_color='#FF9388', bg_color='transparent', justify='left')
    info_bg_lab.place(x=350, y=110)

    # Back button
    back_btn = CTkButton(window, text='Quay lại', command=lambda:go_back(window, main_app), width=120, height=30,
                        fg_color='#407777', hover_color='#FF7B81',
                        bg_color='transparent', corner_radius=10)
    back_btn.place(x=10, y=20)

    

    # friend button
    friend_btn = CTkButton(window, text='Thêm bạn bè', width=120, height=50,
                        fg_color='#407777', hover_color='#FF7B81',
                        bg_color='transparent', corner_radius=10, command=lambda:add_fr(id1, id2))
    friend_btn.place(x=370, y=350)

    window.resizable(False, False)
    window.mainloop()
