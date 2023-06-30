# Date anf Time (latihan)

import datetime as dt
from re import A # mengimport  datetime sebagai dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}") # :%A untuk menampilkan hari pada tanggal yang kita maksud

tanggal = dt.date(2002,1,15)
print(tanggal) 
print(f"hari ini adalah hari = {tanggal:%A}\n") 

# cara mendeteksi  hari lahir
print("Silahkan masukan tanggal, bulan, dan tahuun lahir anda\n")
tanggal = int(input ("Tanggal\t: "))
bulan = int(input ("Bulan\t: "))
tahun = int(input ("Tahun\t: "))

hari_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah = {hari_lahir}")
print(f"Hari lahir anda adalah    = {hari_lahir:%A\n}")

hari_ini = dt.date.today()
print(f"Hari tanggal :{hari_ini}")

umur_hari = hari_ini - hari_lahir
print(f"Umur hari anda adalah :{umur_hari}")

umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur anda adalah : {umur_tahun} Tahun {umur_bulan_sisa} Bulan")