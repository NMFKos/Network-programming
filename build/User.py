
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Lập trình mạng\PongGame\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x390")
window.configure(bg = "#EAEBED")


canvas = Canvas(
    window,
    bg = "#EAEBED",
    height = 390,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=74.0,
    y=278.0,
    width=139.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=406.0,
    y=278.0,
    width=114.0,
    height=47.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=21.0,
    y=23.0,
    width=30.0,
    height=30.0
)

canvas.create_rectangle(
    263.0,
    69.0,
    663.0,
    254.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    315.0,
    117.0,
    anchor="nw",
    text="ID:",
    fill="#000000",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    315.0,
    154.0,
    anchor="nw",
    text="User name:",
    fill="#000000",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    315.0,
    192.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    447.0,
    117.0,
    anchor="nw",
    text="01",
    fill="#000000",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    445.0,
    154.0,
    anchor="nw",
    text="abc",
    fill="#000000",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    450.0,
    192.0,
    anchor="nw",
    text="abc@gmail.com",
    fill="#000000",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_rectangle(
    51.0,
    69.0,
    236.0,
    254.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    144.0,
    162.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()