# Operasi dan manipulsai String

'''
    1. menyambung stirng (concatenate)
    2. menghitung panjang atau banyak karakter dari string (len)
    3. operator untuk string 
       A. mengecek apakah ada komponen char atau string di string(in/not in)
       B. mengulang stirng(angka*string/string*angka)
       C. indexing atau mengambil data dari string ([..]) yang dimulai dari 0
       D. item terkecil/terbesar (min/max)
       E. asci code => untuk mengentahui nilai dari karakter atau nilai itu berbentuk karakter apa (ord)
    4. operator dalam bentuk metode ==>> untuk mengetahui jumlah suatu karakter pada suatu data (.count)
'''

# contoh nomer 1
nama_pertama = 'muhammad'
nama_akhir = 'sofiyan'
nomer_kesukaan = 17

nama_lengkap = nama_pertama +' '+ nama_akhir 
print(nama_lengkap)

# contoh nomer 2
panjang = len(nama_lengkap)
print('panjang dari ',nama_lengkap,'=',panjang)

# contoh nomer 3

# contoh 3A

d = "d"
status = d in nama_lengkap
print('apakah huruf',d,'ada di',nama_lengkap,'=',status)

D = "D"
status = D in nama_lengkap
print('apakah huruf',D,'ada di',nama_lengkap,'=',status)

d = "d"
status = d not in nama_lengkap
print('apakah huruf',d,'ada di',nama_lengkap,'=',status)

# contoh 3B
print(10*'wk')

# contoh 3C
print('index ke-0 :'+nama_lengkap[0])
print('index ke-9 :'+nama_lengkap[9])
print('index ke(-1) :'+nama_lengkap[-1])
print('index ke(-2) :'+nama_lengkap[-2])
print('index ke(0:8) :'+nama_lengkap[0:10])
print('index ke(0:8) :'+nama_lengkap[9:16])
print('index ke(0,2,4,6,8,10,12,14,16) :'+nama_lengkap[0:16:2])

# contoh 3D
print('item paling kecili adalah :'+min(nama_lengkap))
print('item paling kecili adalah :'+max(nama_lengkap))

# contoh 3E
ascii_code = ord('s')
print('ASCII CODE untuk s adalah :'+ str(ascii_code))
karakter = 110
print('Karakter dari ASCII CODE 110 adalah :'+ chr(karakter))

# contoh 4
data = 'ini dalah operasi untuk opertor metode'
jumlah = data.count('o')
print('jumlah o pada \''+ data +'\' adalah = ' + str(jumlah))