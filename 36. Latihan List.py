# program liat buku
#data_buku = [["judul buku","Penulis"],[],[]]

list_buku = []

while True:
    print("\nMasukan data buku \n")
    judul = input("Masukan judul buku\t:")
    penulis = input("Masukan nama penulis\t:")

    buku_baru = [judul ,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        index+=1
        print(f"{index} | {buku[0]} | {buku[1]}")
    
    print("\n","-"*10)
    islanjut = input("Apakah ingin berhenti (y/n) : ")
    if islanjut == "y":
        break
    
print("\nPROGRAM BERAKHIR")