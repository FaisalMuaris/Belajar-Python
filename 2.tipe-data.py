# a = 10, a adalah variable bernilai 10

# tipe data: angka satuan / interger
from ctypes import c_double
data_integer = 1
print("data :", data_integer, " bertipe", type(data_integer))

# tipe data: desimal / float
data_float = 3.14
print("data :", data_float, " bertipe", type(data_float))

# tipe data: string / kumpulan karakter
data_string = "ucup"
print("data :", data_string, " bertipe", type(data_string))

# tipe data: boolean / biner true/false
data_bool = False
print("data :", data_bool, " bertipe", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print("data :", data_complex, " bertipe", type(data_complex))


# tipe data dari bahasa C


data_c_double = c_double(10.5)
print("data :", data_c_double, " bertipe", type(data_c_double))
