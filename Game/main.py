import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
import subprocess

# Thiết lập cửa sổ chính
app = CTk()
app.title('PONG GAME')
app.geometry('850x500')
app.configure(bg='green')
app.resizable(False, False)

def offline_mode():
    app.destroy()
    subprocess.run(['python', 'Ponggame.py'])

def pve_mode():
    app.destroy()
    subprocess.run(['python', 'PongCPU.py'])

def mode_games():
    btn_machine = CTkButton(app, text='MÁY',command=pve_mode, width=120, height=50, corner_radius=5, cursor="hand2")
    btn_machine.place(x=220, y=200)

    btn_offline = CTkButton(app, text='OFFLINE',command=offline_mode, width=120, height=50)
    btn_offline.place(x=370, y=200)

    btn_online = CTkButton(app, text='ONLINE', width=120, height=50)
    btn_online.place(x=520, y=200)

    btn_play.place_forget()
    tab_notifications.place_forget()
    tab_sound.place_forget()
    tab_personal.place_forget()
    


bg_img = CTkImage(dark_image=Image.open("bgmain.jpg"), size=(850, 500))

bg_lab = CTkLabel(app, image=bg_img, text="")
bg_lab.grid(row=0, column=0)

# Tạo nút 'Play'
btn_play = CTkButton(app, text='PLAY', command=mode_games, fg_color='purple', width=120, height=50)
btn_play.place(x=370, y=300)

# Tạo các tab ở đầu cửa sổ
tab_personal = CTkButton(app, text='Trang cá nhân', width=120, height=30)
tab_personal.place(x=10, y=20)

tab_notifications = CTkButton(app, text='Thông báo', width=120, height=30)
tab_notifications.place(x=550, y=20)

tab_sound = CTkButton(app, text='Âm thanh', width=120, height=30)
tab_sound.place(x=720, y=20)

app.mainloop()
