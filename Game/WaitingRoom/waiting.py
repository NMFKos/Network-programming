import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import socket
import threading
from PIL import ImageDraw

class ClientApp:
    def __init__(self, master):
        self.master = master
        master.title("Phòng Chờ")
        
       

        # Cập nhật đường dẫn của avatar
        self.avatar_image = Image.open(r"background.jpg")
        self.avatar_image = self.avatar_image.resize((200, 200))  # Resize the image to 200x200 pixels
        self.avatar_image = self.avatar_image.convert("RGBA")  # Convert the image to RGBA format
        self.avatar_image = self.make_circle(self.avatar_image)  # Make the image circular
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)
        self.avatar_label = tk.Label(master, image=self.avatar_photo)
        self.avatar_label.pack()


        self.chat_frame = tk.Frame(master)
        self.chat_log = scrolledtext.ScrolledText(self.chat_frame, height=10, state='disabled')
        self.chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.message_entry = tk.Entry(self.chat_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.send_button = tk.Button(self.chat_frame, text="Gửi", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.status_label = tk.Label(master, text="Chưa sẵn sàng")
        self.status_label.pack()

        self.ready_button = tk.Button(master, text="Sẵn sàng", command=self.send_ready, background="green", foreground="black")
        self.ready_button.pack()

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 12345
        self.client_socket.connect((self.host, self.port))

        # self.chat_log.tag_config('right', justify='right')
        # self.chat_log.tag_config('left', justify='left')

        # bg_image = Image.open("background.jpg")
        # self.bg_photoimage = ImageTk.PhotoImage(bg_image)

        # self.canvas = tk.Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight())
        # self.canvas.pack(fill="both", expand=True)

        # self.canvas.create_image(0, 0, image=self.bg_photoimage, anchor="nw")

        threading.Thread(target=self.receive_message, daemon=True).start()

    # def display_message(self, message, sender):
    #     self.chat_log.config(state='normal')
    #     if sender == 'self':
    #         self.chat_log.insert(tk.END, message + '\n', 'right')
    #     else:
    #         self.chat_log.insert(tk.END, message + '\n', 'left')
    #     self.chat_log.config(state='disabled')



    

    def send_ready(self):
        self.client_socket.sendall("READY".encode())
        self.ready_button.config(state=tk.DISABLED)
        
    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client_socket.sendall(message.encode())
            self.message_entry.delete(0, tk.END)
    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if message == "START":
                self.status_label.config(text="Bắt đầu trận đấu!")
                # Tại đây, bạn có thể thêm logic để chuyển sang màn hình trận đấu.
            else:
                # Cập nhật chat log
                self.chat_log.config(state=tk.NORMAL)
                self.chat_log.insert(tk.END, f"Người chơi: {message}\n")
                self.chat_log.config(state=tk.DISABLED)
                self.chat_log.yview(tk.END)

    def make_circle(self, image):
        width, height = image.size
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, width, height), fill=255)
        result = Image.new("RGBA", (width, height))
        result.paste(image, (0, 0), mask=mask)
        return result

root = tk.Tk()
app = ClientApp(root)
root.mainloop()