# Program List Buku

list_buku = []
while True:
    print('\nMasukan Data Buku')
    judul = input('Judul Buku \t\t: ')
    penulis = input('Masukan Nama Penulis \t: ')

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print("=" * 20, "DATA BUKU BACAAN", "=" * 20)
    for index, buku in enumerate(list_buku):
        print(f"{index+1}. | {buku[0]}\t| {buku[1]}  ")

    print("=" * 40)
    isLanjut = input("Apakah di lanjutkan? (y / n) ")
    if isLanjut == "n":
        break

print("Program Selesai!! Terimakasih")
