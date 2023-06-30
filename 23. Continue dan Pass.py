# Continue, Pass, Break

# Pass ==> berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0
while angka < 5 :
    angka += 1
    print(angka)
print('\n')

angka = 0
while angka < 5 :
    angka += 1
    if angka == 3:
        print('Angka sama dengan 3')
    print(angka)
print('\n')

angka = 0
while angka < 5 :
    angka += 1
    if angka == 3:
        pass # ini tidak akan di eksekusi
    print(angka)
print('\n')
    
# Continue 
angka = 0
print(f'Angka sekarang ==> {angka}\n')

while angka <5:
    angka += 1
    print(f'Angka sekarang ==> {angka}') # aksi 1
    
    if angka ==3:
        print(f'Sekarang angka {angka}')
        continue # akan membuat loop ke step selanjutnya 
    '''
    Semua looping yang berada setelahnya akan di loncat 
    '''
    
    print(f'===> {angka}') # aksi 2
print(f'Finish\n')