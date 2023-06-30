# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar  dari

print('=== LEBIH BESAR DARI ">" ===')
hasil = a > 3
print(a, '>', 3, '=', hasil)

hasil = b > 3
print(b, '>', 3, '=', hasil)

hasil = b > 2
print(b, '>', 2, '=', hasil)

print('=== LEBIH KECIL DARI "<" ===')
hasil = a < 3
print(a, '<', 3, '=', hasil)

hasil = b < 3
print(b, '>', 3, '=', hasil)

hasil = b < 2
print(b, '<', 2, '=', hasil)

print('=== LEBIH DARI SAMA DENGAN ">=" ===')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)

hasil = b >= 3
print(b, '>=', 3, '=', hasil)

hasil = b >= 2
print(b, '>=', 2, '=', hasil)

print('=== KURANG DARI SAMA DENGAN "<=" ===')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)

hasil = b <= 3
print(b, '<=', 3, '=', hasil)

hasil = b <= 2
print(b, '<=', 2, '=', hasil)

print('=== SAMA DENGAN "==" ===')
hasil = a == 3
print(a, '==', 3, '=', hasil)

hasil = b == 3
print(b, '==', 3, '=', hasil)

hasil = b == 2
print(b, '==', 2, '=', hasil)

print('=== TIDAK SAMA DENGAN "!=" ===')
hasil = a != 3
print(a, '!=', 3, '=', hasil)

hasil = b != 3
print(b, '!=', 3, '=', hasil)

hasil = b != 2
print(b, '!=', 2, '=', hasil)

print('=== OBJECT IDENTITY "is" ===') # is artinya "Apakah sama ?".jika sama, maka akan menghasilkan "True"

''' is fungsinya unttuk membandingkan objek atau memori '''
# is sebagai komparasia object identity
'''
    print(type (x))
    print(id(x))
'''

x = 5 # ini adalah assigment membuat object
y = 5 

print('nilai x = ', x, 'id,', hex(id(x)))
print('nilai y = ', y, 'id,', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

x = 5 # ini adalah assigment membuat object
y = 6 

print('nilai x = ', x, 'id,', hex(id(x)))
print('nilai y = ', y, 'id,', hex(id(y))) 
hasil = x is y
print('x is y =', hasil)


print('=== OBJECT IDENTITY "is not" ===')# is not artinya "Apakah tidak sama ?".jika tidak sama, maka akan menghasilkan "True"

x = 5 # ini adalah assigment membuat object
y = 5 

print('nilai x = ', x, 'id,', hex(id(x)))
print('nilai y = ', y, 'id,', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)

x = 5 # ini adalah assigment membuat object
y = 6 

print('nilai x = ', x, 'id,', hex(id(x)))
print('nilai y = ', y, 'id,', hex(id(y))) 
hasil = x is not y
print('x is y =', hasil)
