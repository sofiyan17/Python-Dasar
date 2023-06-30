import os

# Cara mendefinisikan Fungsi
def fungsi ():
    print("Ini adalah fungsi")
    
# Cara memanggil Fungsi
fungsi()
os.system("cls")

# Membuata fungsi sederhana
def jenis_ayam ():
    print("Ayam jago")
    
def harga_ayam ():
    jenis_ayam()
    print("Harga ayam per 1 Kg adalah Rp. 20.000")
    
# Membuat fungsi dengan input argumen

def harga_total_ayam (Kg):
    jenis_ayam()
    harga = 20000
    hargatotal = Kg*harga
    print("Harga ", Kg, "Ayam adalah ", hargatotal)
    
harga_ayam()
harga_total_ayam(3)
harga_total_ayam(0.5)
harga_total_ayam(1)
harga_total_ayam(9)
    
