# Soal 1
# +++++++ 0 ------ 5 ++++++ 8 ----- 11 +++++

inputUser = float(
    input('Masukan angka kurang dari 0\ndan\nlebih dari 5 dan kurang dari 11\n:'))

# memeriksa kurang dari 0

isKurangdariNol = (inputUser < 0)
print('kurang dari nol =', isKurangdariNol)

# memeriksa lebih dari 5 dan kurang dari 8
isLebihDariLima = (inputUser > 5 and inputUser < 8)
print('lebih dari 5 dan kurang dari 8 =', isLebihDariLima)

# memeriksa lebih dari 11
isLebihDariDelapan = (inputUser > 11)
print('lebih dari 11 =', isLebihDariDelapan)
# +++++++ 0 ------ 5 ++++++ 11 -----
isCorrect = (isKurangdariNol or isLebihDariLima or isLebihDariDelapan)
print('Angka yang anda masukan =', isCorrect)
