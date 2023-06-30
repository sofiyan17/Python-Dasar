# width and multiline

# data 
data_nama = 'Muh. Sofiyan'
data_umur = 20
data_tinggi = 163.5
data_nomor_sepatu = 40

# string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi} nomor sepatu = {data_nomor_sepatu}"
print(5*'=','Data string',5*'=')
print(data_string,'\n')

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}\numur = {data_umur}\ntinggi = {data_tinggi} \nnomor sepatu = {data_nomor_sepatu}"
print(5*'=','Data string',5*'=')
print(data_string,'\n')

# string multiline (dengan menggunakan kutip triplets)

data_string = f'''nama = {data_nama} 
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}

'''
print(5*'=','Data string',5*'=')
print(data_string)

# mengatur lebar 
data_nama2 = 'ucup'
data_string = f'''
nama         = {data_nama} 
nama         = {data_nama2:>5}
umur         = {data_umur:>5}
tinggi       = {data_tinggi}
nomor sepatu = {data_nomor_sepatu:>5} 

'''
# :>5 untuk mengatur kita mau mengesernya sesuai ke inginan kita
# jika datanya melebihi dari niliai/angka yang kita tetapkan maka ia tidak akan berubah
print(5*'=','Data string',5*'=')
print(data_string)