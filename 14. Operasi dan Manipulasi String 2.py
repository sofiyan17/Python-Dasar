# Operator dalam bentuk metode

## merubah string menjadi case
print(10*'=','MERUBAH STIRNG MENJADI CASE',10*'=')
# merubah semua ke uppercase

salam = 'bro !'
print('normal =',salam)

salam = salam.upper()
print('upper =',salam,'\n')

# mengubah semua menjadi lowercase
halo = 'Hello Dunia'
print(halo)

halo = halo.lower()
print('lower =',halo,'\n')

## pengecekan menggunakan isX method
print(10*'=','PENGECEKAN MENGGUNAKAN isX METHOD',10*'=')
''''
    1. islower() = mengecek apakah semuanya huruf kecil
    2. isupper() = mengecek apakah semuanya huruf besar
    3. isalpha() = mengecek apakah semuanya huruf 
    3. isdecimal() = mengecek apakah semuanya angka 
    3. isalnum() = mengecek apakah semuanya huruf dan angka
    3. isspace() = mengecek apakah semuanya spasi, tab, new line \n 
    3. istitle() = mengecek apakah semuanya di awali dengan huruf besar
'''
# contoh pengecekan lowecase
salam = 'sist'
print("="*20)
print(f"is lower = {salam.islower()}")
print(f"is upper = {salam.isupper()}")
print(f"is title = {salam.istitle()}")
print(f"is alpha = {salam.isalpha()}")
print(f"is decimal = {salam.isdecimal()}")
print(f"is alnum = {salam.isalnum()}")
print(f"is space = {salam.isspace()}")
print(f"startswith = {salam.startswith('sis')}")
apakah_lower =salam.islower() # hasilnya bool
print(salam,'is lower =',apakah_lower)
apakah_upper =salam.isupper() 
print(salam,'is upper =',apakah_upper,'\n')

judul = 'It Okay Not To Be Orkay'
cek_judul = judul.istitle()
print(judul,'is title =',cek_judul,'\n')

## mengecek komponen startswith() endswith()
print(10*'=','MENGECEK AWALAN/AKHIRAN KOMPONEN',10*'=')

cek_start = 'ini adalah percobaan'.startswith('ini')
print('start =',cek_start)

cek_end = 'ini adalah percobaan'.endswith('percobaan')
print('end =',cek_end,'\n')

## penggabungan komponen join() ==> menggabungkan, split() ==> memisahkan
print(10*'=','MENGGABUNGKAN/MEMISAHKAN KOMPONEN',10*'=')

pisah = ['aku','mau','makan']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

split = 'aku mau makan'
print(split.split(),'\n')

## alokasi katrakter menggunakan rjust(), ljust(), center()
print(10*'=','ALOKASI KARAKTER',10*'=')

kanan = 'kanan'.rjust(10)
print("'",kanan,"'")

kiri = 'kiri'.ljust(10)
print("'",kiri,"'")

center = 'tengah'.center(20,':')
print("'",center,"'")

# pembatalan -> strip()

kanan = 'kanan'.strip()
print("'",kanan,"'")

kiri = 'kiri'.strip()
print("'",kiri,"'")

center = 'tengah'.strip(':')
print("'",center,"'")
