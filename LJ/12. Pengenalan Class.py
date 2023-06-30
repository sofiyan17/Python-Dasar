import os
os.system("cls")

class mahasiswa():
    nama = 'nama' # nilai yang menempel di class disebut --> atribut

otong = mahasiswa() # untuk mengaktifkan / menghubungkan class yang di buat
ucup = mahasiswa() # nilainya akan sama dengan variable yang kita masukkan

otong.nama = "otong surotong" # Cara mengubah nilai atribut yang ada pada class

print(otong.nama) # Cara memanggil stribut nama yang ada pada class
print(ucup.nama)