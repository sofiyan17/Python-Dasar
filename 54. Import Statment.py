import os
os.system("cls")

# import

# funsinya adalah untuk mengambil program dari file external.py

# 1. untuk menyambung program dari external
import program_print
import program_dudung

# 2. import dengan data
import variable
import dadang

# data ada di namespace variable
print(variable.data)
print(dadang.data)

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,3)
print(hasil)