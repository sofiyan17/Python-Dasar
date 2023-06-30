import os
os.system("cls")

# Scope variable : local

namateman = "Ramli"

def rubahnamateman (namabaru):
    namateman = namabaru # variaable local
    print ("Saya merubah nama teman menjadi ", namateman)

rubahnamateman("Thoni")
rubahnamateman("Kholis")
print("Nama teman saya menjadi ",namateman) # nama teman tidak akan berubah, karena ia termasuk scope global
print("")

# Scope variable : global

namateman = "Ramli"
makanansaatini = "Nasgor"

def rubahnamateman (namabaru):
    global namateman
    namateman = namabaru 
    print ("Saya merubah nama teman menjadi ", namateman)
    
rubahnamateman("Thoni")
print("Nama teman saya menjadi ",namateman) 
print("")
    
    
def rubahnamamakanan (makanan, nama):
    global makanansaatini,namateman # cara mengubah multiple variable global
    namateman = nama 
    makanansaatini = makanan

rubahnamamakanan ("Bakso","Khalik") 

print("Nama teman saya saat ini menjadi ", namateman, "dan makanan kita saat ini adalah ",makanansaatini)

