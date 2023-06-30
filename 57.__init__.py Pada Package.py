import os

os.system("cls")

import sains
from sains.matematika import sientific

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(1,2)
print(f"hasil fisika = {hasil_fisika}")

hasil_kali = sains.matematika.kali(10,27)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = sientific.pangkat(3)
print(f"hasil pangkat = {hasil_pangkat(5)}")

# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,5)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_fisika = fisika.gaya(1,2)
# print(f"hasil fisika = {hasil_fisika}")

# hasil_kali = matematika.basic.kali(10,27)
# print(f"hasil kali = {hasil_kali}")

