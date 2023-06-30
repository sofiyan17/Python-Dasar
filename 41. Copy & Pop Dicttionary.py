teman_teman = {
    'sf':'Sofiyan',
    'th':'Thony',
    'rm':'Ramli',
    'kh':'Kholis',
}
friends = teman_teman.copy()

print('Teman-teman = ',teman_teman)
print('Friends = ',friends)

print("")

teman_teman['kh'] = 'Kholik'
print('Teman-teman = ',teman_teman)
print('Friends = ',friends)
print("")

# pop dict (berdasarkan item)
dataSofiyan = friends.pop('sf') # datanya akan di terasnfer ke sini
print('DataSofiyan = ',dataSofiyan)
print('Friends = ',friends)
print("")

# pop item dict (data terakhir)
dataterakhir = friends.popitem()
print('Dataterakhir = ',dataterakhir)
print('Friends = ',friends)
print("")