import os
os.system("cls")

'''
            KODE TERMINAL
1. py = untuk mengaktifkan komenline
2. py --version = untuk mengetahui versi python yang kita punya
3. pip --version = untuk mengetahui versi pip yang kita punya
4. pip list --format=columns = untuk mengetahui package yang kita punya / sudah terinstal
5. pip install (apa yang mau diinstall) =  untuk menginstall package --> contoh = pip install numpy
6. pip uninstall (apa yang mau di uninstall)
7. pip install --upgrade pip atau python.exe -m pip install --upgrade pip atau nama dan tempat forder python.exe -m pip install --upgrade pip(untuk mengupgrade pip)

'''


'''
                SYARAT MENGISTAL EKSTENAL PACKAGE
1. PUTHON UDAH TERINSTAL
2. KONEKSI INTERNET
3. DEFENDENSI
'''
import numpy as np 

a = np.array([1, 2, 3, 4,])
b = np.array([5, 6, 7, 8,])

print(a + b)

from PIL import Image

im = Image.open("foto.png")


print("Format file : " , im.format)
print("Ukuran file : " , str(im.size))
print("Mode file   : " , im.mode)

im.show()

