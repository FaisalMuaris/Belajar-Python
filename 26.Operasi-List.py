dataAngka = [5, 4, 67, 2, 3, 5, 2, 5, 6, 7, 2, 5, 5, 6, 7]
print(f"Data angka = \n{dataAngka}\n")

# Count data

jumlah_data_5 = dataAngka.count(5)
jumlah_data_2 = dataAngka.count(2)

print(f"jumlah angka 5 pada data angka = {jumlah_data_5} ")
print(f"jumlah angka 2 pada data angka = {jumlah_data_2} ")

# Ambil posisi data (index)

data = ["Asep", "Udok", "Dimas", "Amin"]

print(f"Data = {data} ")

index_udok = data.index("Udok")
index_amin = data.index("Amin")
print(f"Index si Udok = {index_udok} ")
print(f"Index si Amin = {index_amin} ")

# =================================
#          MENGURUTKAN LIST
# =================================


print(f"data angka sebelum sort = \n{dataAngka} ")
dataAngka.sort()  # Angka terkecil ke terbesar
print(f"data angka sort = \n{dataAngka}")

print(f"data = {data} ")
data.sort()  # String mengurut dari A-Z
print(f"data sort = {data} ")


# ========== Urutkan dari Terbesar ke Terkecil ======
# ========== Urutkan dari Huruf Z - A =====
#
# Balik Listnya
dataAngka.reverse()
data.reverse()
print(f"Data di reverse = \n{dataAngka} \n{data} ")
