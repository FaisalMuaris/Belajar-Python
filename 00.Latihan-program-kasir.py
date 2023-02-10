print("===== Program Kasir Sederhana =====")
pembeli = input("Masukan nama Pembeli: ")
print(f"Nama Pembeli : {pembeli}")


def fungsiMakanan():
    global totalMakan
    global porsi
    global makan
    print("\n ===== Menu Makanan =====")
    print("1. Nasi Goreng - Rp. 15000")
    print("2. Soto Ayam   - Rp. 12000")
    print("3. Nasi Bebek  - Rp. 20000")
    print("4. Tidak Memesan")
    nomor = int(input("Masukan Pilihan : "))
    porsi = int(input("Berapa Porsi    : "))

    if nomor == 1:
        totalMakan = porsi * 15000
        print(porsi, f"porsi Nasi Goreng = Rp.{totalMakan}")
        makan = "Nasi Goreng"
    elif nomor == 2:
        totalMakan = porsi * 12000
        print(porsi, f"porsi Soto Ayam = Rp. {totalMakan} ")
        makan = "Soto Ayam"
    elif nomor == 3:
        totalMakan = porsi * 20000
        print(porsi, f"porsi Nasi Bebek = Rp. {totalMakan} ")
        makan = "Nasi Bebek"
    elif nomor == 4:
        totalMakan = porsi * 0
        print('Tidak Memesan!')
        makan = "Tidak Memesan!"

    else:
        print("Pilihan tidak ada, silahkan pilih kembali!!")
        fungsiMakanan()


def fungsiMinuman():
    global totalMinum
    global minum
    global gelas
    print("\n ===== Menu Minuman =====")
    print("1. Es Jeruk  - Rp. 4000")
    print("2. Jus Jeruk - Rp. 5000")
    print("3. Es Kelapa - Rp. 7000")
    nomor = int(input("Masukan Pilihan : "))
    gelas = int(input("Berapa Gelas    : "))

    if nomor == 1:
        totalMinum = gelas * 4000
        print(gelas, f" Gelas Es Jeruk = Rp. {totalMinum} ")
        minum = " Gelas Es Jeruk"
    elif nomor == 2:
        totalMinum = gelas * 5000
        print(gelas, f" Gelas Jus Jeruk - Rp. {totalMinum} ")
        minum = " Jus Jeruk"
    elif nomor == 3:
        totalMinum = gelas * 7000
        print(gelas, f" Gelas Es Kelapa - Rp. {totalMinum} ")
        minum = " Es Kelapa"
    else:
        print("Pilihan Tidak Ada")
        fungsiMinuman()


fungsiMakanan()
fungsiMinuman()
totalSemua = totalMakan + totalMinum

print(f"\nTotal Harus dibayar: Rp. {totalSemua:,} ")
uang = int(input("Uang Tunai Pembeli : Rp. "))
kembalian = int(uang - totalSemua)
print(f"Kembalian\t   : Rp. {kembalian:,} ")

print("\n===========================")
print("\n======= STRUK BELI ========")
print("\n===========================")

print(f"Nama\t\t: {pembeli} ")
print(f"Beli\t\t: {porsi} {makan} (Rp. {totalMakan:,}) ")
print(f"\t\t  {gelas}{minum} (Rp. {totalMinum:,}) ")
print(f"Tagihan\t\t: Rp. {totalSemua:,}")
print(f"Dibayar\t\t: Rp. {uang:,}")
print(f"Kembalian\t: Rp. {kembalian:,} ")
print("===========================")
print("===========================")
