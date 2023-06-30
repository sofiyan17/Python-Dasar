import os
os.system("cls")

class ojek ():
    def __init__(self,nama, transmisi, daerah ):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
        
    def cek_id_ojek(self):
        print("Nama : ",self.nama,"\nTransmisi : ",self.transmisi,"\nDaerah : ",self.daerah)
        
class Gojek (ojek): ## inheritance
    ## kita juga bisa mengubah atau menimpa apa yang ada di dalam ojek
    # def cek_id_ojek(self):
    #     print("Cek aplikasi GOjek")
        
    pass
    
        

ojek1 = ojek("Mario","Manual","Lombok")
ojek2 = Gojek("Jackson","Automatic","Bali")

ojek1.cek_id_ojek()
print('')
ojek2.cek_id_ojek()
        

