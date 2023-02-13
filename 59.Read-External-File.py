# # tutorial membaca file external
import os

os.system('cls')
print(3*'=', 'Membaca File Txt', 3*'=')
file = open("data.txt", mode="r")

print(f"status Read : {file.readable()} ")
print(f"status Write : {file.writable()} ")

# baca seluruh file
print(file.read())

# baca perbaris
# print(file.readline(), end='')  # baca baris pertama
# print(file.readline(), end="")  # baca baris kedua

# baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah di close : {file.closed} ")
file.close()
print(f"apakah file sudah di close : {file.closed} ")

# salah satu tehnik membuka file di python
# with
print("\n", 3*'=', 'Membaca File Txt', 3*'=')

with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")


print(f"apakah file sudah di close : {file.closed} ")
