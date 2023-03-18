import qrcode
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from tkinter import filedialog


def generate_qr_code(ssid, password, security_type):
    wifi_string = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
    qr = qrcode.QRCode(version=1, box_size=3, border=2)
    qr.add_data(wifi_string)
    qr.make(fit=True)
    global qr_image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def create_qr_code():
    ssid = ssid_entry.get()
    password = password_entry.get()
    security_type = security_type_var.get()
    qr_image = generate_qr_code(ssid, password, security_type)
    qr_image = qr_image.resize((300, 300))
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image
    
def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_image.save(file_path)


window_width = 600
window_hight = 600
       
root = tk.Tk()
        
monitor_width = root.winfo_screenwidth()
monitor_hight = root.winfo_screenheight()
        
x = (monitor_width / 2) - (window_width / 2)
y = (monitor_hight / 2) - (window_hight / 2)

root.title("QR Code Generator")
root.config(bg="#dbdbdb")
root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
root.resizable(False, False)
root.iconbitmap("JK.ico")


ssid_label = tk.Label(root, text="SSID:", font=("Arial", 12), bg="#dbdbdb")
ssid_label.pack(pady=3)

ssid_entry = tk.Entry(root, font=("Arial", 12), width=50)
ssid_entry.pack(pady=3)

password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#dbdbdb")
password_label.pack(pady=3)

password_entry = tk.Entry(root, font=("Arial", 12), width=50)
password_entry.pack(pady=3)

security_type_label = tk.Label(root, text="Security type:", font=("Arial", 12), width=20, bg="#dbdbdb")
security_type_label.pack(pady=3)

security_type_var = tk.StringVar()
security_type_var.set("WPA")

options = ["WEP", "WPA", "WPA2"]

security_type_menu = tk.OptionMenu(root, security_type_var, *options)
security_type_menu.pack(pady=3)

generate_button = tk.Button(root, text="Generate QR Code", command=create_qr_code, font=("Arial", 12), width=20)
generate_button.pack(pady=3)

save_button = tk.Button(root, text="Save QR Code", command=save_qr_code, font=("Arial", 12), width=20)
save_button.pack(pady=3)

qr_label = tk.Label(root, bg="#dbdbdb")
qr_label.pack(pady=3)


root.mainloop()

