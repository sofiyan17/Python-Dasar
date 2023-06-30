# Operasi logika atau boolean

# not, or, and, xor

#NOT

print('=== NOT ===')
a = False
c = not a

print('data a =', a)

print('--- NOT ---')
print('data c =', c,'\n')

#OR
'''
    jika salah satu atau keduanya True, maka hasilnya adalah True
    
    Operasi (OR) di ibaratkan seperti pejumlahan,
    yang dimana :
    False = 0
    True  = 1 
'''

print('=== OR ===')

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)

a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)

a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c,'\n')

# AND
'''
    jika keduanya True, maka hasilnya adalah True
    
    Operasi (AND) di ibaratkan seperti perkalian,
    yang dimana :
    False = 0
    True  = 1 
'''
print('=== AND ===')

a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)

a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)

a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c,'\n') 

# XOR (^)
'''
    jika keduanya berlawanan, maka hasilnya adalah True
'''
print('=== XOR ===')

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)

a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)