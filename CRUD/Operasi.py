from . import Database
from .Util import random_string
from time import time
import time
import os

def create_first_data():
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus 4, silahkan masukkan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
    
    data = Database.TEMPLATES.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATES["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATES["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\r'
    
    print(data_str)
    # tahun = input("Tahun : ")
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udahlah gagal boss")    
        
def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    
def create(tahun, judul, penulis):
    data = Database.TEMPLATES.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATES["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATES["judul"][len(judul):]
    data["tahun"] = str(tahun)
    # print(data)
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\r'

    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udahlah tidak bisa menambahkan data boss") 

def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = Database.TEMPLATES.copy()
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATES["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATES["judul"][len(judul):]
    data["tahun"] = str(tahun)
    # print(data)
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\r'
    
    panjang_data = len(data_str)
    # print(panjang_data)
    
    try:
        with open(Database.DB_NAME,'r+',encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("Error dalam Update data")
    
def delete(no_buku):
    try:
        with (open(Database.DB_NAME,'r')) as file:
            counter = 0
            
            while (True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database error")
        
    os.replace("data_temp.txt",Database.DB_NAME)