# IF dan ELSE statment 

# IF Statment
'''
    1. IF
    2. Kondisi
    3. Aksi
'''
# if kondisi: aksi
# program selanjutnya

print( 5*'=', ' IF STATMENT ',5*'=')

# program if iniline
print('\t',5*'=', ' program if iniline ',5*'=')
nama = input ('Siapa nama anda ? :')
if nama=='sofiyan' : print('Nama awalmu adalah = Muhammad')
print(f'Termakasih {nama}\n')

# program if indentation
print('\t',5*'=', ' program if indentation ',5*'=')
nama = input ('Siapa nama anda ? :')
if nama == 'sofiyan':
    print('Nama awalmu adalah = Muhammad')
    print('Program studimu adalah = Teknik Informatika')
print(f'Termakasih {nama}\n')

# ELSE statment
print( 5*'=', ' ELSE STATMENT ',5*'=')
nama = input ('Siapa nama anda ? :')
if nama == 'sofiyan':
    print('Nama awalmu adalah = Muhammad')
else:
    print('Namamu tidak terdaftar dalam program')
print(f'Termakasih {nama}\n')

