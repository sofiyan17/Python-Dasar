import os
os.system("cls")

# fungsi dengan menggunakan argumen sederhana
def siswa (nama):
    print("Siswa ini bernama :",nama)

siswa('Mario')

# fungsi dengan menggunakan keywords arguments

def guru (nama,pelajaran):
    print("Guru ini bernama",nama)
    print("Mengajar ",pelajaran)
    
guru(nama='Harianto',pelajaran='Dasar pemrograman')
guru(pelajaran = 'ALgoritma',nama='Andriska' )# nggk harus berdasarkan urutannya
guru('B.Inggris','Kerta wijaya')# ini akan memasukkan ke variable pertama lalu selanjutnya

# Fungsi dengan menggunakan Default arguments

def teman (nama,sifat='baik',jurusan='Teknik informatika'): # Variable yang sudah mempunyai nilai bisa tidak di isi dan bisa juga dirubah,
    print("Teman ini bernama ",nama)
    print("Sifatnya ",sifat)
    print("Jurusannya ",jurusan)

teman('Thorik') # Variable yang tidak mempunyai nilai default, nilainya harus diisi ketika pemanggilan
teman('Taufik',sifat='Humor')
teman('Rusdi',jurusan='Olahraga')

