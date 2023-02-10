# Continue dan Pass

# Pass -> dia berfungsi sebagai dummy, tidak akan di eksekusi

# angka = 0

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass  # ini tidak akan di eksekusi

#     print(angka)


# Continue

# angka = 0

# print(f"angka sekarang {angka}")

# while angka < 5:
#     angka += 1
#     print(f"angka sekarang {angka}")  # aksi satu
#     if angka == 3:
#         print("niicccee")
#         continue  # membbuat loop meloncat ke step selanjutnya
#     print("slowwwmann")  # aksi dua

# print('finish')

# =============================
#               Break
# =============================


angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang {angka}")

    if angka == 3:
        print('cakeeepp')
        break

    print('slebewww')

print('======================')
print('finishh')

# ==========================================
data_int = int(input('hitung sampai = '))

angka = 0

while True:
    angka += 1
    print(f"angka sekarang {angka}")

    if angka == data_int:
        print('cakeeepp')
        break

    print('slebewww')

print('======================')
print('finishh')
