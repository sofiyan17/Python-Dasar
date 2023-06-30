import os
os.system("cls")

# ## Class
# class mahasiswa():
    
#     jurusan = "Teknik Informatika"
    
#     def __init__(self,input_nama,input_nim):
#         self.nama = input_nama 
#         self.nim = input_nim
            
            

# ## Main program

# otong = mahasiswa("Otong surotong",210602138)
# ucup = mahasiswa("Ucup surucup",210602135)


# otong.jurusan = "Ekonomi" # akan menambah dictionary di dirinya sendiri
# otong.kegemaran = "Futsal"

# print(mahasiswa.jurusan)
# print(otong.jurusan)
# print(ucup.jurusan)

# print(mahasiswa.__dict__) # cara menngetahui dictionary yang ada pada variable atau sebaginya
# print(ucup.__dict__)
# print(otong.__dict__)


## Class
class mahasiswa():
    
    jumlah_mahsiswa = 0
    
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama 
        self.nim = input_nim
        mahasiswa.jumlah_mahsiswa += 1
            
            

## Main program

otong = mahasiswa("Otong surotong",210602138)
ucup = mahasiswa("Ucup surucup",210602135)
tony = mahasiswa("Tony suhendra",210602130)

print(mahasiswa.jumlah_mahsiswa)

