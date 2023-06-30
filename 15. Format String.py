# format string

# contoh generic
# string
nama = 'Sofiyan'
str = 'hello '+ nama
print(str)

format_str = f"hello {nama}"
print(format_str,'\n')

# angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str,'\n')

# boolean
boolean = False 
format_str = f"boolean = {boolean}"
print(format_str,'\n')

# bilangan bulat 
angka = 15
format_str = f"bilangan bulat = {angka:d}" # :d khusus untuk bilangan bulat
print(format_str,'\n')

# bilangan ribuan/jutaan
angka = 2000
format_str = f"ribuan = {angka:,}" # :, untuk menambahkan koma pada setiap angka ribuan atau jutaan
print(format_str)
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str,'\n')

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # :.2f untuk menampilkan berapa angka setelah koma yang akan di tampilkan
print(format_str,'\n')

# menampilkan leading zero
angka = 2005.54321
format_str = f"leading zero = {angka:7.2f}" # :7.2f untuk menampilkan berapa jumlah karakter yang akan di tampilkan, dan berapa angka setelah koma yang akan di tampilkan
print(format_str)
angka = 2005.54321
format_str = f"leading zero = {angka:8.2f}" # jika ia melebihi jumlah karakter setelah berapa angka setelah koma di tentukan, maka ia akan menambahkan output kosong di awal
print(format_str)
angka = 2005.54321
format_str = f"leading zero = {angka:08.2f}" # jika di tambahkan angka 0 di awalnya maka ia akan menampilkan 0 pada output yang kosong
print(format_str,'\n')

# menampilkan tanda + atau -
angka_plus1 = 10
angka_plus2 = 10.1234
angka_minus = -10
format_minus = f"minus = {angka_minus}"
format_plus1 = f"plus1 = {angka_plus1:+d}" #:+d untuk menampilkan tanda plus pada angka yang positif
format_plus2 = f"plus2 = {angka_plus2:+.2f}" # :+.2f untuk menampilkan tanda plus pada angka yang positif dan berapa angka di belakang koma yang akan ditampilkan
print(format_plus1)
print(format_plus2)
print(format_minus,'\n')

# mempformat persen

persentase = 0.045
format_persen1 = f"persen1 = {persentase:%}" # :% untuk mengubahnya menjadi persen
print(format_persen1)
format_persen2 = f"persen2 = {persentase:.2%}" # :2% untuk menampilkan persen dan berapa banyak angka di belakang persen
print(format_persen2,'\n')

# melakukan operasi aritmatika di dalam placeholder

harga = 10000
jumlah = 5
format_string = f"harga total = Rp.{harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 225
format_binary = f"binary = {bin(angka)}" # bin() untuk menampilkan format binery
format_octal = f"octal = {oct(angka)}" # oct() untuk menampilkan format octal
format_hex = f"hexadecimal = {hex(angka)}" # hex() untuk menampilkan format hexadecimal

print(format_binary)
print(format_octal)
print(format_hex)