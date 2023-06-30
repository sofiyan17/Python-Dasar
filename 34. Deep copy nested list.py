data_0 = [1,2,]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()
print(f"Data = {data_2D}")
print(f"Data copy = {data_2D_copy}")

# mengambil data dari nested list

data = data_2D[1][0]
print(f"data = {data}")

#address semuanya

print(f"address data_2D asli = {hex(id(data_2D))}")
print(f"address data_2D_copy= {hex(id(data_2D_copy))}\n")

print(f"address dari member ke-1")
print(f"address data_2D asli = {hex(id(data_2D[0]))}")
print(f"address data_2D_copy= {hex(id(data_2D_copy[0]))}\n")
data_2D[1][0] = 5
data_2D[2] = 9
print(f"Data = {data_2D}")
print(f"Data copy = {data_2D_copy}")

# kita gunakan deppcopy

from copy import deepcopy
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
print(f"address data_2D asli = {hex(id(data_2D[0]))}")
print(f"address data_2D_copy= {hex(id(data_2D_deepcopy[0]))}\n")

print(f"address dari member ke-1")
print(f"address data_2D asli = {hex(id(data_2D[0]))}")
print(f"address data_2D_copy= {hex(id(data_2D_copy[0]))}\n")

data_2D[1][1] = 6
print(f"Data = {data_2D}")
print(f"Data copy = {data_2D_copy}")
print(f"Data deep = {data_2D_deepcopy}")