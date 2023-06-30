import os
os.system("cls")
#Belajar Casting
#Casting adalah merubah satu tipe menjadi tipe yang lain
#Tipe data = int, float, str, bool

print(10*'=','CASTING',10*'=','\n') 

print ('\n',"====CASTING INTEGER====")
data_int = 0
print ("data =",data_int,"      type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool = bool(data_int)
print ("data =",data_float,"    type =",type(data_float))
print ("data =",data_str,"      type =",type(data_str))
print ("data =",data_bool,"  type =",type(data_bool))#false jika data integernya 0

print('\n', "====CASTING FLOAT====")
data_float = 9.5
print ("data =",data_float,"    type =",type(data_float))

data_int = int(data_float)#akan di bulatkan ke bawah
data_str   = str(data_float)
data_bool = bool(data_float)
print ("data =",data_int,"      type =",type(data_int))
print ("data =",data_str,"    type =",type(data_str))
print ("data =",data_bool,"   type =",type(data_bool))#false jika data floatnya 0

print ('\n',"====CASTING STRING====")
data_str = "0"
print ("data =",data_str,"      type =",type(data_str))

data_int = int(data_str)#akan di bulatkan ke bawah dan stringnya harus angka
data_float   = float(data_str)#stringnya harus angka
data_bool = bool(data_str)
print ("data =",data_int,"      type =",type(data_int))
print ("data =",data_float,"    type =",type(data_float))
print ("data =",data_bool,"   type =",type(data_bool))#false jika data stringnya tidak ada

print ('\n',"====CASTING BOOLEAN====")
data_bool = True
print ("data =",data_bool,"   type =",type(data_bool))

data_float = float(data_bool)
data_str   = str(data_bool)
data_int = int(data_bool)
print ("data =",data_float,"    type =",type(data_float))
print ("data =",data_str,"   type =",type(data_str))
print ("data =",data_int,"      type =",type(data_int))