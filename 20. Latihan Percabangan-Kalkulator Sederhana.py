# Latihan 

# Kalkulator sederhana
from ast import operator


print(20*'=',' KALKULATOR SEDERHANA ',20*'=','\n')

a = float(input('Masukan angka pertama :'))
operator = input("Masukan operator yang anda mau (+,-,x,/) :")
b = float(input('Masukan angka kedua :'))

# Percabangan

if operator=='+':
    hasil = a + b
    print(f'Hasilnya adalah : {hasil:.2f}')
elif operator=='-':
    hasil = a - b
    print(f'Hasilnya adalah : {hasil:.2f}')
elif operator=='x' or operator=='*':
    hasil = a * b
    print(f'Hasilnya adalah : {hasil:2f}')
elif operator=='/':
    hasil = a / b
    print(f'Hasilnya adalah : {hasil:2f}')
else:
    print('Maaf operator tidak tersedia, Terimakasih')
