# Break 

import os
os.system("cls")

angka = 0
while angka <5:
    angka += 1
    print(f'Angka sekarang --> {angka}')
    
    if angka == 3:
        print(f'Angka yang anda cari adalah: {angka}\n')
        break # break akan memberhentikan  program ketika output yang kita inginkan sudah di temukan
    
    print(f'===> {angka}')
    
print('Finish','\n\n')

pencarian_data = int(input('Masukan angka yang anda cari : '))
angka = 0
while True:
    angka += 1
    print(f'Angka sekarang --> {angka}')
    
    if angka == pencarian_data:
        print(f'Angka yang anda cari adalah: {angka}\n')
        break # break akan memberhentikan  program ketika output yang kita inginkan sudah di temukan
    
    print(f'===> {angka}')
    
print('Finish\n',)