# opertaor doctionary
data_dict = {
    'sf':'Sofiyan',
    'th':'Thony',
    'rm':'Ramli',
    'ky':'Value',
}

# panjang dintionary
lendict = len(data_dict)
print(f"Panjang dari dict : {lendict}")

# mengecek key axist atau tidak 
key = "sf"
cekkey = key in data_dict
print(f"Apakah {key} ada di data_dict : {cekkey}")

# mengakses value (read) dengan get
print(data_dict['sf'])
print(data_dict.get('sf')) # untuk mengetahui apakah dia dict atau tidak
print(data_dict.get('so')) # apabila key tidak ada, maka akan keluar tampilan "None"
print(data_dict.get('sl','Key tidak ada di dalam program')) # menentukan masssage sesuai keinginan apabila key tidak ada

# mengubah data disct
data_dict['ky'] = "Kholis"
print(data_dict)

# menambah data Dict
data_dict['ko'] = 'Kholik'
print(data_dict)

# mengupdate data dict
data_dict.update({'sf':'Sofiyan'}) # kalau sudah ada di dalam datanya, maka akan di hiraukan
data_dict.update({'th':'Thoriq'}) # kalau belum ada di dalam datanya, maka akan langsung di tambahkan

print(data_dict)

# mendelete data dict
del data_dict['th']
print(data_dict)