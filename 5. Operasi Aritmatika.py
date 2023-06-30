# Operasi Aritmatika

a = 10
b = 3

# Operasi penjumlahan +

hasil = a+b
print(a, "+", b, "=", hasil)

# Operasi pengurangan -

hasil = a-b
print(a, "-", b, "=", hasil)

# Operasi perkalian *

hasil = a*b
print(a, "*", b, "=", hasil)

# Operasi pembagian /

hasil = a/b
print(a, "/", b, "=", hasil)

# Operasi pemangkatan **

hasil = a**b
print(a, "**", b, "=", hasil)

# Operasi modulus (sisa bagi) %

hasil = a%b
print(a, "%", b, "=", hasil)

# Operasi floor devision (pembulatan) //

hasil = a//b
print(a, "//", b, "=", hasil)

# Prioritas operasi

'''
    1. ()
    2. eksponent **
    3. perkalian dan teman-teman * / % //
    4. penjumlahan dan pengurangan + -
'''

x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)

# Kurung akan mengambil langkah pertama

hasil = (x + y) * z
print("(",x, "+", y,") *", z, "=", hasil)