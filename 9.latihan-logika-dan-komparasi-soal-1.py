# Soal 1
# ----- 0 +++++++ 5 ------ 11 ++++++

inputUser = float(
    input('Masukan angka lebih dari 0\ndan\n kurang dari 5\ndan\nlebih dari 11 \n:'))

# memeriksa lebih dari 0
isLebihDariNol = (inputUser > 0 and inputUser < 5)
print('Lebih dari 0 dan kurang dari 5 :', isLebihDariNol)


# memeriksa lebih dari 11
isLebihdariSebelas = (inputUser > 11)
print('Lebih dari 11 :', isLebihdariSebelas)

# ----- 0 +++++++ 5 ------ 11 ++++++
isCorrect = (isLebihDariNol or isLebihdariSebelas)
print('Nilai yang anda masukan :', isCorrect)
