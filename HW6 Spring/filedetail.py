# Course: PROG 1403 - Spring 2026
# Project: HW5 - Zip File
# By Shriya Sreejith

import tkinter as tk
from tkinter import messagebox, filedialog
import zipfile
import os


def get_compression_name(compress_type):
    names = {
        0: "Stored (No Compression)",
        8: "DEFLATE",
        12: "BZIP2",
        14: "LZMA",
    }
    return names.get(compress_type, f"Unknown ({compress_type})")


class FileDetailWindow:
    def __init__(self, parent, zip_info, zip_path):
        self.zip_info = zip_info
        self.zip_path = zip_path

        self.window = tk.Toplevel(parent)
        self.window.title("File Details")
        self.window.geometry("420x320")
        self.window.grab_set()  # make it modal

        self.build_ui()

    def build_ui(self):
        info = self.zip_info

        tk.Label(self.window, text="File Details", font=("Arial", 13, "bold")).pack(pady=(10, 5))

        frame = tk.Frame(self.window)
        frame.pack(padx=20, pady=5, fill="x")

        date_str = "{:04d}-{:02d}-{:02d}  {:02d}:{:02d}:{:02d}".format(
            info.date_time[0], info.date_time[1], info.date_time[2],
            info.date_time[3], info.date_time[4], info.date_time[5]
        )
        compress_name = get_compression_name(info.compress_type)

        # Calculate compression ratio safely
        if info.file_size > 0:
            ratio = 100.0 * (1 - info.compress_size / info.file_size)
            ratio_str = f"{ratio:.1f}%"
        else:
            ratio_str = "N/A"

        fields = [
            ("File Name:",          info.filename),
            ("Uncompressed Size:",  f"{info.file_size:,} bytes"),
            ("Compressed Size:",    f"{info.compress_size:,} bytes"),
            ("Compression Ratio:",  ratio_str),
            ("File Date/Time:",     date_str),
            ("Compression Method:", compress_name),
            ("CRC-32:",             f"{info.CRC:#010x}"),
        ]

        for label, value in fields:
            row = tk.Frame(frame)
            row.pack(fill="x", pady=2)
            tk.Label(row, text=label, width=20, anchor="w", font=("Arial", 10, "bold")).pack(side="left")
            tk.Label(row, text=value, anchor="w", font=("Arial", 10)).pack(side="left")

        # Button area
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=15)

        if info.compress_type == 8:  # DEFLATE
            tk.Button(btn_frame, text="Extract File", width=14,
                      command=self.extract_file).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Close", width=10,
                  command=self.window.destroy).pack(side="left", padx=5)

    def extract_file(self):
        # Ask the user where to save the extracted file
        filename = os.path.basename(self.zip_info.filename)
        save_path = filedialog.asksaveasfilename(
            title="Save Extracted File As",
            initialfile=filename
        )
        if not save_path:
            return  # user cancelled

        try:
            with zipfile.ZipFile(self.zip_path, 'r') as zf:
                data = zf.read(self.zip_info.filename)
            with open(save_path, 'wb') as out_file:
                out_file.write(data)
            messagebox.showinfo("Success", f"File extracted successfully to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not extract file:\n{e}")