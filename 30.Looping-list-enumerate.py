# Looping dari List

# for loop
print('For loop')
kumpulan_angka = [1, 4, 2, 5, 6, 7, 4, 3]

for angka in kumpulan_angka:
    print(f"angka = {angka} ")


peserta = ['Asep', "Dimas", 'Sule', 'Entis', 'Udokk']
for nama in peserta:
    print(f"nama = {nama} ")

# For loop dan Range

print('\nFor loop dan Range')
kumpulan_angka = [4, 5, 2, 6, 7, 8, 1]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]} ")


# while

print('\nWhile Loop')
kumpulan_angka = [4, 5, 2, 6, 7, 8, 1]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]} ")
    i += 1

# List comprehesion
print('\nList Comprehesion')
data = ['Asep', 1, 4, 5, 'Dimas']

[print(f"data = {i} ") for i in data]

angka = [4, 5, 2, 6, 7, 8, 1]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)


# Enumerate
print('\nEnumerate Loop')
data_list = ['Asep', 1, 4, 5, 'Dimas']

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data} ")
