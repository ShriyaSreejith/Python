# Course: PROG 1403 - Spring 2026
# Project: HW5 - Zip File
# By Shriya Sreejith

import tkinter as tk
from tkinter import messagebox, filedialog
import os
import zipfile
from filedetail import FileDetailWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("HW5 - Zip File")
        self.root.geometry("800x550")

        self.zip_folder = ""
        self.zip_files = []
        self.current_zip_entries = []

        self.build_ui()

    def build_ui(self):
        # Header
        tk.Label(self.root, text="HW5 - Zip File", font=("Arial", 14, "bold")).pack(pady=(10, 0))
        tk.Label(self.root, text="Solution by Shriya Sreejith", font=("Arial", 11)).pack()
        tk.Label(self.root, text="").pack()  # blank line

        # Folder selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(folder_frame, text="Zip Folder:").pack(side="left")
        self.folder_var = tk.StringVar()
        tk.Entry(folder_frame, textvariable=self.folder_var, width=50, state="readonly").pack(side="left", padx=5)
        tk.Button(folder_frame, text="Browse...", command=self.browse_folder).pack(side="left")

        # Two listboxes side by side
        lists_frame = tk.Frame(self.root)
        lists_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Left: zip files
        left_frame = tk.Frame(lists_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
        tk.Label(left_frame, text="Available Zip Files:", font=("Arial", 10, "bold")).pack(anchor="w")
        zip_scroll = tk.Scrollbar(left_frame, orient="vertical")
        self.zip_listbox = tk.Listbox(left_frame, yscrollcommand=zip_scroll.set, width=30)
        zip_scroll.config(command=self.zip_listbox.yview)
        zip_scroll.pack(side="right", fill="y")
        self.zip_listbox.pack(fill="both", expand=True)
        self.zip_listbox.bind("<<ListboxSelect>>", self.on_zip_selected)

        # Right: files inside zip
        right_frame = tk.Frame(lists_frame)
        right_frame.pack(side="left", fill="both", expand=True)
        tk.Label(right_frame, text="Files Inside Selected Zip:", font=("Arial", 10, "bold")).pack(anchor="w")
        entry_scroll = tk.Scrollbar(right_frame, orient="vertical")
        self.entry_listbox = tk.Listbox(right_frame, yscrollcommand=entry_scroll.set, width=60)
        entry_scroll.config(command=self.entry_listbox.yview)
        entry_scroll.pack(side="right", fill="y")
        self.entry_listbox.pack(fill="both", expand=True)
        self.entry_listbox.bind("<<ListboxSelect>>", self.on_entry_selected)

        # Bottom buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Exit", width=10, command=self.root.quit).pack()

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder Containing Zip Files")
        if folder:
            self.zip_folder = folder
            self.folder_var.set(folder)
            self.load_zip_files()

    def load_zip_files(self):
        self.zip_listbox.delete(0, tk.END)
        self.entry_listbox.delete(0, tk.END)
        self.zip_files = []
        try:
            for filename in os.listdir(self.zip_folder):
                if filename.lower().endswith(".zip"):
                    self.zip_files.append(filename)
            if self.zip_files:
                for f in self.zip_files:
                    self.zip_listbox.insert(tk.END, f)
            else:
                messagebox.showinfo("No Zip Files", "No .zip files found in the selected folder.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not read folder:\n{e}")

    def on_zip_selected(self, event):
        selection = self.zip_listbox.curselection()
        if not selection:
            return
        zip_name = self.zip_files[selection[0]]
        zip_path = os.path.join(self.zip_folder, zip_name)
        self.load_zip_contents(zip_path)

    def load_zip_contents(self, zip_path):
        self.entry_listbox.delete(0, tk.END)
        self.current_zip_entries = []
        self.current_zip_path = zip_path
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                for info in zf.infolist():
                    self.current_zip_entries.append(info)
                    date_str = "{:04d}-{:02d}-{:02d}".format(
                        info.date_time[0], info.date_time[1], info.date_time[2]
                    )
                    compress_name = get_compression_name(info.compress_type)
                    display = "{:<30} {:>10} bytes   {}   {}".format(
                        info.filename,
                        info.file_size,
                        date_str,
                        compress_name
                    )
                    self.entry_listbox.insert(tk.END, display)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open zip file:\n{e}")

    def on_entry_selected(self, event):
        selection = self.entry_listbox.curselection()
        if not selection:
            return
        info = self.current_zip_entries[selection[0]]
        FileDetailWindow(self.root, info, self.current_zip_path)


def get_compression_name(compress_type):
    names = {
        0: "Stored (No Compression)",
        8: "DEFLATE",
        12: "BZIP2",
        14: "LZMA",
    }
    return names.get(compress_type, f"Unknown ({compress_type})")