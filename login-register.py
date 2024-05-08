import mysql.connector
import secrets
import customtkinter as ctk
import bcrypt
from tkinter import messagebox
from tkinter import *
import subprocess
import PIL
from PIL import Image, ImageTk

app = ctk.CTk()
app.title('PONG GAME')
app.geometry('850x500')
app.config(bg='#001220')

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')
font3 = ('Arial', 13, 'bold')
font4 = ('Arial', 13, 'bold', 'underline')

conn = mysql.connector.connect(host="localhost", user="root", password="NMFK1rit0!", database="p0ng")
cursor = conn.cursor()
def generate_random_two_digit_number():
        return secrets.randbelow(90) + 10
def signup():
    id_user = generate_random_two_digit_number()
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    accountname = username

    if username != '' and password != '':
          cursor.execute('SELECT Tên_đăng_nhập FROM USERS WHERE Tên_đăng_nhập= %s', (username,))
          if cursor.fetchone() is not None:
                messagebox.showerror('Thông báo', 'Tên đăng nhập đã tồn tại')
          else:
                # encoded_password = password.encode('utf-8')
                # hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                cursor.execute('INSERT INTO USERS VALUES (%s, %s, %s, %s, %s)', [id_user, username, password, email, accountname])
                conn.commit()
                messagebox.showinfo('Thông báo', 'Đăng ký thành công')
    else:
        messagebox.showerror('Thông báo', 'Vui lòng nhập đầy đủ thông tin')

def login_account():
    username = username_entry2.get()
    password = password_entry2.get()

    if username != '' and password != '':
        cursor.execute('SELECT Mật_khẩu FROM USERS WHERE Tên_đăng_nhập= %s', [username,])
        result = cursor.fetchone()
        if(result):
            if password == result[0]:
                messagebox.showinfo('Thông báo', 'Đăng nhập thành công')
                app.destroy()
                subprocess.run(["python", "main.py"])
            else:
                messagebox.showerror('Thông báo', 'Sai mật khẩu')
        else:
            messagebox.showerror('Thông báo', 'Tên đăng nhập không tồn tại')
    else:
         messagebox.showerror('Thông báo', 'Vui lòng nhập đầy đủ thông tin')

def login():
    frame1.destroy()
    global frame2 
    frame2 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=840, height=500)
    frame2.place(x=0, y=0)
    
    login_label2 = ctk.CTkLabel(frame2, font=font1, text='Đăng nhập', text_color='#fff', bg_color='#001220')
    login_label2.place(x=345, y=100)

    global username_entry2
    global password_entry2

    username_entry2 = ctk.CTkEntry(frame2, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Tên đăng nhập', placeholder_text_color='#a3a3a3', width=200, height=50)  
    username_entry2.place(x=310, y=170)

    password_entry2 = ctk.CTkEntry(frame2, font=font2, show = '*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Mật khẩu', placeholder_text_color='#a3a3a3', width=200, height=50)
    password_entry2.place(x=310, y=240)

    login_button2 = ctk.CTkButton(frame2,command=login_account, font=font2, text_color='#fff', text='Đăng nhập', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=200)
    login_button2.place(x=310, y=310)


frame1 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=840, height=500)
frame1.place(x=0, y=0)

signup_label = ctk.CTkLabel(frame1, font=font1, text='Đăng ký', text_color='#fff', bg_color='#001220')
signup_label.place(x=360, y=100)

username_entry = ctk.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Tên đăng nhập', placeholder_text_color='#a3a3a3', width=200, height=50)
username_entry.place(x=310, y=170)

password_entry = ctk.CTkEntry(frame1, font=font2, show = '*', text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Mật khẩu', placeholder_text_color='#a3a3a3', width=200, height=50)
password_entry.place(x=310, y=240)

email_entry = ctk.CTkEntry(frame1, font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3, placeholder_text='Email', placeholder_text_color='#a3a3a3', width=200, height=50)
email_entry.place(x=310, y=310)

signup_button = ctk.CTkButton(frame1,command=signup, font=font2, text_color='#fff', text='Đăng ký', fg_color='#00965d', hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5, width=200)
signup_button.place(x=310, y=380)

login_label = ctk.CTkLabel(frame1,font=font3, text='Đã có tài khoản ?', text_color='#fff', bg_color='#001220')
login_label.place(x=310,y=420)

login_button = ctk.CTkButton(frame1, command=login, font=font4, text_color='#00bf77', text='Đăng nhập', fg_color='#001220', hover_color='#001220', cursor='hand2', width=40)
login_button.place(x=435,y=420)


app.mainloop()


