# Lambda Function

def f_kuadrat(angka):
    return angka**2


print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")


# kita coba dengan lambda
# output = lambda argument: expression
def kuadrat(angka): return angka**2


print(f"ini hasil lambda kuadrat = {kuadrat(5)}")


def pangkat(num, pow): return num**pow


print(f"hasil lambda 2 argument {pangkat(2,5)} ")

# kegunaan
# sorting untuk list biasa
data_list = ["Asep", "Udin", "Dimas"]
data_list.sort()
print(f"sort list = {data_list} ")

# sorting dengan panjang huruf


def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(f"sort list by panjang = {data_list} ")

# sort pakai lambda
data_list = ["Asep", "Udin", "Dimas"]
data_list.sort(key=lambda nama: len(nama))

print(f"sort list by lambda = {data_list} ")

# filter
data_angka = [1, 2, 34, 5, 6, 7, 8, 9]


def kurang_dari_lima(angka):
    return angka <= 5


data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x: x < 10, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x: x % 2 == 0, data_angka))

print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x: x % 2 != 0, data_angka))

print(data_ganjil)


# kelipatan 3
data_kelipatan_3 = list(filter(lambda x: x % 3 == 0, data_angka))

print(data_kelipatan_3)

# # ANONYMOUS FUNCTION
# currying  <- Haskell Curry


def pangkat_anonymous(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat_anonymous(5, 2)
print(data_hasil)

# currying


def pangkat_currying(n):
    return lambda angka: angka**n


pangkat2 = pangkat_currying(2)

print(f"pangkat 2 = {pangkat2(5)} ")
pangkat3 = pangkat_currying(3)
print(f"pangkat 3 = {pangkat3(3)} ")
print(f"pangkat bebas = {pangkat_currying(4)(5)} ")
