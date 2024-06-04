from pathlib import Path
import mysql.connector
# from tkinter import *
# Explicit imports to satisfy Flake8
from customtkinter import CTk, CTkCanvas, CTkButton, CTkImage
from PIL import Image


def profile_info(id_user):
    connection = mysql.connector.connect(host="localhost", user="root", password="NMFK1rit0!", database="p0ng")
    cursor = connection.cursor()
    cursor.execute("SELECT id_user, email, Tên_người_dùng FROM USERS where id_user = %s", [id_user,])
    rows = cursor.fetchall()
    id = [row[0] for row in rows]
    email = [row[1] for row in rows]
    name = [row[2] for row in rows]


    connection.close()


    window = CTk()

    window.geometry("700x390")
    window.configure(bg = "#2B5955")


    canvas = CTkCanvas(
        window,
        bg = "#2B5955",
        height = 390,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = CTkImage(
        Image.open("./User/assets/frame0/image_1.png"))
    image_1 = canvas.create_image(
        350.0,
        195.0,
        image=image_image_1
    )

    button_image_1 = CTkImage(
        Image.open("./User/assets/frame0/button_1.png"))
    button_1 = CTkButton(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat",
        bg="#407777"
    )
    button_1.place(
        x=403.0,
        y=311.0,
        width=114.0,
        height=47.0
    )

    button_image_2 = CTkImage(
        Image.open("./User/assets/frame0/button_2.png"))
    button_2 = CTkButton(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat",
        bg="#2B5955"
    )
    button_2.place(
        x=76.0,
        y=293.0,
        width=139.0,
        height=65.0
    )

    image_image_2 = CTkImage(
        Image.open("./User/assets/frame0/image_2.png"))
    image_2 = canvas.create_image(
        460.0,
        156.0,
        image=image_image_2
    )

    canvas.create_text(
        332.0,
        112.0,
        anchor="nw",
        text="ID:",
        fill="#EAEBED",
        font=("OpenSans Regular", 12 * -1)
    )

    canvas.create_text(
        332.0,
        149.0,
        anchor="nw",
        text="User name:",
        fill="#EAEBED",
        font=("OpenSans Regular", 12 * -1)
    )

    canvas.create_text(
        332.0,
        187.0,
        anchor="nw",
        text="Email:",
        fill="#EAEBED",
        font=("OpenSans Regular", 12 * -1)
    )

    canvas.create_text(
        464.0,
        112.0,
        anchor="nw",
        text=id[0],
        fill="#EAEBED",
        font=("OpenSans Regular", 12 * -1)
    )

    canvas.create_text(
        462.0,
        149.0,
        anchor="nw",
        text=name[0],
        fill="#EAEBED",
        font=("OpenSans Regular", 12 * -1)
    )

    canvas.create_text(
        467.0,
        187.0,
        anchor="nw",
        text=email[0],
        fill="#EAEBED",
        font=("OpenSans Regular", 12 * -1)
    )

    image_image_3 = CTkImage(
        Image.open("./User/assets/frame0/image_3.png"))
    image_3 = canvas.create_image(
        145.0,
        156.0,
        image=image_image_3
    )

    image_image_4 = CTkImage(
        Image.open("./User/assets/frame0/image_4.png"))
    image_4 = canvas.create_image(
        146.0,
        157.0,
        image=image_image_4
    )

    button_image_3 = CTkImage(
        Image.open("./User/assets/frame0/button_3.png"))
    button_3 = CTkButton(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat",
        bg="#FF9388"
    )
    button_3.place(
        x=13.0,
        y=8.0,
        width=40.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()
