data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]

print(f"list biasa = {data_list_biasa} ")

list_2D = [data_0, data_1, data_list_biasa, 7, 8]

print(f"list 2D = {list_2D} ")


# contoh penggunaan

peserta_0 = ["Asep", 22, "Laki-Laki"]
peserta_1 = ["Dimas", 15, "Laki-Laki"]
peserta_2 = ["Udok", 10, "Perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"Daftar Peserta = \n{list_peserta} ")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]} ")
    print(f"Gender\t: {peserta[2]}\n")


# permasalahan dengan reference
list_copy = list_peserta.copy()

print(f"Daftar Peserta = \n{list_copy} ")
