import os
os.system("cls")

import datetime

mahasiswa1 = {
    'nama':'Muh. Sofiyan',
    'nim':'210602138',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2002, 1, 15),
}

mahasiswa2 = {
    'nama':'M. Taufik Hidayat',
    'nim':'210602135',
    'sks_lulus':135,
    'beasiswa':False,
    'lahir':datetime.datetime(2003, 5, 20),
}

mahasiswa3 = {
    'nama':'M. Thoriq Habib',
    'nim':'210602141',
    'sks_lulus':100,
    'beasiswa':False,
    'lahir':datetime.datetime(2003, 9, 13),
}

data_mahasiswa = {
    'key1':mahasiswa1,
    'key2':mahasiswa2,
    'key3':mahasiswa3
}
print(data_mahasiswa,'\n')

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print('-'*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY] ['nama']
    NIM = data_mahasiswa [KEY] ['nim']
    SKS = data_mahasiswa [KEY] ['sks_lulus']
    BEASISWA = data_mahasiswa [KEY] ['beasiswa']
    LAHIR = data_mahasiswa[KEY] ['lahir'].strftime('%x')
    
    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^8} {LAHIR:<10}")