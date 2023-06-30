import os
os.system("cls")

## fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print("Nilai kuadrat dari ", argumen, "Adalah ",total)
    return total
    
a = kuadrat(4)
print(a) # jika nilai dari variable itu berasal dari fungsi, maka nilainya harus di return terlwbih dahulu

print("-"*33)

## fungsi dengan return value dan multiple argumen

def tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1,' + ', argumen2,' = ',total)
    return total

def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1,' x ', argumen2,' = ',total)
    return total
    
a = tambah(3,4)
b = kali(3,4)
b = kali(3,a) # nilai daria argument nya bisa dari variable yang nilainya sudah di return
# atau b = kali (3,a) atau b = (3,tambah(3,4))
print(a)
print(b)

print("-"*33)

def tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1,' + ', argumen2,' = ',total)
    return [total,3,4,5]# data return tidak harus angka, namun bisa juga list, string, dan lainnya
    
a = tambah(3,4)
print(a)


