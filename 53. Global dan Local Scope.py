import os
os.system("cls")
## Global dan local scope

nama_global = "Otong" # <- ini variable global


# akses varaiable global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")
    
fungsi1()

# akses variable global dalam loop

for i in range(0, 5):
    print(f"loop {i} - {nama_global}")
    
# percabangan 
if True:
    print(f"if menampilkan {nama_global}")
    

## variable local scope

def fungsi2():
    nama_local = "Ucup" # <-- variable local scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan

## contoh pengunaan
def say_otong():
    print(f"hello {nama}")
    
nama = "Otong"
say_otong()

## contoh 2: merubah variabel global

angka= 0

name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru
    
print(f"sebelum {angka, name}")
ubah(10, "Otong")
print(f"sesudah {angka, name}")

## contoh 3:

angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0
    
print(angka)
print(angka_dummy)

if True:
    angka = 15
    angka_dummy = 45
    
print(angka)
print(angka_dummy)