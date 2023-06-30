import os
os.system("cls")

# Module matematika demgam import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as sesuai_keinginan
# from matematika import * # <-- untuk mengimport semua

import matematika as math # <-- bisa dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}") 

hasil_pangkat = sesuai_keinginan(3)
print(f"hasil pangkat = {hasil_pangkat(3)}")