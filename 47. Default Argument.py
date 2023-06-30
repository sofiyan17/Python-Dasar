import os
os.system("cls")

## default argument 
'''Template default argument 
def nama_fungsi (nama_argument = isi default argument):
    print (f" nama = {nama_argument})
'''


# contoh 1
def say_hello(nama = "Sofiyan"):
    print(f"Hallo {nama}")
    
say_hello() # ketika isi argument tidak di isi, maka akan menghasilkan default argumennya (jika dia default argument)
say_hello ("Thony") # ketika argument nya di isi, maka akan menghasilkan apa yang di isi


# contoh 2
def selamat(nama, pesan = 'Selamat malam'): # setelah default argument, tidak boleh ada argument biasa. default argument harus berada di setelah argument biasa
    '''Fungsi dengan argument biasa, dan default argument'''
    print(f"Hai {nama}, {pesan}")
    
selamat("Sofiyan","Selamat pagi")

selamat("Thony")


# contoh 2

def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat (2,4))
print(hitung_pangkat (pangkat = 5, angka = 4)) # kita bisa akses nilai berdasarkan nama argumentnya, dan tidak harus berurutan. cara ini berguna jika kita punya banyak argument. liaht contoh 3


# Contoh 3

def fungsi(angka1 = 1, angka2 = 2, angka3 = 3, angka4 = 4):
    hasil = angka1 + angka2 + angka3 + angka4
    return hasil

print(fungsi (angka3 = 10))
    


    

