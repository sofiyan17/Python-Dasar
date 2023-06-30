## Teknik menduplikat list

a = ['Sofiyan','Thony','Ramli','Khalik','Khaerul']
print(f"a = {a}\n")

print(5*'=',' Pass by referens',5*'=')
b = a # pass by referens
print(f"b = {b}\n")

# kita akan merubah member dari a
print(5*'=',' Merubah member a',5*'=')
a[-1] = "Umam"
b.sort()
print(f"a = {a}")
print(f"b = {b}\n")

# address dari kedia list a dan b
print(5*'=',' Address dari a dan b',5*'=')
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}\n")

# menduplikat list dengan menggunakan copy
print(5*'=',' Menduplikat list dengan .copy',5*'=')
print("Membuat list c dengan .copy")
c = a.copy() # full duplikat / data baru 
print(f"Address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Mengubah data c")
c[-1] = "Khairul"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
