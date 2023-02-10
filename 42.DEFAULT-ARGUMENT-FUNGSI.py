import os

os.system('cls')

''' Default Argument'''
# def fungsi(argument):
# def fungsi(nilai = nilai default nya)

# contoh 1


def sayHello(nama="Kamuuuu"):
    # fungsi dengan default argument
    print(f"Hello, {nama} !")


sayHello("Muaris")
sayHello()

# contoh 2


def sapa_dia(nama, pesan='Apa Kabar?'):
    '''fungsi dengan satu input biasa dan default argument'''
    print(f"haii {nama}, {pesan} ")


sapa_dia('Muaris')


# contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil


print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat=2, angka=5)
print(hasil)

# contoh 4


def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil


print(fungsi())
print(fungsi(input3=10))
