# looping dict
teman_teman = {
    'sf':'Sofiyan',
    'th':'Thony',
    'rm':'Ramli',
    'kh':'Kholis',
}

# looping first try (yang keluar adalah key nya)
print("Mengggunakan cara bisa")
for teman in teman_teman:
    print(teman)
print("")
    
# opeator untuk mengambil item / iterable
print("Mengggunakan keys")
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
print("")
    
print("Mengggunakan values")
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
print("")
    
print("Mengggunakan item")
item = teman_teman.items()
print(item)
for item in teman_teman.items():
    print(item)
print("")
    
print("Percobaan")
for key,value in teman_teman.items():
    print(f"Key = {key}   Value = {value}")