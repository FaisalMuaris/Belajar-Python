import os

os.system('cls')

''' FUngsi dengan Return '''

# template fungsi dengan kembalian (return)
# def nama_fungsi(argument):
# badan  fungsi
# return output

# fungsi kuadrat


def kuadrat(input_angka):
    # fungsi kuadrat
    output_kuadrat = input_angka**2
    return output_kuadrat


y = kuadrat(4)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)


# fungsi tambah
def fungsi_tambah(angka_1, angka_2):
    # Fungsi return dengan multi input
    return angka_1+angka_2


a = fungsi_tambah(10, 5)
print(a)

# fungsi dengan return banyakk


def operasi_matematika(angka_1, angka_2):
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2

    return kali, bagi, tambah, kurang


k, b, t, kurang = operasi_matematika(9, 5)

print(f"Hasil Kali = {k} ")
print(f"Hasil Bagi = {b} ")
print(f"Hasil Tambah = {t} ")
print(f"Hasil Kurang = {kurang} ")
