import os
os.system("cls")
'''Type hints pada fungsi'''

# bentuk standar fungsi yang sudah kita pelajari 

'''# Studi kasus
def fungsi(parameter):
    print(parameter)
    hasil = parameter ** 2
    
fungsi(1)
fungsi("Ucup")
fungsi(True)'''

# penggunaan type hints
import string
def sepuluhPangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10 ** argument
    return output

hasil = sepuluhPangkat (2)
print(hasil)

def display(argument:string):
    print(argument)
    
display("Ucup")
    