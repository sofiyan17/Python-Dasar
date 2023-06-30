# ELIF = else if statment

nama = input('Masukan Nama Anda :')

if nama == 'sofiyan': # kondisi 1
    print(f'''Your identitas :
          Nama  : Muh. Sofiyan
          Prodi : Teknik Informatika
          Kelas : TI E
          ''') # aksi true 1
elif nama == 'thoriq': # Kondisi 2
    print(f'''Your identitas :
          Nama  : M. Thoriq Habib
          Prodi : Sistem Informasi
          Kelas : SI B
          ''') # aksi true 2
elif nama == 'taufiq': # kodisi 3
    print(f'''Your identitas :
          Nama  : M. Hidayat Ramdan
          Prodi : Teknik Komputer
          Kelas : TK A
          ''') # aksi true 3
else:
    print('Maaf nama anda tidak terdaftar dalam program') # aksi false