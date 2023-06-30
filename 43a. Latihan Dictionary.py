
import datetime

import os

from pprint import pp
# tamplat dict mahasiswa
mahasiswa_tempalte = {
    'nama':'nama',
    'nim':'0000000',
    'sks': 0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system("cls")
#Os.system("clear") --> untuk selain windows
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_tempalte.keys())
mahasiswa ['nama'] = input('Nama Mahasiswa :')
mahasiswa ['nim'] = input('NIM Mahasiswa : ')
mahasiswa ['sks'] = int(input('SKS Lulus : '))
TAHUN_LAHIR = int(input('Tahun Lahir (YYYY) : '))
BULAN_LAHIR = int(input('Bulan Lahir (1-12) : '))
TANGGAL_LAHIR = int(input('Tanggal Lahir (1-31) : '))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa) 
