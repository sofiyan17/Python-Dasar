import os
os.system("cls")

def jumlah(a,b):
    c = a + b
    return c
hasil = jumlah(4,5)
print(hasil)
print("-"*35,'\n')

# membuart anonymous function dengan lamda

coba = lambda argumen: print(argumen)
coba('Test')
print("")

kali = lambda x,y: x * y
print(kali(3,4))
print("")

# Atau 
kali = lambda x,y: x * y
hasil = kali(3,4)
print(hasil)

