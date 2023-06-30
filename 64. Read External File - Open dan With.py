import os
os.system("cls")

## tutorial membaca file external

print(3*"=", "Membaca file txt", 3*"=")

file = open("data2.txt", mode="r")


print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# baca seluruh
# print(file.read())

# baca perbaris
# print(file.readline(),end="") # baca baris ke 1
# print(file.readline(),end="") # baca baris ke 2

# baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah di close : {file.closed}")
file.close()
print(f"apakah file sudah di close : {file.closed}")

# salah satu teknik membuka file di python
print("\n",3*"=", "Membaca file txt dengan with", 3*"=")

with open("data2.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file sudah di close : {file.closed}")

print(f"apakah file sudah di close : {file.closed}")