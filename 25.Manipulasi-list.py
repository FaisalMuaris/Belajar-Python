# Operasi

# Index  0(-3)    1(-2)   2(-1)
data = ["Ujang", "Asep", "Dimas"]

# Mengambil data dari data list

data_0 = data[0]
print(f"Data pertama yang (index-nya 0) adalah : {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah : {data_terakhir} ")

data_ujang = data[-3]
print(f"ini adalah data : {data_ujang} ")

# Mengambil jumlah data di dalam list

panjang_data = len(data)
print(f"panjang data adalah : {panjang_data} ")

# Manipulasi Data list

# Menambahkan item pada list sesuai posisi
print(f"Data sebelum ditambah = \n{data} ")

# index yang ditambahkan adalah index-1
data.insert(3, "Jordan")
data.insert(3, "Koplak")
print(f"data sesudah ditambah = \n{data}")

# Menambah diakhir list
data.append("Dudin")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
# atau menggabungkan list dengan list
data_baru = ['Ucup', 'rivan', 'didih']
data.extend(data_baru)
print(f"data Gabungan = \n{data}")

# Merubah data
# Ubah data kedua menjadi Jhonson
data[2] = "Jhonson"
print(f"data sudah dirubah = {data} ")


# meremove atau menghilangkan data

# data.remove("Dimas")
# data.remove("dimas")  # error, data didalamnya harus sama persis
print(f"data Remove = {data} ")

# Meremove data paling belakang
data.pop()
print(f"data akhir = \n{data} ")
