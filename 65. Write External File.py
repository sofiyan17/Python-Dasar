import os
os.system("cls")

# 1. mode write
# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data3.txt", mode="w") as file:
    file.write("ucup surucup")
with open("data3.txt", mode="w") as file:
    file.write("jon si jonny")
with open("data3.txt", mode="w") as file:
    file.write("metimpa")
    
# 2. mode append
with open("data4.txt", mode="w") as file:
    file.write("jon si jonny\n")
with open("data4.txt", mode="a") as file:
    file.write("ucup surucup\n")
with open("data4.txt", mode="a") as file:
    file.write("tambah lagi degan append\n")
    
# mode r+
with open("data3.txt", "w", encoding="utf-8") as file:
    file.write("data ke 3\n")
    
with open("data3.txt", "r+", encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("data3.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(data)
    
with open("data3.txt", "r+", encoding="utf-8") as file:
    file.write("otong surotongdang")# menimpa isi text sesuai dengan panjang data
    