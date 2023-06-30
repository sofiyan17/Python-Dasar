# Pemebahasan Tentang Tipe Data
print(10*'=','TYPE DATA',10*'=','\n') 

#type data: angka satuan <tidak ada koma>(integer)


data_integer = 7
print("data :", data_integer)
print("-bertipe :", type(data_integer))

#type data: angka dengan koma(float)
data_float = 1,7
print("data :", data_float)
print("bertipe :", type(data_float))

#type data: kumpulan karakter (string)
data_string = "Sofiyan"
print("data :", data_string)
print("bertipe :", type(data_string))

#type data: biner true/false (boolean)
data_bool = True
print("data :", data_bool)
print("bertipe :", type(data_bool),'\n')

#tipe data khusus
print(10*'=','TYPE DATA KHUSUS',10*'=','\n') 

# bilangan kompleks
print(10*'-','Type data komplex',10*'-') 
data_complex = complex(5,6) # hanya bisa berisi 2 data saja
print("data    :", data_complex)
print("bertipe :", type(data_complex),'\n')

#tipe dari bahasa C
print(10*'-','Type data dari bahasa C',10*'-') 
from ctypes import c_double
data_c_double = c_double(10.5)
print("data    :", data_c_double)
print("bertipe :", type(data_c_double))

