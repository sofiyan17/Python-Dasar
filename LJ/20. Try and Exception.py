import os
os.system("cls")

'''
                TYPE ERROR
1. SyntaxError  = Kesalahan pada sintaks
2. ErrorRunTime = Kesalahan pada saat program berjalan
    a. ValueError = Kesalahan pada saat pengimputan nilai
    b. TypeError = Kesalahan type data yang di butuhkan operasi yang kita buat
    c. ZeroDivisionError = Kesalahan yang bisa membuat program langsung close

'''
# # contoh SyntaxError
# a = input("Masukkan angka apa saja)

# # contoh ErrorRunTime
# a. ValueError 
# penyebut = int (input("Masukkan angka penyebut : ")) # ==> inputannya : huruf


# b. TypeError 

# def pembagian(a,b):
#           return a / b

# penyebut = input("Masukkan angka penyebut : ")
# pembilang = input("Masukkan angka pembilang : ")
# print(pembagian(penyebut, pembilang))



# c. ZeroDivisionError 

# def pembagian(a,b):
#           return a / b

# penyebut = int (input("Masukkan angka penyebut : "))
# pembilang = int (input("Masukkan angka pembilang : ")) # ==> inputannya : 0


# print(pembagian(penyebut, pembilang))

'''
        Cara mengatasi ErrorRunTime
Dengan 2 cara :
1. try
2. except
'''
## contoh pertama
# try:
#     a = 1/0
# except:
#     print("Error pembagian oleh 0")
    

## cara kedua
while True:
    try:
        penyebut = int (input ("Masukkan angka penyebut : "))
        pembilang = int (input ("Masukkan angka pembilang : "))
        
        hasil = penyebut / pembilang
        break
    except ValueError:
        print("Yang anda masukkan bukan angka\n")
    except ZeroDivisionError:
        print("Pembagian oleh nol tidak bisa di lakukan\n")
    except TypeError:
        print("Tipe data yang anda masukkan salah\n")
        
print("Berhasil anda memasukkan, hasil : ",hasil)

## Cara ketiga

# while True:
#     try:
#         penyebut = int (input ("Masukkan angka penyebut : "))
#         pembilang = int (input ("Masukkan angka pembilang : "))
        
#         hasil = penyebut / pembilang
#         break
#     except Exception as error: # sintaks untuk mendapatkan instruksi atau kesalahan pada ErrorRunTime akan di beri tahu. namun instruksinya berbahasa inggris
#         print(error,'\n')
        
# print("Berhasil anda memasukkan angka : ",hasil)

