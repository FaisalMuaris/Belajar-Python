''' Type hints untuk fungsi'''

# Bentuk standar yang sudah dipelajari

import os
import string
'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)


fungsi(1)
fungsi("Ucupp")
fungsi(True)

'''

# Penggunaan type hints


def sepuluh_pangkat(argument: int) -> int:
    ''' FUNGSI DENGAN HINTS'''
    output = 10 ** argument
    return output


HASIL = sepuluh_pangkat(3)
print(HASIL)


def display(argument: str):
    print(argument)


display("Asep")


# hasil = os.system('cls')
# print(hasil)
