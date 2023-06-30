import os
os.system("cls")
'''*args'''

# memasukkan data/argumen

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("Ucup", 175, 64)

def fungsi2(dataList):
    data = dataList.copy()
    
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi2(["Dadang", 180, 54])

# kenalan dengan *args

def fungsi3(*args):# *args tidak harus namanya "args", namun bisa juga dengan kata yang lain
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi3("Dudung", 156, 50)

# studi kasus
def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    
    for angka in data:
        output += angka
    return output
    
hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil {hasil}")

hasil = tambah(10,5,15)
print(f"Hasil {hasil}")