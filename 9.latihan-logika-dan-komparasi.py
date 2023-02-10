# Latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++3---------10+++++++
# inputUser = float(input(
#     'Masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:'))

# ++++++++++3---------------
# memeriksa angka kurang dari 3
# isKurangDari = (inputUser < 3)
# print("kurang dari 3 =", isKurangDari)

# ---10+++++++++++
# memeriksa angka lebih dari
# isLebihDari = (inputUser > 10)
# print("lebih dari 10 =", isLebihDari)

# +++++++3---------10+++++++

# angka = (inputUser < 3 or inputUser > 10)
# print('Nilai yang anda input = ', angka)


# ------3+++++++++10-------
inputUser = float(input(
    'Masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:'))

# memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print('lebih dari 3 = ', isLebihDari)

# Memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)
print('kurang dari 10 =', isKurangDari)

# ------3+++++++++10-------
isCorrect = isLebihDari and isKurangDari
print('nilai yang anda input =', isCorrect)
