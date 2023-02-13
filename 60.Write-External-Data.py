# 1. mode write,
# dia akan membuat file baru jika tidak ada
# lalu akan menimppa atau overwrite isinya
import os

os.system('cls')

with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Asep Balmon")

with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Kocak Geming")

with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("Overwrite")

# 2. Mode append

with open("data2.txt", mode="w", encoding="utf-8") as file:
    file.write("Asep Balmon\n")

with open("data2.txt", mode="a", encoding="utf-8") as file:
    file.write("Faisal Bisa\n")

with open("data2.txt", mode="a", encoding="utf-8") as file:
    file.write("Menambah Lagi dengan Append")


# 3. Mode r+
with open("data_3.txt", 'w', encoding='utf-8') as file:
    file.write('data ke 3\n')

with open("data_3.txt", "r+", encoding="utf-8") as file:
    file.write('baris-1\n')
    file.write('baris-2\n')
    file.write('baris-3\n')

with open('data_3.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    print(data)

with open('data_3.txt', 'r+', encoding='utf-8') as file:
    # menimpa isi file sesuai dengan panjang data
    file.write('')
    data = file.read()
    print(data)
