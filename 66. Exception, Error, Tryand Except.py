import os
os.system("cls")

## exception akan terjadi saat program mengalami errot saat runtime

## contoh sederhana 

# input_user = int(input("Masukkan angka : "))
# hasil = None

# try:
#     hasil = 10/input_user
# except:
#     print("ini tidak boleh 0")
    
# print(f"hasil = {hasil}")


# # contoh di aplikasi 
# while True:
#     angka = int(input("Masukkan angka pembagi : "))
#     try:
#         hasil = 10/angka
#         print(f"hasil = {hasil}")
#         is_done = input("lanjutkan (y/n) ? ")
#         if is_done == "n":
#             break
#     except:
#         print("pembagi 0 silahkan masukkan input lagi")
        
# print("akhir dari program 1")


# # contoh aplikasi untuk membuat file data.txt
# try:
#     with open("data5.txt", "r") as file:
#         print(file.read())

# except:
#     print("file data5.txt tidak ditemukan, membuat file baru")
#     with open("data5.txt", "w", encoding="utf-8") as file :
#         data_baru = input("Masukkan isi data baru : ")
#         file.write(data_baru)

# print("akhir program 2")


## contoh membuat exception
# from numbers import Number
# def tambah(a,b):
#     if  not isinstance(a,Number) or not isinstance(b,Number):
#         raise TypeError("input harus angka")
#     return a+b
# print(tambah(6, 9))

## 
angka = 0
try:
    hasil = 10/ angka
except Exception as error_message:
    print(error_message)

