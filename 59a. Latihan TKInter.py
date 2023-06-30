import os
os.system("cls")

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.resizable(1,1)
window.title("Perhitungan Luas dan Keliling Segitiga")

panjang = tk.IntVar()
lebar = tk.IntVar()

def hitung():
    labelPanjang = ttk.Label(frame, text="\nMasukkan Panjang")
    labelPanjang.pack(padx=10, fill="y", expand=1)

    entryPanjang = ttk.Entry(frame, textvariable=panjang)
    entryPanjang.pack(padx=10, fill="x", expand=1)

    labelLebar = ttk.Label(frame, text="Masukkan Lebar")
    labelLebar.pack(padx=10, fill="y", expand=1)

    entryLebar = ttk.Entry(frame, textvariable=lebar)
    entryLebar.pack(padx=10, fill="x", expand=1)

def hitungLuas():
    def hasilLuas():
        luas = panjang.get() * lebar.get()
        hasil =f"Luas = {luas}"
        showinfo(title="Hasil", message=hasil)
    subhome = ttk.Label(frame, text="\nProgram Mencari Luas Persegi Panjang")
    subhome.pack(padx=10, fill="y", expand=1)
    hitung()
    tombolHitung = ttk.Button(frame, text="Hitung", command=hasilLuas)
    tombolHitung.pack(padx=10,pady=10, fill="y",expand=1)

def hitungKeliling():
    def hasilKeliling():
        keliling = 2 * (panjang.get() + lebar.get())
        hasil =f"Keliling = {keliling}"
        showinfo(title="Hasil", message=hasil)
    subhome = ttk.Label(frame, text="\nProgram Mencari Keliling Persegi Panjang")
    subhome.pack(padx=10, fill="y", expand=1)
    hitung()
    tombolHitung = ttk.Button(frame, text="Hitung", command=hasilKeliling)
    tombolHitung.pack(padx=10,pady=10, fill="y",expand=1)

frame = ttk.Frame(window)
frame.pack(padx=10, fill="x", expand=1)

homeL1 = ttk.Label(frame, text=f"PROGRAM MENGHITUNG LUAS")
homeL1.pack(padx=10, fill="y", expand=1)
homeL2 = ttk.Label(frame, text=f"DAN MENGHITUNG KELILING PERSEGI PANJANG")
homeL2.pack(padx=10, fill="y", expand=1)
homeL3 = ttk.Label(frame, text=f"-"*70)
homeL3.pack(padx=10, fill="y", expand=1)

tombol1=ttk.Button(frame, text="Mencari Luas", command=hitungLuas)
tombol1.pack(padx=10, pady=10, fill="x", expand=1)

tombol2=ttk.Button(frame, text="Mencari Keliling", command=hitungKeliling)
tombol2.pack(padx=10, pady=10, fill="x", expand=1)

window.mainloop()

