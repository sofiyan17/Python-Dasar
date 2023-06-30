import os
os.system("cls")

## Stack

tumpukan = [1,2,3,4,5,6,]
print("Data sekarang : ", tumpukan)

# memasukkan daata baru
tumpukan.append(7)
print("Data masuk    : ", 7)
print("Data sekarang : ", tumpukan)
tumpukan.append(8)
print("Data masuk    : ", 8)
print("Data sekarang : ", tumpukan)

out = tumpukan.pop() # .pop() --> adalah cara Stacking
print("Data Keluar   : ",out)
print("Data sekarang : ", tumpukan)

print("")
print("-"*50)
print("")

## Queus

from collections import deque # Keyword pertama untuk melakukan Queues

antrian = deque([1,2,3,4,5])

print("Data sekarang : ",antrian)

# menambahkan data 
antrian.append(6)
print("Data masuk    : ",6)
print("Data sekarang : ",antrian)

antrian.append(7)
print("Data masuk    : ",7)
print("Data sekarang : ",antrian)

# mengurangi antrian 

out = antrian.popleft() # Keyword kedua --> .popleft()
print("Data keluar   : ",out)
print("Data sekarang : ",antrian)

out = antrian.popleft()
print("Data keluar   : ",out)
print("Data sekarang : ",antrian)

out = antrian.popleft()
print("Data keluar   : ",out)
print("Data sekarang : ",antrian)

antrian.append(8)
print("Data masuk    : ",8)
print("Data sekarang : ",antrian)
