# ----- LIST ----- #

# Kumpulan Data Number
data_angka = [1, 2, 3]
print(data_angka)

# Kumpulan data String
data_string = ['ujang', 'asep', 'dimas']
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bala-bala", 'comro', 'asep', True]
print(data_campuran)


# Cara Alternatif membuat List
data_range = range(0, 10, 3)  # range (start->stop->step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop, loop comprerention
list_pake_for = [i**2 for i in range(0, 10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)
