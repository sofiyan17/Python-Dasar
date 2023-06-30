# Latihan konversi satuan temperatur
''' Ada beberapa temperatur yaitu :
        1. Celcius
        2. Reamur
        3. Fahrenheit
        4. Kelvin
'''
# Program konversi ke satuan lain
''' Adapun rumus konversi ke temperatur lain adalah sbb:
        1. Celcius
            a. Ke Reamur = 4/5*C
            b. Ke Fahrenheit = 9/5*C+32
            c. Ke Kelvin = C+273
        2. Reamur
            a. Ke Celcius = 5/4*R
            b. Ke Fahrenheit = 9/4*R+32
            c. Ke Kelvin = 5/4*R+273
        3. Fahrenheit
            a. Ke Celcius = 5/9(F-32)
            b. Ke Reamur = 4/9(F-32)
            c. Ke Kelvin = 5/9(F-32)+273
        4. Kelvin
            a. Ke Celcius = K-273
            b. Ke Reamur = 4/5(K-273)
            c. Ke Fahrenheit = 9/5(K-273)+32
'''

print("PROGRAM KONVERSI TEMPERATUR\n")

print('===CONVERSI CALCIUS===')

'''
        1. Celcius
            a. Ke Reamur = 4/5*C
            b. Ke Fahrenheit = 9/5*C+32
            c. Ke Kelvin = C+273
'''

celcius = float (input ('Masukan suhu dalam celsius :'))
print('suhun adalah ', celcius,'Celcius')

# Ke Reamur
reamur =(4/5)*celcius
print('Suhu dalam reamur adalah ', reamur, 'Reamur')

# Ke Fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print('Suhu dalam fahrenheit adalah ', fahrenheit, 'Fahrenheit')

# Ke Kelvin
kelvin = celcius + 273
print('Suhu dalam kelvin adalah ', kelvin, 'Kelvin\n')



print('===CONVERSI REAMUR===')

'''
        2. Reamur
            a. Ke Celcius = 5/4*R
            b. Ke Fahrenheit = 9/4*R+32
            c. Ke Kelvin = 5/4*R+273
'''

reamur = float(input('Masukan suhu dalam reamur :'))

# Ke Celcius
celcius = (5/4)*reamur
print('Suhu dalam celcius adalah ', celcius, 'Celcius')

# Ke Fahrenheit
fahrenheit = ((9/4)*reamur)+32
print('Suhu dalam fahrenheit adalah ', fahrenheit, 'Fahrenheit')

# Ke Kelvin 
kelvin = ((5/4)*reamur)+372
print('Suhu dalam kelvin adalah ', kelvin, 'Kelvin\n')



print('===CONVERSI FAHRENHEIT===')

'''
        3. Fahrenheit
            a. Ke Celcius = 5/9(F-32)
            b. Ke Reamur = 4/9(F-32)
            c. Ke Kelvin = 5/9(F-32)+273
'''

fahrenheit= float(input ('Masukan suhu dalam fahrenheit:'))

# Ke Celcius

celcius =5/9*(fahrenheit-32)
print('Suhu dalam celcius adalah ', celcius, 'Celcius')

# Ke Reamur
reamur = 4/9*(fahrenheit-32)
print('Suhu dalam reamur adalah ', reamur, 'Reamur')

# Ke Kelvin 
kelvin = 5/9*(fahrenheit-32)+273
print('Suhu dalam kelvin adalah ', kelvin, 'Kelvin \n')



print('===CONVERSI KELVIN===')

'''
        4. Kelvin
            a. Ke Celcius = K-273
            b. Ke Reamur = 4/5(K-273)
            c. Ke Fahrenheit = 9/5(K-273)+32
'''

kelvin = float(input ('Masukan suhu dalam kelvin :' ))

# Ke Celcius 
celcius = kelvin-273
print('Suhu dalam celcius adalah ', celcius , 'Celcius')

# Ke Reamur
reamur = 4/5*(kelvin-273)
print('Suhu dalam reamur adalah ', reamur, 'Reamur')

# Ke Fahrenheit
fahrenheit = 9/5*(kelvin-273)+32
print('Suhu dalam fahrenheit adalah ', fahrenheit,'Fahrenheit')