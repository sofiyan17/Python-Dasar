import os
os.system("cls")

import numpy as np

list_a = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

# print(list_a**2) # <-- akan gaga;
print(f"list a = {list_a}")
print(f"a pangkat 2 = {vector_a**2}")
print(f"a kali 5 = {vector_a*5}")
print(f"vector a = {vector_a}")

matrix_b = np.array([(1,2),(3,4)])

print(f"\nmatrix b = \n{matrix_b}")
print(f"\nmatrix b^2= \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"\nzeros_c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"\nones_d = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"\njumlah = \n{jumlah}")