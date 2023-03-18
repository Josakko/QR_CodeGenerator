import tkinter as tk
import qrcode
from PIL import ImageTk, Image
from tkinter import filedialog
import pyperclip

class QRCodeGenerator:
    def __init__(self):
        
        self.window = tk.Tk()
        
        window_width = 600
        window_hight = 600
        
        monitor_width = self.window.winfo_screenwidth()
        monitor_hight = self.window.winfo_screenheight()
        
        x = (monitor_width / 2) - (window_width / 2)
        y = (monitor_hight / 2) - (window_hight / 2)

        self.window.iconbitmap("JK.ico")
        self.window.title("QR Code Generator")
        self.window.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
        self.window.resizable(False, False)
        self.window.config(bg="#dbdbdb")
        
        
        self.qr_label = tk.Label(self.window, bg="#dbdbdb")
        self.qr_label.pack(pady=15)
        
        self.label = tk.Label(self.window, text="Enter text to convert:", bg="#dbdbdb", font=("Arial", 12))
        self.label.pack(pady=15)
        
        self.entry = tk.Entry(self.window, width=60, font=("Arial", 12))
        
        self.entry.pack()
        
        self.button = tk.Button(self.window, text="Generate QR Code", command=self.generate_qr_code, width=20, font=("Arial", 12))
        self.button.pack(pady=5)
        
        self.save_button = tk.Button(self.window, text="Save QR Code", command=self.save_qr_code, width=20, font=("Arial", 12))
        self.save_button.pack(pady=5)
        
        self.pastebutton = tk.Button(self.window, text="Paste text", command=self.pastetext, font=("Arial", 12), width=20)
        self.pastebutton.pack(pady=20)
        
        self.qr_image = None
        
        self.window.mainloop()
        
    def pastetext(self):
        text = pyperclip.paste()
        self.entry.insert("end", text)

        
    def generate_qr_code(self):
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(self.entry.get())
        qr.make(fit=True)
        
        self.qr_image = qr.make_image(fill_color="black", back_color="white")
        
        self.show_qr_code()
        
    def show_qr_code(self):
        if self.qr_image:
            photo_image = ImageTk.PhotoImage(self.qr_image)
            self.qr_label.configure(image=photo_image)
            self.qr_label.image = photo_image
            
    def save_qr_code(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.qr_image.save(file_path)
        
QRCodeGenerator()
