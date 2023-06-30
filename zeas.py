Run = True
data_hasil = []

while Run:
    try:
        data_input = int(input("\nMasukkan angka yang ingin ada hitung : "))
        data_hasil.append(data_input)
        is_run = input("\nApakah ada angka lain? (y/n) : ")
        
        if is_run == "y":
            Run = False
        
    except:
        print("\nData yang ada masuka salah, silahkan coba lagi")
        

print(data_hasil)
    
print("\nTerima kasih sudah berkunjung di program kami")