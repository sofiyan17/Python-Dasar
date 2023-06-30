import os
os.system("cls")

## Class
class mahasiswa():
    
    jurusan = "Teknik Informatika"
    __nilai = 0 # Private ## ---> double underscor untuk mambuat variable private
    
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama # Public
        self.nim = input_nim
    
    def uts(self, input_nilai):
        self.__nilai += input_nilai
        
    def uas(self,input_nilai):
        self.__nilai += input_nilai
        
    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,"Tidak lulus")
        
        else:
            print(self.nama,"Lulus")
            
            
        
        

## Main program

otong = mahasiswa("Otong surotong",210602138)
ucup = mahasiswa("Ucup surucup",210602135)

otong.uts(10)
otong.uas(50)
otong.check_status()

ucup.uts(10)
ucup.uas(25)
ucup.check_status()


