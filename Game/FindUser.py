from customtkinter import CTk, CTkCanvas, CTkButton, CTkImage, CTkLabel, CTkTextbox, CTkEntry, CTkToplevel
import mysql.connector
from pathlib import Path
from PIL import Image
from Results import Result

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
config = dotenv_values(".env")
 
def go_back(window, main_app):
    window.withdraw()
    main_app.deiconify()
def Find(main_app):
    def Find_user():
        global result
        # Connect to the database
        connection = mysql.connector.connect(host=os.getenv("HOST"), user=os.getenv("USER")
                                             , password=os.getenv("PASSWORD"), database=os.getenv("DATABASE"))
        cursor = connection.cursor()
        name = Name_tb.get()
        #print(name)
        try:
            cursor.execute("SELECT * FROM users where Tên_người_dùng = '" + name + "'")
            result = cursor.fetchall()
            if result == []:
                NotFound_label = CTkLabel(window, text="User Not Found", font=("OpenSans Regular", 20))
                NotFound_label.place(x=260, y=200)
                print("No user found")
            else:
                Result(result, window)
            
        except Exception as e:
            print(e)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

# Main window
    window = CTkToplevel(main_app)
    window.geometry("650x350")
    window.configure(bg="#2B5955")
    window.resizable(False, False)
    window.title("Find User")
    main_app.withdraw()
    Name_label = CTkLabel(window, text="User Name:", font=("OpenSans Regular", 20))
    Name_label.place(x=120, y=120)

    Name_tb = CTkEntry(window, width=200, height=20, corner_radius=10, fg_color="#2B5955", font=("OpenSans Regular", 20))
    Name_tb.place(x=270, y=120)


    Find_btn = CTkButton(window, text="Find", height = 30, width = 50, command=Find_user).place(x=260, y=200)

    back_btn = CTkButton(window, text= "Quay lại", width= 120, height=30, command=lambda:go_back(window, main_app)).place(x=10, y =10)

    window.mainloop()
