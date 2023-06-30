# Perulangan
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka,'\n')

# Looping dengan list
'''
for kondisi:
    aksi
'''
angka_list = [0,1,2,3,4,5] # ini adalah list
print(angka_list,'\n')
for i in angka_list:
    print(f'i sekarang adalah => {i}')
print('Akhir looping dengan list','\n')

# looping dengan range

angka_range = range(5)
for i in angka_range:
    print(f'i sekarang adalah => {i}')
print('Akhir looping dengan range 1','\n')

angka_range = range(1,5) # 1,5 ==> dimulai dengan angka 1, semua angka sebelum 5

for i in angka_range:
    print(f'i sekarang adalah => {i}')
print('Akhir looping dengan range 2','\n')
angka_range = range(1,8)

for i in angka_range:
    print(f'Nama saya adalah Muh. Sofiyan')
print('Akhir looping dengan range 3','\n')

# looping menggunakan String
string = 'Muh. Sofiyan'
for huruf in string:
    print(huruf)
print('Akhir looping dengan string','\n')
    