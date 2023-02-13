# Latihan perulangan membuat segitiga

# sisi = 9

# 1. Menggunakan For

# dummy variable
# print('Awal dengan For')
# count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# print('=====================')
# print('Akhir dengan For\n')

# # 2. Menggunakan while

# print('Awal dengan While')
# count = 1
# while True:
#     print('*'*count)
#     count += 1

#     if count > sisi:
#         break

# print('Akhir dengan While')


# 3. Hanya ganjil saja

# print('Awal dengan While')
# count = 1
# while True:
# akan kembali keatas jika ganjil
# if (count % 2):
#     # print jika ganjil
#     print('*'*count)
#     count += 1
# else:
# akan kembali keatas jika genap
# count += 1
# continue

# akan break jika count melebihi sisi
#     if count > sisi:
#         break

# print('Akhir dengan While')


# 4. Hanya ganjil saja

# print('Awal dengan While')
# count = 1
# spasi = int(sisi / 2)
# while True:
#     # akan kembali keatas jika ganjil
#     if (count % 2):
#         # print jika ganjil
#         prin  t(" "*spasi, '+'*count)
#         spasi -= 1
#         count += 1
#     else:
# akan kembali keatas jika genap
# count += 1
# continue

# akan break jika count melebihi sisi
#     if count > sisi:
#         break
# while True:
#     if (count % 2):
#         spasi += 1
#         print(" "*spasi, "+"*count)
#         count -= 1
#     else:
#         count -= 1
#         if count == 0:
#             break
# print('Akhir dengan While')

count = 1
sisi = int(input("Masukan sisi segitiga : "))
spasi = int(sisi/2)
while True:
    if (count % 2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count % 2):
        spasi += 1
        print(" "*spasi, "+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break

# while True:
#     if
