## Operasi
# index   0(-3)     1(-2)   2(-1)
print(10*'=',' Data list ',10*'=')
data = ['Sofiyan','Thony','Ramli']
print(data,'\n')

# mengambil data dari list
print(10*'=',' Mengambil data list ',10*'=')
data_0 = data [0]
print(f"Data pertama (index 0) = {data_0}\n")

data_terakhir = data [-1]
print(f"Data terakhir (index -1) = {data_terakhir}\n")

data_thony = data [1]
print(f"Data thony (index 1) = {data_thony}\n")

# mengambil info data jumlah data dalam list 
print(10*'=',' Mengambil info panjang data list ',10*'=')
panjang_data = len(data)
print(f"Panjang data = {panjang_data}\n")

## manipilasi data list
print(10*'=',' Manipuilasi data list ',10*'=','\n')

# Menambahkan item pada list sesuai posisi
print(5*'=',' Menambahkan item data list sesuai posisi ',5*'=')
print(f"Data sebelum di tambah = {data}")
# data.insert(posisi,item)
data.insert(2,'Khalik')
print(f"Data sesudah di tambah = {data}\n")

# Menambah di akhir list
print(5*'=',' Menambahkan item di akhir data list ',5*'=')
data.append('Hendra')
print(f"Data sesudah di tambah = {data}\n")

# menambahkan list dengan list
print(5*'=',' Menambahkan data list dengan list ',5*'=')
data_baru = ['Rofik','Thoriq','Taufik']
data.extend(data_baru)
print(f"Data gabungan = {data}\n")

# merubah data 
print(10*'=',' Marubah data list ',10*'=')
data[2] = 'Dani'
print(f"Data yang sudah di rubah = {data}\n")

# menghilangkan data
print(10*'=',' Menghilangkan data list ',10*'=')
data.remove('Dani')
print(f"Data yang sudah di hapus = {data}\n")

# meremove data paling belakang 
print(10*'=',' Meremove data list paling akhir',10*'=')
data.pop()
print(f"Data yang sudah di hapus akhirnya = {data}\n")

print(5*'=',' Mengambi data list terakhir menggunakan pop',5*'=')
data_akhir = data.pop()
print(data_akhir)


