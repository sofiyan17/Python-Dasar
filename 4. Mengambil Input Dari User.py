# Input dari user
print(10*'=','MENGAMBIL INPUT DARI USER',10*'=','\n') 

# data yang di masukkan pasti string 

data= input ("masukkan data: ") 
print("data =",data, "tipe =", type(data))

# jika kita ingin mengambil integer

data_int = int(input("masukkan angka :"))
print("data =",data_int, "tipe =", type(data_int))

# jika kita ingin mengambil float

data_float = float(input("masukkan angka :"))
print("data =",data_float, "tipe =", type(data_float))

# jika ingin mengambil boolean

data_boolean = bool(input("masukkan data boolean :"))
print("data =",data_boolean, "tipe =", type(data_boolean))

# jika ingin memunculkan False pada data boolean, maka inputnya harus di Casting dulu menjadi integer

data_boolean = bool(int(input("masukkan data boolean :")))
print("data =",data_boolean, "tipe =", type(data_boolean))