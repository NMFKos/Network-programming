from customtkinter import CTk, CTkCanvas, CTkButton, CTkImage, CTkLabel, CTkTextbox, CTkEntry
import mysql.connector
from pathlib import Path
from PIL import Image

def Find():
    global result
    # Connect to the database
    connection = mysql.connector.connect(host="localhost", user="root", password="123456", database="pong")
    cursor = connection.cursor()
    name = Name_tb.get()
    print(name)
    try:
        cursor.execute("SELECT * FROM users where Tên_người_dùng = '" + name + "'")
        result = cursor.fetchall()
        if result == []:
            NotFound_label = CTkLabel(window, text="User Not Found", font=("OpenSans Regular", 20))
            NotFound_label.place(x=260, y=200)
            print("No user found")
        else:
            Found_label = CTkLabel(window, text="User Found", font=("OpenSans Regular", 20))
            Found_label.place(x=260, y=200)
            print("User found")
        
    except Exception as e:
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# Main window
window = CTk()
window.geometry("650x350")
window.configure(bg="#2B5955")
window.resizable(False, False)
window.title("Find User")

Name_label = CTkLabel(window, text="User Name:", font=("OpenSans Regular", 20))
Name_label.place(x=120, y=40)

Name_tb = CTkEntry(window, width=200, height=20, corner_radius=10, fg_color="#2B5955", font=("OpenSans Regular", 20))
Name_tb.place(x=270, y=40)


Find_btn = CTkButton(window, text="Find", height = 30, width = 50, command=Find).place(x=260, y=100)


window.mainloop()
