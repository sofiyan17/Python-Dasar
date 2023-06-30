import os
os.system("cls")

import time
t_start = time.time()

import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil = sains.matematika.tambah(1,2,3,4,5,)
print(f"hasil tambah dari package adalah = {hasil}")
t_end = time.time()

gaya = fisika.gaya(10,90)
print(f"gaya adalah = {gaya}")

gaya = force(10,90)
print(f"gaya adalah = {gaya}")

print(f"waktu eksekusi adalah {t_start - t_end}")