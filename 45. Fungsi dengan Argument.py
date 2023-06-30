import os
os.system("cls")

''' Fungsi dengan Argument '''

'''
def nama_fungsi(argument):# argument ada juga yang bilang input, parametet
    # Badan fungsi
'''

## Contoh argument String
def hello_world(nama):
    ''' fungsi hello world, menerima input dengan variable nama'''
    print(f"Selamat datang di dunia wahai {nama}")
    
hello_world("Sofiyan")
hello_world("Thony")
# program tambah

## Contoh argument angka
def tambah(a,b):
    '''Fungsi tambah '''
    hasil = a + b
    print(f"{a} + {b} = {hasil}")


tambah(1,5)
tambah(1000,1)


## Contoh argument list
def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")
        
# di sini tempat listnya
anggota = ['Sofiyan', 'Thony', 'Ramli']

say_hi(anggota)
        
        