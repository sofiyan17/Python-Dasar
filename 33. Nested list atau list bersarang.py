# Nested list

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"Data list biasa = {data_list_biasa}\n")

list_2D = [data_0,data_1,data_list_biasa]
print(f"List 2D = {list_2D}")

list_2D = [data_0,data_1,data_list_biasa,5,6,7]
print(f"List 2D = {list_2D}\n")

# contoh penggunaan
peserta_0 = ['Sofiyan',20,'laik-laki']
peserta_1 = ['Thony',19,'laik-laki']
peserta_2 = ['Ramli',19,'laik-laki']

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"Peserta = {list_peserta}\n")

for peserta in list_peserta:
    print(f"Nama \t: {peserta[0]}")
    print(f"Umur \t: {peserta[1]}")
    print(f"Gender \t: {peserta[2]}\n")
    
# dengan referens
print("Permasalaha \n")
list_copy = list_peserta.copy()
print(f"Peserta = {list_copy}")
peserta_2[0] = 'Khalik'
print(f"Peserta = {list_peserta}")
print(f"Peserta = {list_copy}")
