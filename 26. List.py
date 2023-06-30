# list

# kumpulan data number
print(10*'=',' List data number ',10*'=')
data_number = [1,5, 2,3]
print(data_number,'\n')

# kumpulan data String
print(10*'=',' List data string ',10*'=')
data_string = ["Sofiyan","Thony","Ramli"]
print(data_string,'\n')

# kumpulan boolean
print(10*'=',' List data boolean ',10*'=')
data_boolean = [True,False,True,True]
print(data_boolean,'\n')

# kumpulan campuran
print(10*'=',' List data campuran ',10*'=')
data_campuran = [1, 'Sofiyan',2,'TI',True]
print(data_campuran,'\n')

## alternatif membuat list
print(10*'=',' Altenatif membuat list ',10*'=')
data_range = range(0,10,2) # range (start. Stop, step)
print(data_range,'\n')

data_list = list(data_range)
print(data_list,'\n')

# membuat list dengan for loop, list comperhention
print(10*'=',' List data for loop ',10*'=')
list_pakai_for = [i**2 for i in range(0,10)]
print(list_pakai_for,'\n')

# membuat list pakai for if
print(10*'=',' List data for if ',10*'=')
list_pakai_for_if = [i for i in range(0,10) if i !=5]
print(list_pakai_for_if,'\n')

list_pakai_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pakai_for_if,'\n')

list_pakai_for_if = [i for i in range(0,10) if i%2 !=0]
print(list_pakai_for_if)