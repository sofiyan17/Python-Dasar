import os
os.system("cls")

# Module matematika demgam import

from matematika import tambah, kali, pangkat
# from matematika import * # <-- untuk mengimport semua

hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}") 

hasil_pangkat = pangkat(3)
print(f"hasil pangkat = {hasil_pangkat(3)}")