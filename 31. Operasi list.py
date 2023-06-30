
data_angka = [1,4,6,8,3,7,9,3,8,8,3,2,6,8,6,4,7,]
print(f"Data angka = \n{data_angka}\n")

# count data
print(5*'=',' Count data / mencari jumlah list yang di tentukan ',5*'=')
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"Jumlah angka 4 = {jumlah_data_4}")
print(f"Jumlah angka 3 = {jumlah_data_3}\n")

# mengambil posisi data (index)
print(5*'=',' Mengambil posisi data list (index)',5*'=')
data = ['Sofiyan','Thony','Ramli',]
print(f"Data = {data}")
index_Ramli = data.index("Ramli")
index_Thony = data.index("Thony")
print(f"Index Ramli = {index_Ramli}")
print(f"Index Thony = {index_Thony}\n")

# mengurutkan list
print(5*'=',' Mengurutkan data list ',5*'=')
print(f"Data angka sebelum diurutkan / sort = \n  {data_angka}")
data_angka.sort()
print(f"Data angka sesudah diurutkan / sort = \n  {data_angka}")
data.sort()
print(f"Data sesudah diurutkan / sort = \n  {data}\n")

# membalik list
print(5*'=',' Mengurutkan data list dari belakang',5*'=')
data_angka.reverse()
print(f"Data angka sesudah direverse = \n  {data_angka}")
data.reverse()
print(f"Data sesudah direverse = \n  {data}")

