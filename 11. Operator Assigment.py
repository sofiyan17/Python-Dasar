# Operator Assigment
# operasi yang dapat di gunakan dengan penyingkatan
# Operasi di tambah dengan Assigment

a = 5 # ini adalah Assigment
print('nilai a =',a)

# a = a + 1 ==>> Assigment (singkatan)nya adalah
a += 1
print('nilai a +=1 menjadi :',a)

a -= 2
print('nilai a -=2 menjadi :',a)

a *= 5
print('nilai a *=5 menjadi :',a)

a /= 2
print('nilai a /=2 menjadi :',a)

b = 10
print('\nnilai b :',b)

# Modulus dan floor devision
b %= 3
print('nilai b %=3 menjadi :',b)

b = 10
print('\nnilai b :',b)

b //= 3
print('nilai b //=3 menjadi :',b)

# pangakat atau eksponent
a = 5 
print('niali a :',a)
a **= 3
print('nilai a **=3 menjadi :',a)

# Operasi bitwise
#OR

c = True
print('\nnilai c :',c)

c |= False
print('nilai c |= False menjadi :',c)

c = False
print('nilai c :',c)

c |= False
print('nilai c |= False menjadi :',c)

# AND
c = True
print('\nnilai c :',c)

c &= False
print('nilai c &= False menjadi :',c)

c = True
print('nilai c :',c)

c &= True
print('nilai c &= True menjadi :',c)

# XOR
c = True
print('\nnilai c :',c)

c ^= False
print('nilai c ^= False menjadi :',c)

c = True
print('nilai c :',c)

c ^= True
print('nilai c ^= True menjadi :',c)

# geser-geser

d = 0b0100
print('\nnilai d :',format (d, '04b'))
d >>= 2
print('nilai d >>2= nilai d menjadi :',format (d,'04b'))
d <<= 1
print('nilai d <<1= nilai d menjadi :',format (d,'04b'))
