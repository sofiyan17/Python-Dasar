# Operator bitwise(operasi masing-masing bit), operasi biner, binery

''''
    int -> 2 -> 0 0 0 0 0 0 1 0 
   indeks ke -> 7 6 5 4 3 2 1 0
   cara mencarinya adalah dengan 2 dipangkatkan dengan
   nilai indeks angka satu 
   Contoh : 2^1 = 2
   
   Contoh Soal : 0 0 0 0 1 0 0 1
   maka nilai integer nya adalah :
   (2^3) + (2^0) = 8 + 1 = 9
'''
a = 9 
b = 5

# bitwise OR (|)

c = a | b # Binari 1 dan 0 akan diambil 1. Binary 1 dan 1 akan di ambil salah satunya
print('\n============ OR ============')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-----------(|)--------------')                               
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise AND (&)

c = a & b # Binari 1 dan 0 tidak akan diambil. Binary 1 dan 1 akan di ambil salah satunya
print('\n=========== AND ============')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-----------(&)--------------')                               
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise XOR (^)

c = a ^ b # Binari 1 dan 0 akan diambil 1. Binary 1 dan 1 tidak akan di ambil
print('\n=========== XOR ============')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-----------(^)--------------')                               
print('nilai :',c,',binary :',format(c,'08b'))

# bitwise NOT (~)
''''
    nilainya akan berubah menjadi negatif dan lalu di tambahkan -1
'''

c = ~ a 
d = ~ b
print('\n=========== NOT ============')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-----------(~)--------------')                               
print('nilai a :',c,',binary :',format(c,'08b'))
print('nilai b :',d,',binary :',format(d,'08b'))
# FLIFT (merubah niali BINARY menjadi sebaliknya)
print('\n=========== FLIFT ============')
print('\n---------------------------')      
e = 0b00001001
f = 0b00000101
g = 0b11111111           
print('nilai e : ',e)              
print('nilai f : ',f)              
print('nilai f : ',g)              
print('\n-----------(^)--------------')      
print('nilai kebalikan a:',e^g,'binary :',format(e^g,'08b'))
print('nilai kebalikan f:',f^g,'binary :',format(f^g,'08b'))

## Shifting (menggeser binary)

# shift right (>>)

c = a >> 2
d = b >> 1
print('\n========== SHIFT ===========')
print('nilai :',a,',binary :',format(a,'08b'))
print('nilai :',b,',binary :',format(b,'08b'))
print('-----------(>>)--------------')                               
print('nilai a :',c,',binary :',format(c,'08b'))
print('nilai b :',d,',binary :',format(d,'08b'))