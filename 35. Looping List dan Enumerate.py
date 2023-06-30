# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [3,4,7,2,8,4]
 
for angka in kumpulan_angka:
    print(f"Angka = {angka}")
    
peserta = ['Sofiyan','Thony','Ramli','Kholis']

for nama in peserta:
    print(f"Nama = {nama}")
    
# for loop dan range
print("\nFor loop dan Range")

kumpulan_angka = [5,8,2,6,8,3,3,8,6,4]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka = {kumpulan_angka[i]}")

# while 
print("\nWhile Loop")
kumpulan_angka = [5,8,2,6,8,3,3,8,6,4]

panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f"Angka = {kumpulan_angka[i]}") 
    i += 1

# List comperhention

print("\nList Comperhention")
data = ["Sofiyan",1,2,3,"Thony"]
[print(i) for i in data]

angka = [5,8,2,6,8,3,3,8,6,4]
angka_kuadrat = [i**2 for i in angka]
print(f"Angka kuadrat = {angka_kuadrat}")

# enumerate
print("\nEnumerate")
data_list = ["Sofiyan",1,2,3,"Thony"]

for index,data in enumerate(data_list):
    print(f"index = {index} , data = {data}")

