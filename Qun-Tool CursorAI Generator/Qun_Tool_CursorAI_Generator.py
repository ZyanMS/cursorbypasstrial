import uuid
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import json
import os

def generate_unique_code():
    # Membuat kode UUID unik
    return str(uuid.uuid4())

def copy_to_clipboard():
    # Menyalin kode ke clipboard
    code = code_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(code)
    root.update()  # Menjaga isi clipboard tetap ada
    messagebox.showinfo("Sukses", "Kode berhasil disalin ke clipboard!")

def generate_new_code():
    # Membuat kode baru dan menampilkannya
    new_code = generate_unique_code()
    code_label.config(text=new_code)

def insert_code_to_file():
    # Menyalin kode yang dihasilkan ke file JSON
    code = code_label.cget("text")
    file_path = os.path.join(os.getenv("APPDATA"), "Cursor", "User", "globalStorage", "storage.json")

    try:
        # Membaca file JSON
        with open(file_path, "r") as file:
            data = json.load(file)

        # Memperbarui atau menambahkan kode baru
        data["telemetry.devDeviceId"] = code
        data["telemetry.macMachineId"] = code
        data["telemetry.machineId"] = code
        data["telemetry.sqmId"] = f"{{{code}}}"

        # Menyimpan kembali file JSON
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        messagebox.showinfo("Sukses", "Kode berhasil dimasukkan ke dalam file storage.json!")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File tidak ditemukan: {file_path}")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "File JSON tidak valid!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Cursor AI Tool - Versi 1.0 oleh Qun-Tool Dev By JRJR")
root.geometry("600x550")  # Mengatur ukuran jendela tetap
root.resizable(False, False)  # Menonaktifkan resize

# Membuat frame untuk tata letak
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Label header
header_label = tk.Label(frame, text="Cursor AI Tool", font=("Arial", 18, "bold"), fg="darkblue")
header_label.pack(pady=10)

# Label untuk menampilkan kode yang dihasilkan
code_label = tk.Label(frame, text=generate_unique_code(), font=("Arial", 14), fg="blue", wraplength=500, justify="center")
code_label.pack(pady=10)

# Tombol untuk menyalin kode
copy_button = tk.Button(frame, text="1. Salin Kode (Manual)", font=("Arial", 12), command=copy_to_clipboard, width=25, bg="lightgreen")
copy_button.pack(pady=5)

# Tombol untuk menghasilkan kode baru
generate_button = tk.Button(frame, text="2. Buat Kode Baru", font=("Arial", 12), command=generate_new_code, width=25, bg="lightblue")
generate_button.pack(pady=5)

# Tombol untuk memasukkan kode ke file JSON
insert_button = tk.Button(frame, text="3. INJEKAN KODENYA", font=("Arial", 12), command=insert_code_to_file, width=25, bg="orange")
insert_button.pack(pady=5)

# Menambahkan gambar di atas tombol
try:
    image_path = "image.png"  # Path gambar
    img = PhotoImage(file=image_path)
    img_label = tk.Label(frame, image=img)
    img_label.image = img  # Menyimpan referensi gambar
    img_label.pack(pady=10)
except Exception as e:
    messagebox.showerror("Error", "Gambar tidak ditemukan atau tidak valid!")

# Label informasi tambahan
info_label = tk.Label(frame, text="Cursor AI - Free fix for \"Too many free trial accounts used on this machine\"", font=("Arial", 10), fg="black", wraplength=500, justify="center")
info_label.pack(pady=10)

# Footer dengan informasi versi
footer_label = tk.Label(root, text="Versi 1.0 | Qun-Tool Dev By JRJR", font=("Arial", 10, "italic"), fg="gray")
footer_label.pack(side="bottom", pady=10)

# Menjalankan aplikasi
root.mainloop()
