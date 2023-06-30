import os
os.system("cls")

## input output file

# membuat file text

''' 
            MODE 
            
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan di buat file baru
r = read only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write anda read mode 

'''
# Membuat file text

file = open("data.txt", "w")

file.write("Ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nIni baris ke-dua")
file.write("\nIni baris ke-tiga")
file.write("\nIni baris ke-empat")

file.close()

# membaca file text

bacafile = open("data.txt", "r")
# print(bacafile.read()) # cara biasa
# print(bacafile.read(10)) # cara untuk menampilkan berapa karakter yang akan di tampilkan
print(bacafile.readline()) # menampilkan perbaris
print(bacafile.readline()) # readline yang ke selanjutnya akan menamlpilkan baris yang selanjutnya

bacafile.close()

# appending mode

modeappend = open("data.txt", "a")
modeappend.write("\nBaris ini dibuat menggunakan mode append")
modeappend.close()


