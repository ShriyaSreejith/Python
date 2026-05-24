# PROG 1403 – Spring 2026
# HW5 – Zip File
# Solution by Shriya Sreejith
# Shriya Sreejith

import tkinter as tk
from tkinter import messagebox
from zipfile import ZipFile, ZIP_DEFLATED
import os

FOLDER = "."  # current folder

def get_zip_files():
    return [f for f in os.listdir(FOLDER) if f.endswith(".zip")]

def get_zip_contents(zip_name):
    with ZipFile(os.path.join(FOLDER, zip_name), 'r') as z:
        return z.infolist()

def extract_file(zip_name, file_info):
    if file_info.compress_type == ZIP_DEFLATED:
        try:
            with ZipFile(os.path.join(FOLDER, zip_name), 'r') as z:
                z.extract(file_info.filename)
            messagebox.showinfo("Success", f"{file_info.filename} extracted!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Info", "Only DEFLATE files can be extracted.")

def open_file_details(file_info):
    win = tk.Toplevel(root)
    tk.Label(win, text=f"File: {file_info.filename}").pack()
    tk.Label(win, text=f"Size: {file_info.file_size}").pack()
    tk.Label(win, text=f"Date: {file_info.date_time}").pack()
    comp = "DEFLATE" if file_info.compress_type == ZIP_DEFLATED else "OTHER"
    tk.Label(win, text=f"Compression: {comp}").pack()
    if file_info.compress_type == ZIP_DEFLATED:
        tk.Button(win, text="Extract", command=lambda: extract_file(current_zip, file_info)).pack()

def on_zip_select(event):
    global current_zip, contents
    sel = zip_listbox.curselection()
    if not sel: return
    current_zip = zip_listbox.get(sel[0])
    file_listbox.delete(0, tk.END)
    try:
        contents = get_zip_contents(current_zip)
        for f in contents:
            file_listbox.insert(tk.END, f.filename)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_file_select(event):
    sel = file_listbox.curselection()
    if not sel: return
    file_info = contents[sel[0]]
    open_file_details(file_info)

# GUI
root = tk.Tk()
root.title("HW5 – Zip File")

tk.Label(root, text="HW5 – Zip File").pack()
tk.Label(root, text="Solution by QUICKTEAM").pack()
tk.Label(root, text="").pack()

zip_listbox = tk.Listbox(root)
zip_listbox.pack()
file_listbox = tk.Listbox(root)
file_listbox.pack()
tk.Button(root, text="Exit", command=root.quit).pack()

# Load zip files
for z in get_zip_files():
    zip_listbox.insert(tk.END, z)

zip_listbox.bind("<<ListboxSelect>>", on_zip_select)
file_listbox.bind("<<ListboxSelect>>", on_file_select)

root.mainloop()
print("HW5 Complete")