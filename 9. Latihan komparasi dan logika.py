#latihan komparasi dan logika

# membuat gabungan area rentang dari angka


# +++++3-----10+++++

inputUser = float (input("masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# +++++3-----
# memeriksa angka kurang dari 3

iskurangdari = (inputUser < 3)
print('kurang dari 3 :',iskurangdari)

# -----10+++++
# memeriksa angka lebih dari 10

islebihdari = (inputUser > 10)
print('lebih dari 10 :',islebihdari)

iscorect = iskurangdari or islebihdari
print('angka yang anda masukan :',iscorect)

print('\n',10*'=','\n')

inputUser = float (input("masukan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -----3+++++10-----
# memeriksa angka lebih dari 3

islebihdari = (inputUser > 3)
print('lebih dari 3 :',islebihdari)

# -----10+++++
# memeriksa angka kurang dari 10

iskurangdari = (inputUser < 10)
print('kurang dari 10 :',iskurangdari)

iscorect = iskurangdari and islebihdari
print('angka yang anda masukan :',iscorect)


print('\n', 10*'=',' LATIHAN ', 10*'=','\n')


''' LATIHAN '''

'''
    1.----- 0 +++++ 5 ----- 8 +++++ 11 -----
    2.+++++ 0 ----- 5 +++++ 8 ----- 11 +++++
'''

print('\n', 10*'=',' 1.----- 0 +++++ 5 ----- 8 +++++ 11 ----- ', 10*'=','\n')

inputuser = float(input('masukan angka yang bernilai \nlebih dari 0 dan kurang dari 5 \natau \nlebih dari 8 dan kurang dari 11 \n :'))

# ----- 0 +++++
islebihdari0 = inputuser > 0
print('lebih dari 0 :', islebihdari0)

# +++++ 5 -----
iskurangdari5 = inputuser < 5
print('kurang dari 5 :',iskurangdari5)

iscorect1 = islebihdari0 and iskurangdari5


# ----- 8 +++++
islebihdari8 = inputuser > 8
print('lebih dari 8 :', islebihdari8)

# +++++ 11 -----
iskurangdari11 = inputuser < 11
print('kurang dari 11 :',iskurangdari11)

iscorect2 = islebihdari8 and iskurangdari11

iscorectfinaly = iscorect1 or iscorect2
print('angka yang anda masukan :',iscorectfinaly)

print('\n', 10*'=',' 2.+++++ 0 ----- 5 +++++ 8 ----- 11 +++++1 ', 10*'=','\n')

inputuser = float(input('masukan angka yang bernilai \nkurang dari 0 dan lebih dari 5 \natau \nkurang dari 8 dan lebih dari 11 \n :'))

# +++++ 0 -----
iskurangdari0 = inputuser < 0
print('kurang dari 5 :',iskurangdari0)

# ----- 5 +++++
islebihdari5 = inputuser > 5
print('lebih dari 0 :', islebihdari5)

iscorect3 = iskurangdari0 or islebihdari5


# +++++ 8 -----
iskurangdari8 = inputuser < 8
print('kurang dari 11 :',iskurangdari8)

# ----- 11 +++++
islebihdari11 = inputuser > 11
print('lebih dari 8 :', islebihdari11)

iscorect4 = iskurangdari8 or islebihdari11

iscorectfinaly2 = iscorect3 and iscorect4
print('angka yang anda masukan :',iscorectfinaly2)