
'''
                        VARIABLE

        Berikut ini aturan-aturannya secara sederhana:
        1.	Nama variabel hanya boleh diawali oleh huruf atau underscore.
        2.	Nama variabel tidak boleh diawali oleh angka.
        3.	Nama variabel hanya bisa terdiri dari karakter alpha-numeric dan underscore (A-z, 0-9, and _ )
        4.	Nama variabel bersifat case sensitive. Artinya variabel nama berbeda dengan Nama atau naMA

'''
print(10*'=','VARIABLE',10*'=','\n') 

nama = 'Muh. Sofiyan'
usia = 20
sudah_menikah = False
print('Nama : ',nama)
print('Usia : ',usia)
print('Sudah menikah : ',sudah_menikah)
print('')
# Cara assigment nilai variable ada dua 
    # 1. singgle
    # 2. multiple
a, b, c = 'Muh. Sofiyan',20,False
print('a = ',a)
print('b = ',b)
print('c = ',c)
print('')

# kita juga bisa memberikan nilai yang sama pada variable yang berbeda
d = e = f = 'Satu'
print('d = ',d)
print('e = ',e)
print('f = ',f)
print('')

# mencari tau type data dari suatu variable
print('Type a = ',type(a))
print('Type b = ',type(b))
print('Type c = ',type(c))
print('')

# type data numerik
a = 1
b = 1.5
c = 2j
print('Type a = ',a,type(a))
print('Type b = ',b,type(b))
print('Type c = ',c,type(c))
print('')


'''
                    LIST
'''
print(10*'=','LIST',10*'=','\n') 
data_list = ['Muh. Sofiyan',20,False]
print('Data list = ',data_list)
print('Data list [0]= ',data_list[0])
print('Data list [1]= ',data_list[1])
print('Data list [2]= ',data_list[2])
print('')

# Slicing (memotong nilai pada list)
slicing = [0,1,2,3,4,5,6,7,8]
print(slicing[0:3])# angka pertama Start, dan angka kedua end(tidak diambil)
print(slicing[1:])# jika tidak ada end, maka akan menampilkan sampai akhir indeks
print(slicing[:4])# jika tidak ada start, maka akan di mulai dari awal indeks
print('')

# mengubah data list
slicing[4] = 'Empat'
print(slicing)
print('')

## menambahkan data list
# di akhir --> .append()
slicing.append('Data akhir')
print(slicing)
print('')

# Sesuai keinginan
slicing.insert(3,'Menambahkan di indeks ke-3')
print(slicing)
print('')

## menghapus data list
# pop() --> mengambil data list yang terakhir
data_yang_diambil = slicing.pop()
print('Data yang diambil = ',data_yang_diambil)
print('Data ketika sudah diambil = ',slicing)
print('')

# remove()--> menghapus data list sesuai indeks
dremove = slicing.remove('Menambahkan di indeks ke-3')
print('Data yang dihapus = ',dremove) # tidak bisa di tampilkan lagi, karena sudah di hapus
print('Data ketika sudah dihapus = ',slicing)
print('')

# del --> menghapus sesuai keinginan
del slicing[4]
print(slicing)
del slicing[4:]
print(slicing)
del slicing[:1]
print(slicing)
print('')


'''
                        FUNCTION
   def halo_dunia():
      print('Halo python! Halo dunia!')

'''
print(10*'=','FUNCTION DEF',10*'=','\n') 

# hanya menggunakan def
def halo_dunia():
      print('Halo python! Halo dunia!')
      
halo_dunia()

# menggunakan def dan parameters

def selamat_datang(nama):
    print(f"Halo {nama}!, Selamat datang.")
    
selamat_datang('Muh. Sofiyan')
selamat_datang('Toni Suhendra')
# parameters dari def tidak harus 1, namun sesuai keingnan, namun setiap parameters yang di buat wajib diisi

def perkenalan(nama,alamat,umur):
    print(f"Perkenalkan nama saya {nama} berasal dari {alamat} dan umur saya {umur}")

perkenalan('Muh. Sofiyan','RARANG',20)  

# membuat parameters opsional(tidak wajib di isi dan sudah memiliki nilai default)
def suhu(daerah, derajat, satuan = 'Celcius'):
    print(f"Suhu di {daerah} adalah {derajat} {satuan}")
    
suhu('RARANG',45)# jika tidak di isi, maka akan menampilkan niai defaultnya
suhu('RARANG',45,'Fahrenheit')# jika diisi, maka akan menampilkan apa yang di isi
    
# membuat parameters lebih dari satu
def suhu(daerah, derajat=30, satuan = 'Celcius'):
    print(f"Suhu di {daerah} adalah {derajat} {satuan}")

# jika parameters default nya lebih dari satu, dan kita hanya ingin mengisi satu dari paramerters default tersebut, maka ketika menampilkannya, kita harus menulis nama parameters nya terlebih dahulu lalu di ikuti dengan nilai parameters yang kita inginkan
suhu('RARANG',satuan='Fahrenheit')


# function dengan nilai yang dapat di kembalikan untuk di proses
def luas_persegi(sisi):
    return sisi *sisi

# untuk mengeluarkan nilai dari def return, kita membutuhkan "Print"
print(f"Luas persegi adalah = {luas_persegi(6)}")
  
# kita juga bisa simpan di dalam variabel
persegi_besar = luas_persegi(100)
persegi_kecil = luas_persegi(50)

print('Toal luas persegi besar dan kecil adalah:', persegi_besar + persegi_kecil)
print('')


print(10*'=','FUNCTION RECURSIF',10*'=','\n') 

'''def halo_dunia():
      print('Halo dunia!')
      halo_dunia() # <-- rekursifitas
  # panggil dirinya sendiri


# memanggil fungsi helo_dunia untuk pertama kali
halo_dunia()'''


def tampilkanAngka (batas, i = 1):
      print(f'Perulangan ke {i}')
      if (i < batas):
    # di sini lah rekursifitas itu terjadi
          tampilkanAngka(batas, i + 1)

# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka(10)
print('')


def tampilkanAngka (batas, i = 1):
      if (i < batas):
    # di sini lah rekursifitas itu terjadi
          tampilkanAngka(batas, i + 1)
          print(f'Perulangan ke {i}')


# memanggil fungsi tampilanAngka
# untuk pertama  kali
tampilkanAngka(10)
print('')

def tampilkanAngka (batas, i = 1):
      prefix = '--' * (i - 1)
      print(f'{prefix} Sebelum rekursif ({i})')
      if (i < batas):
            # di sini lah rekursifitas itu terjadi
          tampilkanAngka(batas, i + 1)
          print(f'{prefix} Setelah rekursif ({i})')


# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka(5)
print('')



'''
            OPERATOR
'''
print(10*'=','OPERATOR',10*'=','\n') 

# OPERATOR ARITMATIKA --> untuk menghitung (+,-,*,/,%,**,//)

a, b = 10, 3

print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '%', b, '=', a % b)
print(a, '**', b, '=', a ** b)
print(a, '//', b, '=', a //b)



# buat variabel a dan b dengan teknik squence ordering
a, b = 5, 10
# OPERATOR KOMPARASI --> untuk perbandingan (>,<,>=,<=,==,!=)
print(a, '>', b, '=', a > b)
print(a, '<', b, '=', a < b)
print(a, '==', b, '=', a == b)
print(a, '!=', b, '=', a != b)
print(a, '>=', b, '=', a >= b)
print(a, '<=', b, '=', a <= b)
print('')

# OPEATOR PENUGASAN --> shortcut (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<= )

# penugasan pertama
a = 10
print('a = 10 -> ', a)

a += 5
print('a += 5 -> ', a)

a -= 3
print('a -= 3 -> ', a)

a *= 6
print('a *= 6 -> ', a)

a /= 8
print('a /= 8 -> ', a)
print('')

# karena a jadi float, kita ubah lagi menjadi integer

a = 10
print('a = ',a)

a %= 9
print('a %= 9 -> ', a)

a //= 6
print('a //= 6 -> ', a)

a **= 1
print('a **= 1 -> ', a)


a &= 2
print('a &= 2 -> ', a)

a |= 3
print('a |= 3 -> ', a)

a ^= 4
print('a ^= 4 -> ', a)

a >>= 4
print('a >>= 4 -> ', a)

a <<= 2
print('a <<= 4 -> ', a)

print('')


# OPERATOR LOGIKA (and, or, not)
print(True and True)
print(1 + 2 == 3 and True)
print('----')
print(False or 1 > 5)
print(False or 5 > 2)
print('----')
print(not(1 > 5))
print(not(1 < 5))
print('')

# OPERATOR KEANGGOTAAN (in, not in)
perusahaan = 'Microsoft'
list_pulau = ['Jawa', 'Sumatra', 'Sulawesi']

# ini adalah dictionary, insyaallah akan kita pelajari
# di pertemuan-pertemuan yang akan datang
mahasiswa = {
  'nama': 'Lendis Fabri',
  'asal': 'Lamongan'
}

print(
  "Apakah 'c' ada di variabel perusahaan?",
  'c' in perusahaan
)
print(
  "Apakah 'c' tidak ada di variabel perusahaan?",
  'c' not in perusahaan
)
print(
  "Apakah 'Madura' ada di variabel list_pulau?",
  'Madura' in perusahaan
)
print(
  "Apakah 'Madura' tidak ada di variabel list_pulau?",
  'Madura' not in perusahaan
)
print(
  "Apakah atribut 'nama' ada di variabel mahasiswa?",
  'nama' in mahasiswa # kalau dictionary, harus menyebut atributnya, bukan nilainya 
)

print('')

# OPERATOR INDENTITAS (is, is not) menentukan apakah kedua variable sama

a = 5
b = 5
list_a = [1, 2, 3]
list_b = [1, 2, 3]
nama_a = 'budi'
nama_b = 'budi'

# output True
print('a is b:', a is b)
# output False
print('a is not b:', a is not b)

# output False
print('list_a is list_b:', list_a is list_b)
print('Id a = ',hex(id(list_a)))
print('Id b = ',hex(id(list_b)))
# output True
print('list_a == list_b:', list_a == list_b)

# output True
print('nama_a is nama_b:', nama_a is nama_b)
# output False
print('nama_a is not nama_b:', nama_a is not nama_b)

print('')


# OPERATOR BINARY 
'''
    &	Bitwise AND	Mengembalikan bit 1 jika dua bit bernilai 1
    |	Bitwise OR	Mengembalikan bit 1 jika salah satu bit bernilai 1
    ^	Bitwise XOR	Mengembalikan bit 1 jika hanya satu bit saja yang bernilai 1
    ~	Bitwise NOT	Membalikkan semua bit
    >>	Bitwise right shift	Menggeser bit ke kanan dengan mendorong salinan digit sebelah kiri dan membiarkan digit sebalah kanan terlepas
    <<	Bitwise left shift	Menggeser bit ke kiri dengan mendorong digit 0 dan membiarkan bit paling kiri terlepas
'''
x = 0
print(f"Angka binery dari {x} adalah = {x:08b}")
y = 1
print(f"Angka binery dari {y} adalah = {y:08b}")

a = 1
b = 64

print('a =', a, '=', format(a, '08b'))
print('b =', b, '=', format(b, '08b'), '\n')
print('')

print('[and]')
print('a & b =', a & b)
print(format(a, '08b'), '&', format(b, '08b'), '=', format(a & b, '08b'), '\n')

print('[or]')
print('a | b =', a | b)
print(format(a, '08b'), '|', format(b, '08b'), '=', format(a | b, '08b'), '\n')

print('[xor]')
print('a ^ b =', a ^ b)
print(format(a, '08b'), '^', format(b, '08b'), '=', format(a ^ b, '08b'), '\n')

print('[not]')
print('~a ~b =', ~a, ~b)
print('~' + format(a, '08b'), '~' + format(b, '08b'), '=', format(~a, '08b'), format(~b, '08b'), '\n')

print('[shift right]')
print('a >> b =', a >> b)
print(format(a, '08b'), '>>', format(b, '08b'), '=', format(a >> b, '08b'), '\n')

print('[shift left]')
print('b << a =', b << a)
print(format(b, '08b'), '<<', format(a, '08b'), '=', format(b << a, '08b'), '\n')

