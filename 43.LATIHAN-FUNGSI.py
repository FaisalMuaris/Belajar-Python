''' Latihan Fungsi'''

import os


# program menghitung luas dan keliling persegi panjang

# Membuat header

# os.system('cls')
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40} ")
# print(f"{'-'*40:^40}")

# # Mengambil input User
# LEBAR = int(input("Masukan Nilai Lebar: "))
# PANJANG = int(input("Masukan Nilai Panjang: "))

# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # Tampilkan Hasil
# print(f"Hasil Perhitungan LUAS = {LUAS} ")
# print(f"Hasil Perhitungan KELILING = {KELILING} ")

def header():
    # Fungsi Header
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40} ")
    print(f"{'-'*40:^40}\n")
    print('1. Luas Persegi Panjang')
    print('2. Keliling Persegi Panjang')


def inputUser():
    '''fungsi input user'''
    # # Mengambil input User
    LEBAR = int(input("Masukan Nilai Lebar: "))
    PANJANG = int(input("Masukan Nilai Panjang: "))

    return LEBAR, PANJANG


def hitungLuas(lebar, panjang):
    '''fungsi luas'''
    return lebar * panjang


def hitungKeliling(lebar, panjang):
    '''fungsi keliling'''
    return 2 * (lebar + panjang)


def display(message, value):
    ''' Fungsi Display'''
    print(f"Hasil Perhitungan {message} = {value} ")


# Program Utama
while True:
    header()
    opsi = int(input("Pilih Perhitungan: "))
    if opsi == 1:
        LEBAR, PANJANG = inputUser()
        LUAS = hitungLuas(LEBAR, PANJANG)

        display(f"LUAS:", LUAS)
    elif opsi == 2:
        LEBAR, PANJANG = inputUser()
        KELILING = hitungKeliling(LEBAR, PANJANG)

        display(f"KELILING:", KELILING)
    else:
        print("Pilihan Tidak Ada!!")

    isContinue = input("Apakah lanjut (y/n)?")
    if isContinue == 'n':
        break
print('Program Selesai, Terima Kasih!')
