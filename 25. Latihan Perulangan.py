666# Latihan Perulangan memnuat segitiga

sisi = 10
# 1. Menggunakan FOR
# Dummy variable 
print('Awal FOR')
count = 1

for i in range(sisi):
    print("*"* count)
    count +=1 
print('Akhir FOR\n')
    
# 2. Menggunakan While
print('Awal while')
count = 1
while True:
    print("*"*count)
    count +=1
    
    if count > sisi:
        break
print('Akhir while\n')

# 3. Hanya bilangan ganjil
print('Awal while ganjil')
count = 1
while True:
    if count%2:
        # print jika ganjil
        print('*'*count)
        count+=1
    else:
        # kembali jika ganjil
        count+=1
        continue
    if count > sisi:
        # berhenti jika count lebih dari sisi
        break
    
print('Akhir while ganjil\n')

# 4. Membuat segitiga
print('Awal Pembuatan segitiga')
count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        # print jika ganjil
        print(' '*spasi,'*'*count)
        spasi -=1
        count+=1
    else:
        # kembali jika ganjil
        count+=1
        continue
    if count > sisi:
        # berhenti jika count lebih dari sisi
        break
    
print('Akhir Pembuatan segitiga\n')

# 4. Membuat ketupat
print('Awal Pembuatan ketupat')
sisi = 10
count = 1
spasi = int(sisi/2)
balik = int(sisi/2)
while True:
    if count%2:
        # print jika ganjil
        print(' '*spasi,'*'*count)
        spasi -=1
        count+=1
    else:
        # kembali jika ganjil
        count+=1
        continue
    if count > sisi:
        # berhenti jika count lebih dari sisi
        break
spasi +=1
while True:
    if sisi%2:
        print(' '*spasi,'*'*sisi)
        sisi -=1
    else:
        spasi +=1
        sisi -=1
        continue
    if sisi ==0:
        break
    
print('Akhir Pembuatan ketupat\n')