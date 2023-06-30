import os
os.system("cls")

## Class
class mahasiswa():
    
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama # .nama --> bisa menggunakan apa saja, dan berapa saja
        self.nim = input_nim
    
    def belajar(self,kondisi): 
        print(self.nama,"Sedang belajar",kondisi)
        
    def tidur(self):
        print(self.nama,"Sedang tidur di kelas")
        

## Main program

otong = mahasiswa("Otong surotong",210602138) # init akan di jalankan jika sudah di inisialisasi objek

print(otong.nama)
print(otong.nim)

otong.belajar("dengan giat")


