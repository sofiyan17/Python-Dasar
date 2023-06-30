
import datetime
import os
import string
import random

# tamplat dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks': 0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    #Os.system("clear") --> untuk selain windows
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa ['nama'] = input('Nama Mahasiswa :')
    mahasiswa ['nim'] = input('NIM Mahasiswa : ')
    mahasiswa ['sks'] = int(input('SKS Lulus : '))
    TAHUN_LAHIR = int(input('Tahun Lahir (YYYY) : '))
    BULAN_LAHIR = int(input('Bulan Lahir (1-12) : '))
    TANGGAL_LAHIR = int(input('Tanggal Lahir (1-31) : '))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = ''.join({random.choice(string.ascii_uppercase) for i in range(6)})
    data_mahasiswa.update({KEY:mahasiswa})
    
    # dari tutorial sebelumnya, dan hilangkan bagian beasiswanay
    print(f"\n{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Lahir':<10}")
    print('-'*50)
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY] ['nama']
        NIM = data_mahasiswa [KEY] ['nim']
        SKS = data_mahasiswa [KEY] ['sks']
        LAHIR = data_mahasiswa[KEY] ['lahir'].strftime('%x')
        
        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:<10}")
    print("\n")
    
    is_done = input ("Apakah menambahkan data mahasiswa lain ? (y/n) : ")
    if is_done == "n":
        break

print("\nAkhir dari program, Tarima kasih")