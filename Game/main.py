import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
import pygame

# Thiết lập cửa sổ chính
app = CTk()
app.title('PONG GAME')
app.geometry('850x500')
app.configure(bg='green')
app.resizable(False, False)

def offline_mode():
    pygame.mixer.music.stop()
    app.destroy()
    subprocess.run(['python', 'Ponggame.py'])
    subprocess.run(['python', 'main.py'])
    exit()

def pve_mode():
    pygame.mixer.music.stop()
    app.destroy()
    subprocess.run(['python', 'PongCPU.py'])
    subprocess.run(['python', 'main.py'])
    exit()

def return_home():
    btn_play.place(x=370, y=300)
    tab_personal.place(x=10, y=20)
    tab_notifications.place(x=550, y=20)
    tab_sound.place(x=720, y=20)

    btn_online.place_forget()
    btn_machine.place_forget()
    btn_offline.place_forget()
    return_label.place_forget()

def mode_games():
    global btn_machine
    global btn_offline
    global btn_online
    global return_label

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

    return_label = CTkButton(app, text='Trở về',command=return_home, width=120, height=30)
    return_label.place(x=10, y=20)
    
def sound():
    subprocess.run(["python3", "./Volume/Volume/Volume/volume.py"])


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

tab_sound = CTkButton(app, text='Âm thanh',command=sound, width=120, height=30)
tab_sound.place(x=720, y=20)
pygame.mixer.init()
pygame.mixer.music.load('sounds/background_music.mp3')
pygame.mixer.music.play(-1)

app.mainloop()
