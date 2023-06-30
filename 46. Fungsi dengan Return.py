import os

os.system("cls")
''' Fungsi dengan kembalian '''


''' Template fungsi return

def nama_fungsi (nama_argument):
    badan fungsi
    return output
'''
# Fungsi kuadrat

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    hasil_kuadrat = input_angka ** 2
    return hasil_kuadrat

print(kuadrat (6))    


y = kuadrat(5)
print(f"y = {y}")


z = 10 + kuadrat (7)

print(f"z = {z}")

# fungsi tambah
def fungsi_tambah(a,b):
    '''Fungsi return dengan multi input'''
    # inputnya bisa langsung di return
    return a + b

fungsi_tambah (10,8)

# fungsi dengan return banyak 

def operasi_matematika(angka_1, angka_2):
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    
    return kali, bagi, tambah, kurang

print(operasi_matematika (9,5))

k,l,m,n = operasi_matematika (9,5)

print(f"Hasil kali   = {k}")
print(f"Hasil bagi   = {l}")
print(f"Hasil tambah = {m}")
print(f"Hasil kurang = {n}")

