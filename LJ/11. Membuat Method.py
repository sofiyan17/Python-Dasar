import os
os.system("cls")

''' Class '''
class mahasiswa():
    nama = 'nama' 
    
    ## Fungsi yang menempel di dalam class di sebut Method
    def belajar(self,kondisi): # kita bisa menambahkan argument sesuai kebutuhan kita
        print(self.nama,"Sedang belajar",kondisi)
        
    def tidur(self):
        print(self.nama,"Sedang tidur di kelas")
        

''' Main program '''

otong = mahasiswa() 
ucup = mahasiswa()

otong.nama = "otong surotong" 
ucup.nama = "Ucup surucup"


print(otong.nama) 
print(ucup.nama)

otong.belajar("dengan giat") # cara memanggil method dengan argumennya
ucup.tidur() # cara memanggil method biasa


