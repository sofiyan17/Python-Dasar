import os
os.system("cls")

# GUI --> Grapical User Interfase

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("500x400")
window.resizable(0, 0)
window.title("MyTkinter")

#Variable dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombolKlik():
    '''ini akan dipanaggil oleh tombol'''
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="whazzap", message=pesan)
    

#frame input
inputFrame = ttk.Frame(window)
# penempatan, Grid, Pack, Place
inputFrame.pack(padx=10,fill="x", expand=True)

# komponen-komponen
# 1. label nama depan
namaDepanLabel = ttk.Label(inputFrame, text="Nama Depan : ",)
namaDepanLabel.pack(padx=10,fill="x", expand=True)

# 2. entry nama depan
namaDepanEntry = ttk.Entry(inputFrame, textvariable = NAMA_DEPAN)
namaDepanEntry.pack(padx=10,fill="x", expand=True)

# 3. label nama belakang
namaBelakangLabel = ttk.Label(inputFrame, text="Nama Belakang : ",)
namaBelakangLabel.pack(padx=10,fill="x", expand=True)

# 4. entry nama belakang
namaBelakangEntry = ttk.Entry(inputFrame, textvariable = NAMA_BELAKANG)
namaBelakangEntry.pack(padx=10,fill="x", expand=True)

# Tombol
tombolSapa = ttk.Button(inputFrame, text="Sapa!", command=tombolKlik)
tombolSapa.pack(padx=10,pady=10,fill="x", expand=True)

#Mainloop window
window.mainloop()