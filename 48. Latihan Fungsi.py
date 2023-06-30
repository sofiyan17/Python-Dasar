'''Latihan Fungsi'''

# MEMbuat Header
# import os
# os.system("cls")


# # Program menghitung luas dan keliling persegi panjang

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# #Mengambil input user

# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai panjang : "))
# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai panjang : "))

# # Program menghitung luas dan keliling
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # Tampilan Hasil
# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan keliling = {KELILING}")

def header():
    import os
    os.system("cls")

    # Program menghitung luas dan keliling persegi panjang

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")
    
def inputUser():
    lebar = int(input("Masukkan nilai lebar : "))
    panjang = int(input("Masukkan nilai panjang : "))
    return lebar, panjang

def hitungLuas(lebar, panjang):
    return lebar * panjang

def hitungKeliling(lebar, panjang):
    return 2 * (lebar + panjang)

def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")
    
    
# Program utama
while True:
    header()
    print(f'''{'OPSI':^40}
1. Luas
2. Keliling
''')
    
    options = input("Masukkan nomor opsi : ")
    print("")
    
    if options == "1":
        LEBAR, PANJANG = inputUser()
        LUAS = hitungLuas(LEBAR,PANJANG)
        display("lebar", LUAS)
    elif options == "2":
        LEBAR, PANJANG = inputUser()
        KELILING = hitungKeliling(LEBAR, PANJANG)
        display("keliling", KELILING)
    else:
        print("Maaf opsi yang anda masukkan tidak ada silahkan coba kembali")
        
    
    isContinue = input("\nApakah ingin mencoba lagi (y/n) ? : ")
    if isContinue == "n":
        print("\nProgram Selesai, Terima Kasih")
        break
    elif isContinue != "y" and "n":
        print("Maaf opsi yang anda masukkan tidak ada silahkan run kembali")
        break
    
    