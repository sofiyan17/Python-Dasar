import os
os.system("cls")

## Lambda Funtion

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# kita coba dengan lamda
# ouput = lambda argument : expression

kuadrat = lambda angka : angka**2

print(f"hasil lambda kuadrat = {kuadrat(3)}")

pangkat = lambda num,pow : num ** pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## kegunaan

# sorting untuk list, biasa

dataList = ["Otong", "Ucup", "Dudung"]
dataList.sort()
print(f"\nsorted List                 = {dataList}")

# sorting dia pakai panjang 

dataList.sort(key=len)
print(f"sorted List by len          = {dataList}")

def panjang_nama(nama):
    return len(nama)

dataList.sort(key=panjang_nama)
print(f"sorted List by panjang_nama = {dataList}")


# sort pakai lambda
dataList = ["Otong", "Ucup", "Dudung"]
dataList.sort(key=lambda nama:len(nama))
print(f"sorted List by lambda       = {dataList}")

# filter pakai function
dataAngka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurangDariLima(angka):
    return angka < 5
dataAngkaBaru = list(filter(kurangDariLima, dataAngka))
print(f"\nfilter by function           = {dataAngkaBaru}")

# filter pakai lambda
dataAngkaBaru = list(filter(lambda x: x < 7, dataAngka))
print(f"filter by lambda             = {dataAngkaBaru}")

# kasus genap

dataGenap = list(filter(lambda x: (x%2==0), dataAngka))
print(f"filter by lambda genap       = {dataGenap}")

# kasus ganjil
dataGanjil = list(filter(lambda x: (x%2!=0), dataAngka))
print(f"filter by lambda ganjil      = {dataGanjil}")

# kasus kelipatan tiga

data_kelipatan_tiga = list(filter(lambda x: (x%3==0),dataAngka))
print(f"filter by lambda kelipatan 3 = {data_kelipatan_tiga}")

# anonymous function
# currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil


datahasil = pangkat(5,2)
print(f"\nFungsi biasa                = {datahasil}")

# degan currying ,menjadi

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Fungsi Lambda pangkat 2     = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"Fungsi Lambda pangkat 3     = {pangkat3(3)}")
print(f"Fungsi Lambda pangkat bebas = {pangkat(4)(5)}")
