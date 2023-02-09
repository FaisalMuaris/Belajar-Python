import numpy as np
import os

os.system('cls')

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a = {list_a} ")
# print(list_a**2) # gagal
print(f"vector_a = {vector_a} ")
print(f"a pangkat 2 = {vector_a**2} ")
print(f"a kali 3 = {vector_a*5} ")

matrix_b = np.array([(1,2),(3,4)])
print(f"ini adalah matrix b = \n{matrix_b} ")
print(f"matrix b pangkat 2 = \n{matrix_b**2} ")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c} ")

ones_d = np.ones((2,2))
print(f"ones d = \n{ones_d} ")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah matrix = \n{jumlah} ")