import os
os.system("cls")

def tambah(a,b):
    print(a, '+', b,'=',a + b)

def kurang(a,b):
    print(a, '-', b,'=',a - b)

# print(__name__) # 1. jika di run di filenya sendiri, maka akan menghasilkan --> __main__
                 # 2. jika file ini di import di file lain. kemudian di run, maka akan menghasilkan --> nama dari file ini


def main():
    print("Ini adalah fungsi utama dari matematika")
    
if __name__ == "__main__":
    main()

