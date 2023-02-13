import os

os.system('cls')
'''Fungsi Dengan Argument'''
'''
def nama_fungsi(argument):
    Badan Fungsi
'''


def helloWorld(nama, kota):
    '''funssi hello world menerima input dengan variable nama'''
    print(f"Selamat datang wahai {nama} di kota {kota}! ")


helloWorld("Asep", "Ciamis")
helloWorld('Udin', 'Bandung')

# program tambah


def tambah(angka_1, angka_2):
    '''FUngsi Tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil} ")


tambah(2, 3)
tambah(313, 131)


def say_hi(list_syntax):
    '''fungsi say hi'''
    data_syntax = list_syntax.copy()
    for syntax in data_syntax:
        print(f"Yang Terbiasa {syntax} ")


anggota_syntax = ['Array', 'Function', 'Dictionary']

say_hi(anggota_syntax)
