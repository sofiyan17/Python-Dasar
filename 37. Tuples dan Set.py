# List
data_list = [4,5,6,8,7] # menggunakan kurung siku
print(data_list)
# tuples 

data_tuples = (1,4.5,7,8,9)
print(data_tuples)
print(data_tuples[3])

# Data tuples tidak bisa di rubah isinya
# dengan cara --> data_tuples[1] = "Sofiyan"
# atau --> data_tuples.append(1)


# set (himpunan)
data_set = {2,3,5,9,7,8}
print(data_set)
data_set.add(10)
print(data_set)
data_set.pop()
print(data_set)
# tidak bisa di ambil datanya --> 
# dan tidak punya indeks --> print(data_set[3])
# namun bisa di append atau hitung panjangnya