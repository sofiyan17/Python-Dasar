import os
os.system("cls")

'''**kwargs'''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi("Ucup", 176,45)

def fungsi2(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
    
fungsi2(nama="Ucup", tinggi=176,berat=45)

def math(*args, **kwargs):
    if kwargs["option"] == "tambah":
        output = 0
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operator")
    
    return output

hasil = math(1,2,3,4,option="tambah")
print(f"Hasil tambah = {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"Hasil kali = {hasil}")
        
    